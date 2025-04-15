# ghostshell_main.pyc was compiled from the following Python source code:

import os
import sims4.commands # type: ignore
import services # type: ignore
from sims4.resources import Types, get_resource_key # type: ignore
from GS_enums.constants_enum import GSAge, GSCareer
from .dictionaries import ghostshell_trait_commands
from GS_enums.traits_enum import GSTrait
from GS_enums.skills_enum import GSSkill

# Helper functions for traits and skills
def resolve_sim(args, client):
    """
    Resolves a Sim by name or defaults to the active Sim.
    Args:
        args: Command arguments, expected to contain the Sim's first and/or last name.
        client: The client object to access the active Sim and other Sims.

    Returns:
        The resolved SimInfo object or None if no match is found.
    """
    if not args:
        return client.active_sim.sim_info  # Default to the active Sim if no arguments are provided

    input_name = " ".join(args).lower()  # Combine arguments into a single name string
    sim_manager = services.sim_info_manager()
    matched_sims = []

    for sim_info in sim_manager.get_all():
        full_name = f"{sim_info.first_name} {sim_info.last_name}".lower()
        if input_name in full_name:  # Check for partial match
            matched_sims.append(sim_info)

    if len(matched_sims) == 1:
        return matched_sims[0]  # Return the single match
    elif len(matched_sims) > 1:
        # If multiple matches, log them and return the first match
        output = sims4.commands.CheatOutput(client.id)
        output("Multiple Sims matched the name:")
        for sim in matched_sims:
            output(f" - {sim.first_name} {sim.last_name} (ID: {sim.sim_id})")
        return matched_sims[0]  # Default to the first match
    else:
        return None  # No match found


def _apply_traits(sim, output, trait_manager, traits):
    for trait_id in traits:
        trait = trait_manager.get(get_resource_key(trait_id, Types.TRAIT))
        output(f"Resolved trait: {getattr(trait, '__name__', 'None')}" if trait else f"Failed to resolve trait {trait_id}")
        if trait and not sim.has_trait(trait):
            sim.add_trait(trait)


def _remove_traits(sim, output, trait_manager, traits):
    for trait_id in traits:
        trait = trait_manager.get(get_resource_key(trait_id, Types.TRAIT))
        output(f"Resolved trait for removal: {getattr(trait, '__name__', 'None')}" if trait else f"Failed to resolve trait {trait_id}")
        if trait and sim.has_trait(trait):
            sim.remove_trait(trait)


def _apply_skills(sim, output, skill_manager, skills):
    # This HAS to stay in place. Just setting everything to 81580 doesn't work.
    # The game uses a different set of levels for each skill, so we need to set them individually.
    skill_levels = [0, 100, 1540, 3700, 7300, 12580, 19780, 29920, 43360, 60460, 81580]

    for skill_id in skills:
        skill = skill_manager.get(get_resource_key(skill_id, Types.STATISTIC))
        output(f"Resolved skill: {getattr(skill, '__name__', 'None')}" if skill else f"Failed to resolve skill {skill_id}")
        if not skill:
            continue

        tracker = sim.get_tracker(skill)
        if tracker is None:
            output(f"No tracker found for skill {skill.__name__}. Skipping.")
            continue

        if not tracker.has_statistic(skill):
            tracker.add_statistic(skill)
        stat = None
        try:
            stat = tracker.get_statistic(skill, add=True)
        except Exception as e:
            output(f"Error getting statistic for skill {skill.__name__}: {e}")
            continue

        if stat:
            try:
                stat.set_value(skill_levels[10])
                stat.show_on_ui = True
            except Exception as e:
                output(f"Error applying value or UI to skill {skill.__name__}: {e}")
        else:
            output(f"Tracker returned no statistic for skill {skill.__name__} (ID {skill_id})")


def set_relationship(sim, target_sim, friendship_score, romantic_bit_id, just_friends, output, romantic_score=None):
    """Sets the relationship between two Sims."""
    sim.relationship_tracker.add_relationship_score(target_sim.sim_id, friendship_score, "friendship")

    if not just_friends:
        # Ensure both Sims are teen or older for romantic relationships
        if sim.age >= GSAge.TEEN.value and target_sim.age >= GSAge.TEEN.value:
            bit_manager = services.get_instance_manager(Types.RELATIONSHIP_BIT)
            romantic_bit = bit_manager.get(get_resource_key(romantic_bit_id, Types.RELATIONSHIP_BIT))
            if romantic_bit:
                sim.relationship_tracker.add_relationship_bit(target_sim.sim_id, romantic_bit)
                output(f"Romantic interest set with {target_sim.first_name} {target_sim.last_name}")
                # Set romantic score if provided
                if romantic_score is not None:
                    sim.relationship_tracker.add_relationship_score(target_sim.sim_id, romantic_score, "romance")
                    output(f"Romantic relationship score set to {romantic_score} with {target_sim.first_name} {target_sim.last_name}")
            else:
                output(f"Failed to resolve romantic relationship bit ID: {romantic_bit_id}")
        else:
            output("Romantic relationships can only be set for Sims who are Teen or older.")
    else:
        output(f"Set as friends with {target_sim.first_name} {target_sim.last_name} only")


for command, actions in ghostshell_trait_commands.items():
    def make_command(command=command, actions=actions):
        @sims4.commands.Command(f'gs.{command}', command_type=sims4.commands.CommandType.Live)
        def command_fn(*args, _connection=None):
            client = services.client_manager().get(_connection)
            output = sims4.commands.CheatOutput(_connection)
            sim = client.active_sim.sim_info
            household = sim.household

            # Get the household and sims in it
            # Auto-pay bills for the household
            if command in ["me", "my", "service", "curated", "royal"]:
                if household and hasattr(household, 'bills_manager'):
                    bills = household.bills_manager
                    if hasattr(bills, 'pay_all_bills'):
                        bills.pay_all_bills()
                        output("Auto-paid household bills.")

            trait_manager = services.get_instance_manager(Types.TRAIT)
            skill_manager = services.get_instance_manager(Types.STATISTIC)

            if command in ["my", "service"] and sim.career_tracker is not None:
                if sim.age == GSAge.TEEN:
                    school = sim.career_tracker.get_career_by_uid(GSCareer.HighSchool)
                    if school:
                        sim.career_tracker.remove_career(school)
                        output("Removed school career from teen sim.")
                elif command == "my" and sim.age == GSAge.CHILD:
                    school = sim.career_tracker.get_career_by_uid(GSCareer.HighSchool)
                    if school:
                        sim.career_tracker.remove_career(school)
                        output("Removed school career from child sim.")

            # Remove traits
            _remove_traits(sim, output, trait_manager, actions.get("remove", []))
            if sim.is_female:
                _remove_traits(sim, output, trait_manager, actions.get("IfFemaleRemove", []))
            elif sim.is_male:
                _remove_traits(sim, output, trait_manager, actions.get("IfMaleRemove", []))

            # Apply traits
            if sim.is_female:
                _apply_traits(sim, output, trait_manager, actions.get("IfFemaleAdd", []))
            else:
                _apply_traits(sim, output, trait_manager, actions.get("IfMaleAdd", []))

            if sim.age == GSAge.TODDLER:
                _apply_traits(sim, output, trait_manager, actions.get("IfToddlerAdd", []))
            elif sim.age == GSAge.CHILD:
                _apply_traits(sim, output, trait_manager, actions.get("IfChildAdd", []))
            elif sim.age == GSAge.TEEN:
                _apply_traits(sim, output, trait_manager, actions.get("IfTeenAdd", []))

            _apply_traits(sim, output, trait_manager, actions.get("add", []))

            # Add age based skills
            if sim.age == GSAge.TODDLER:
                _apply_skills(sim, output, skill_manager, actions.get("IfToddlerSkills", []))
            elif sim.age == GSAge.CHILD:
                _apply_skills(sim, output, skill_manager, actions.get("IfChildSkills", []))
            elif sim.age == GSAge.TEEN:
                _apply_skills(sim, output, skill_manager, actions.get("IfTeenSkills", []))

            # Add gender based skills
            if sim.is_female:
                _apply_skills(sim, output, skill_manager, actions.get("IfFemaleSkills", []))
            elif sim.is_male:
                _apply_skills(sim, output, skill_manager, actions.get("IfMaleSkills", []))

            # Apply general skills
            _apply_skills(sim, output, skill_manager, actions.get("skills", []))

        return command_fn

    make_command(command, actions)


@sims4.commands.Command('gs.removeschool', command_type=sims4.commands.CommandType.Live)
def remove_school_command(_connection=None):
    client = services.client_manager().get(_connection)
    output = sims4.commands.CheatOutput(_connection)
    sim = client.active_sim.sim_info

    trait_manager = services.get_instance_manager(Types.TRAIT)
    ged_trait_id = GSTrait.HSEXIT_EARNEDGED
    ged_trait = trait_manager.get(get_resource_key(ged_trait_id, Types.TRAIT))

    if sim.career_tracker is not None:
        if sim.age == GSAge.TEEN:
            school = sim.career_tracker.get_career_by_uid(GSCareer.HighSchool)
            if school:
                sim.career_tracker.remove_career(school)
                output("Removed school career from teen sim.")
        elif sim.age == GSAge.CHILD:
            school = sim.career_tracker.get_career_by_uid(GSCareer.GradeSchool)
            if school:
                sim.career_tracker.remove_career(school)
                output("Removed school career from child sim.")

    if ged_trait and not sim.has_trait(ged_trait):
        sim.add_trait(ged_trait)
        output(f"Added GED trait: {ged_trait.__name__} (ID {ged_trait_id})")


@sims4.commands.Command('gs.simid', command_type=sims4.commands.CommandType.Live)
def get_sim_id_command(*args, _connection=None):
    client = services.client_manager().get(_connection)
    output = sims4.commands.CheatOutput(_connection)

    # Resolve the Sim by name or default to the active Sim
    sim = resolve_sim(args, client)
    if not sim:
        output("Error: Could not resolve the Sim.")
        return

    # Output the Sim's name and ID
    output(f"Sim Name: {sim.first_name} {sim.last_name}, Sim ID: {sim.sim_id}")
