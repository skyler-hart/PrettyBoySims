from sims4.resources import Types, get_resource_key
from pbs_skills import *
from pbs_traits import *
import os
import services, sims4.commands


@sims4.commands.Command('pbs_service', command_type=sims4.commands.CommandType.Live)
def pbs_service(_connection=None):
    # Get the console output
    output = sims4.commands.CheatOutput(_connection)

    # Get the sim_info for the active sim
    sim = services.client_manager().get(_connection).active_sim.sim_info

    # Get the tuned trait instance from the tuning instance manager
    instance_manager = services.get_instance_manager(Types.TRAIT)

    # Remove all non-core traits from the Sim
    trait_manager = services.get_instance_manager(Types.TRAIT)
    skill_manager = services.get_instance_manager(Types.STATISTIC)
    all_traits = list(sim._traits)

    # List of trait categories to preserve
    core_trait_ids = set()

    # Add known "do not touch" traits here (gender, age, occult, etc.)
    # These can be expanded as needed
    core_trait_ids.update(sim.age_trait.guid64)                 # age trait
    core_trait_ids.update(sim.gender_trait.guid64)              # gender trait
    core_trait_ids.update(sim.occult_tracker.get_occult_trait_ids())  # vampire, werewolf, mermaid, etc.

    for trait in all_traits:
        trait_id = trait.guid64 if hasattr(trait, 'guid64') else None
        if trait_id in core_trait_ids:
            continue  # Skip protected traits

        sim.remove_trait(trait)

    # Set Handiness Skill to 10.0 (add if missing)
    handy_skill = skill_manager.get(S_HANDINESS)  # Skill ID from pbs_s_ids

    if handy_skill:
        # Ensure the Sim has a tracker for the skill
        sim_tracker = sim.get_tracker(handy_skill)
        if not sim_tracker.has_statistic(handy_skill):
            sim_tracker.add_statistic(handy_skill)

        # Now set the value
        sim_tracker.set_value(handy_skill, 10.0)

    # Add The Knack trait if not already present
    the_knack_trait = trait_manager.get(get_resource_key(TRAIT_THEKNACK, Types.TRAIT))

    if the_knack_trait:
        if not sim.has_trait(the_knack_trait):
            sim.add_trait(the_knack_trait)


@sims4.commands.Command('pbs_white', command_type=sims4.commands.CommandType.Live)
def pbs_white(_connection=None):
    # Get the console output
    output = sims4.commands.CheatOutput(_connection)

    # Get the sim_info for the active sim
    sim = services.client_manager().get(_connection).active_sim.sim_info

    # Get the tuned trait instance from the tuning instance manager
    instance_manager = services.get_instance_manager(Types.TRAIT)

    wickedwhims_trait_white_romance = instance_manager.get(get_resource_key(WICKEDWHIMS_TRAIT_WHITE_ROMANCE, Types.TRAIT))
    if not sim.has_trait(wickedwhims_trait_white_romance):
        sim.add_trait(wickedwhims_trait_white_romance)


@sims4.commands.Command('pbs_maxskill', command_type=sims4.commands.CommandType.Live)
def pbs_maxskill(_connection=None):
    # Get the console output
    output = sims4.commands.CheatOutput(_connection)

    # Get the sim_info for the active sim
    sim = services.client_manager().get(_connection).active_sim.sim_info

    # Max out all skills
    skill_manager = services.get_instance_manager(Types.STATISTIC)
    all_skills = [s for s in skill_manager.types.values() if hasattr(s, 'max_level') and s.max_level > 0]

    for skill in all_skills:
        tracker = sim.get_tracker(skill)
        if not tracker.has_statistic(skill):
            tracker.add_statistic(skill)

        tracker.set_value(skill, float(skill.max_level))
