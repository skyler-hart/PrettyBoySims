# ghostshell_main.pyc was compiled from the following Python source code:

import os
import sims4.commands # type: ignore
import services # type: ignore
from sims4.resources import Types, get_resource_key # type: ignore
Types.RELATIONSHIP_TRACK = 0x53E9A2C5  # Manually added constant
Types.TRAIT = getattr(Types, "TRAIT", 0xB13B13F)
Types.STATISTIC = getattr(Types, "STATISTIC", 0x7CA5C2DA)
from relationships.relationship_bit import RelationshipBit # type: ignore

# Define constants
AGE_BABY = 0
AGE_INFANT = 1
AGE_TODDLER = 2
AGE_CHILD = 3
AGE_TEEN = 4
AGE_YOUNGADULT = 5
AGE_ADULT = 6
AGE_ELDER = 7

# Helper functions for traits and skills
def find_sim_by_name(first_name, last_name):
    household_manager = services.household_manager()
    for household in household_manager.get_all():
        for sim in household.sim_info_gen():
            if sim.first_name.lower() == first_name.lower() and sim.last_name.lower() == last_name.lower():
                return sim  # Break early when found
    return None

def resolve_sim(args, client):
    """
    Resolve a Sim based on the provided arguments. If no arguments are provided,
    return the active Sim. If a name or Sim ID is provided, attempt to find the Sim.

    Args:
        args: List of arguments passed to the command.
        client: The client object to get the active Sim.

    Returns:
        The resolved SimInfo object or the active Sim if no arguments are provided.
    """
    if not args:
        return client.active_sim.sim_info

    arg = args[0].lower().replace('"', '')

    # Check if it's simid:<id>
    if arg.startswith("simid:"):
        try:
            sim_id = int(arg.replace("simid:", ""))
            sim_info = services.sim_info_manager().get(sim_id)
            if sim_info:
                return sim_info
        except ValueError:
            pass

    # Otherwise, treat it as a name and use find_sim_by_name
    name_arg = " ".join(args).strip().replace('"', '')
    first_name, *last_name = name_arg.split(" ")
    last_name = " ".join(last_name) if last_name else ""
    sim = find_sim_by_name(first_name, last_name)

    if sim:
        return sim

    # Fallback to the active Sim if no match is found
    return client.active_sim.sim_info

def process_sim_traits_and_skills(sim, output, actions):
    """Helper function to process traits and skills for a Sim."""
    trait_manager = services.get_instance_manager(Types.TRAIT)
    skill_manager = services.get_instance_manager(Types.STATISTIC)

    # Remove traits
    _remove_traits(sim, output, trait_manager, actions.get("remove", []))
    if sim.is_female:
        _remove_traits(sim, output, trait_manager, actions.get("IfFemaleRemove", []))
    elif sim.is_male:
        _remove_traits(sim, output, trait_manager, actions.get("IfMaleRemove", []))

    # Apply age-specific skills and general skills
    if sim.age == AGE_TEEN:
        output("Applying teen-specific skills...")
        _apply_skills(sim, output, skill_manager, actions.get("IfTeenSkills", []))
    elif sim.age == AGE_CHILD:
        output("Applying child-specific skills...")
        _apply_skills(sim, output, skill_manager, actions.get("IfChildSkills", []))
    elif sim.age == AGE_TODDLER:
        output("Applying toddler-specific skills...")
        _apply_skills(sim, output, skill_manager, actions.get("IfToddlerSkills", []))
    else:
        output(f"Sim age {sim.age} does not match any specific age group for skills.")

    _apply_skills(sim, output, skill_manager, actions.get("skills", []))

    # Apply traits based on gender
    if sim.is_female:
        _apply_traits(sim, output, trait_manager, actions.get("IfFemaleAdd", []))
    elif sim.is_male:
        _apply_traits(sim, output, trait_manager, actions.get("IfMaleAdd", []))

    # Apply traits based on age
    if sim.age == AGE_TEEN:
        _apply_traits(sim, output, trait_manager, actions.get("IfTeenAdd", []))
    elif sim.age == AGE_CHILD:
        _apply_traits(sim, output, trait_manager, actions.get("IfChildAdd", []))
    elif sim.age == AGE_TODDLER:
        _apply_traits(sim, output, trait_manager, actions.get("IfToddlerAdd", []))

    # Apply general traits
    _apply_traits(sim, output, trait_manager, actions.get("add", []))


def _apply_traits(sim, output, trait_manager, traits):
    for trait_id in traits:
        output(f"Resolving trait ID: {trait_id}")
        trait = trait_manager.get(get_resource_key(trait_id, Types.TRAIT))
        output(f"Resolved trait: {getattr(trait, '__name__', 'None')}" if trait else f"Failed to resolve trait {trait_id}")
        if trait and not sim.has_trait(trait):
            sim.add_trait(trait)
            output(f"Added trait: {trait.__name__} (ID {trait_id})")


def _remove_traits(sim, output, trait_manager, traits):
    for trait_id in traits:
        output(f"Resolving trait ID for removal: {trait_id}")
        trait = trait_manager.get(get_resource_key(trait_id, Types.TRAIT))
        output(f"Resolved trait for removal: {getattr(trait, '__name__', 'None')}" if trait else f"Failed to resolve trait {trait_id}")
        if trait and sim.has_trait(trait):
            sim.remove_trait(trait)
            output(f"Removed trait {trait.__name__} (ID {trait_id})")


def _apply_skills(sim, output, skill_manager, skills):
    """
    Apply a list of skills to a Sim and set them to the maximum level.

    Args:
        sim: The Sim to apply skills to.
        output: Function to send debug/output messages.
        skill_manager: The skill manager to resolve skill IDs.
        skills: A list of skill IDs to apply.
    """
    max_skill_value = 81580  # Maximum skill value

    for skill_id in skills:
        output(f"Attempting to resolve skill ID: {skill_id}")
        skill = skill_manager.get(get_resource_key(skill_id, Types.STATISTIC))

        if not skill:
            output(f"Error: Failed to resolve skill ID {skill_id}. Skipping...")
            continue

        output(f"Resolved skill: {skill.__name__} (ID {skill_id})")

        try:
            # Get the skill tracker for the Sim
            tracker = sim.get_tracker(skill)
            if not tracker:
                output(f"Error: No tracker found for skill {skill.__name__}. Skipping...")
                continue

            # Add the skill if it doesn't already exist
            if not tracker.has_statistic(skill):
                tracker.add_statistic(skill)

            # Get the skill statistic and set its value
            stat = tracker.get_statistic(skill, add=True)
            if stat:
                stat.set_value(max_skill_value)
                stat.show_on_ui = True  # Ensure the skill is visible in the UI
                output(f"Successfully maxed skill: {skill.__name__} (ID {skill_id})")
            else:
                output(f"Error: Failed to retrieve statistic for skill {skill.__name__}.")
        except Exception as e:
            output(f"Error applying skill {skill.__name__} (ID {skill_id}): {e}")


# Dictionary populated from the spreadsheet logic
ghostshell_trait_commands = {
    "me": {
        "IfChildAdd": [],
        "IfToddlerAdd": [],
        "IfMaleAdd": [],
        "add": [176123, 199156, 367987, 367988, 26200, 35504, 179023, 26203, 253268, 27082, 26476, 32431, 114410,
            277990, 26197, 249429, 32110, 26199, 32111, 16841, 276492, 137716, 137717, 276496, 27917, 26686,
            354602, 104486, 104487, 104480, 104481, 104484, 104485, 104482, 104483, 104488, 104489, 102783, 26393,
            144978, 27942, 230745, 31924, 231700, 132296, 32429, 26691, 32635, 29827, 163783, 149328, 26202, 16824,
            291675, 26439, 231050, 185795, 104880, 165025, 249731, 108876, 183508, 183507, 27328, 218130, 230325,
            230336, 185794, 27772, 18084875558065733633, 10684945704101449557, 15163032885896298056, 17070969323678292030,
            15260778326631125946, 460148084400330375, 12289485419405954221, 12054833788133711574
        ],
        "remove": [191807, 191819, 191820, 191817, 191818, 204539, 199155, 199223, 16854, 124879, 14185653986600082294,
            13684666234489556334, 10190719869461745074, 12967236809106674147, 9860031022131805491, 10205296704829281144
        ],
        "IfFemaleAdd": [276493, 27080, 291674, 270904, 1690154921011321723, 17143627558403278375, 4962284592606331639, 4027040388],
        "IfFemaleRemove": [],
        "IfTeenAdd": [3455194433, 277740],
        "skills": [5255876730914093336, 4641759162532272279, 11311871620839888931, 13681797894157322134, 15755652231701198849,
            18282882584276959514, 10913272126822913979, 16699, 16705, 231908, 16659, 16701, 16704, 16706, 160504,
            16703, 217413, 245639, 16710, 117858, 165900
        ],
        "IfTeenSkills": [],
        "IfChildSkills": [16718, 16719, 16720, 16721],
        "IfToddlerSkills": [140170, 140706, 136140, 144913, 140504]
    },
    "my": {
        "IfChildAdd": [],
        "IfToddlerAdd": [],
        "IfMaleAdd": [],
        "add": [],
        "remove": [],
        "IfFemaleAdd": [1690154921011321723],
        "IfFemaleRemove": [],
        "IfTeenAdd": [3455194433],
        "skills": [],
        "IfTeenSkills": [],
        "IfChildSkills": [],
        "IfToddlerSkills": []
    },
    "myplayed": {
        "IfChildAdd": [98698],
        "IfToddlerAdd": [],
        "IfMaleAdd": [],
        "add": [176123, 199156, 27419, 26388, 32110, 26199, 32111, 276492, 276496, 354602, 26389, 27942, 27086, 183024, 291675, 26439, 231050, 26639, 32621, 185795, 249731, 183508, 183507, 27328, 185794, 27772, 15163032885896298056, 17070969323678292030, 460148084400330375],
        "remove": [183505, 183506],
        "IfFemaleAdd": [26200, 276493, 27080, 29618, 291674, 258765, 269262, 270900, 18084875558065733633, 13329958653635829193, 17143627558403278375, 4962284592606331639],
        "IfFemaleRemove": [],
        "IfTeenAdd": [3455194433, 277740],
        "skills": [11311871620839888931, 104198, 16705, 16659, 16704, 16706, 117858],
        "IfTeenSkills": [],
        "IfChildSkills": [16718, 16719, 16720, 16721],
        "IfToddlerSkills": [140170, 140706, 136140, 144913, 140504]
    },
    "maid": {
        "IfChildAdd": [],
        "IfToddlerAdd": [],
        "IfMaleAdd": [],
        "add": [],
        "remove": [],
        "IfFemaleAdd": [],
        "IfFemaleRemove": [],
        "IfTeenAdd": [3455194433],
        "skills": [],
        "IfTeenSkills": [],
        "IfChildSkills": [],
        "IfToddlerSkills": []
    },
    "nanny": {
        "IfChildAdd": [],
        "IfToddlerAdd": [],
        "IfMaleAdd": [],
        "add": [],
        "remove": [],
        "IfFemaleAdd": [],
        "IfFemaleRemove": [],
        "IfTeenAdd": [3455194433],
        "skills": [],
        "IfTeenSkills": [],
        "IfChildSkills": [],
        "IfToddlerSkills": []
    },
    "service": {
        "IfChildAdd": [],
        "IfToddlerAdd": [],
        "IfMaleAdd": [],
        "add": [176123, 199156, 35504, 114410, 234887, 234566, 32111, 276492, 276493, 354602, 26393, 27942, 9602, 183034, 26392, 291675, 291674, 26639, 185795, 27328, 2639086337, 16286435799976315035, 13777170317512132992, 3256270857, 1646527862],
        "remove": [],
        "IfFemaleAdd": [1690154921011321723, 13329958653635829193, 17143627558403278375, 4962284592606331639, 18084875558065733633, 4027040388],
        "IfFemaleRemove": [],
        "IfTeenAdd": [3455194433],
        "skills": [231908, 16659, 16700, 16704, 11311871620839888931, 16649350022740743409],
        "IfTeenSkills": [],
        "IfChildSkills": [],
        "IfToddlerSkills": [],
    },
    "slave": {
        "IfChildAdd": [],
        "IfToddlerAdd": [],
        "IfMaleAdd": [],
        "add": [],
        "remove": [],
        "IfFemaleAdd": [],
        "IfFemaleRemove": [],
        "IfTeenAdd": [3455194433],
        "skills": [],
        "IfTeenSkills": [],
        "IfChildSkills": [],
        "IfToddlerSkills": []
    },
    "hot": {
        "IfChildAdd": [],
        "IfToddlerAdd": [],
        "IfMaleAdd": [],
        "add": [],
        "remove": [],
        "IfFemaleAdd": [],
        "IfFemaleRemove": [],
        "IfTeenAdd": [3455194433],
        "skills": [],
        "IfTeenSkills": [],
        "IfChildSkills": [],
        "IfToddlerSkills": []
    },
    "sub": {
        "add": [15713697132725812026, 15260778326631125946, 9860031022131805491, 14185653986600082294, 10190719869461745074, 460148084400330375],
        "IfFemaleAdd": [4962284592606331639],
        "IfTeenAdd": [3455194433],
        "skills": [11311871620839888931, 16649350022740743409, 12503627023949270877]
    },
    "dom": {
        "add": [10416229829191106747, 15163032885896298056, 17070969323678292030, 15713697132725812026, 15260778326631125946, 15354059437099474587],
        "IfFemaleAdd": [],
        "IfTeenAdd": [3455194433],
        "skills": []
    }
}

for command, actions in ghostshell_trait_commands.items():
    def make_command(command=command, actions=actions):
        @sims4.commands.Command(f'gs.{command}', command_type=sims4.commands.CommandType.Live)
        def command_fn(*args, _connection=None):
            client = services.client_manager().get(_connection)
            output = sims4.commands.CheatOutput(_connection)
            sim = resolve_sim(args, client)

            # Process traits and skills using the helper function
            process_sim_traits_and_skills(sim, output, actions)

            # Auto-pay bills for the household
            household = sim.household
            if household and hasattr(household, 'bills_manager'):
                bills = household.bills_manager
                if hasattr(bills, 'pay_all_bills'):
                    bills.pay_all_bills()
                    output("Auto-paid household bills.")

            # Remove school career if applicable
            if command in ["me", "my", "service"] and sim.career_tracker is not None:
                school = None
                if sim.age == AGE_TEEN:
                    school = sim.career_tracker.get_career_by_uid(137624)  # High School
                elif sim.age == AGE_CHILD:
                    school = sim.career_tracker.get_career_by_uid(135606)  # Grade School

                if school:
                    sim.career_tracker.remove_career(school)
                    output(f"Removed school career from {'teen' if sim.age == AGE_TEEN else 'child'} sim.")

        return command_fn

    make_command(command, actions)

@sims4.commands.Command('gs.lovebob', command_type=sims4.commands.CommandType.Live)
def love_bob_command(*args, _connection=None):
    from sims4.resources import Types, get_resource_key  # type: ignore # ensure resolve_sim has access
    client = services.client_manager().get(_connection)
    output = sims4.commands.CheatOutput(_connection)
    sim = resolve_sim(args, client)

    # Force -JustFriends for baby, infant, toddler, or child
    if sim.age in (AGE_BABY, AGE_INFANT, AGE_TODDLER, AGE_CHILD):
        args = list(args)
        if '-JustFriends' not in args:
            args.append('-JustFriends')

    # Determine if the relationship should be "just friends"
    just_friends = '-JustFriends' in args

    # Traits to add
    love_traits = [2503347606, 2425531959, 2308952560, 2819699501]
    trait_manager = services.get_instance_manager(Types.TRAIT)
    for trait_id in love_traits:
        trait = trait_manager.get(get_resource_key(trait_id, Types.TRAIT))
        if trait and not sim.has_trait(trait):
            sim.add_trait(trait)
            output(f"Added trait: {trait.__name__} (ID {trait_id})")

    # Find Bob Dow and set relationship
    bob_dow = find_sim_by_name("Bob", "Dow")
    if bob_dow:
        track_manager = services.get_instance_manager(Types.RELATIONSHIP_TRACK)
        friendship_key = get_resource_key(0x03B33, Types.RELATIONSHIP_TRACK)
        romance_key = get_resource_key(0x03B35, Types.RELATIONSHIP_TRACK)
        friendship_track = track_manager.get(friendship_key)
        romance_track = track_manager.get(romance_key)

        if not friendship_track or not hasattr(friendship_track, 'track_type'):
            output("Error: Invalid friendship track object")
            return
        if not romance_track or not hasattr(romance_track, 'track_type'):
            output("Error: Invalid romance track object")
            return

        relationship = sim.relationship_tracker._get_relationship(bob_dow.sim_id)
        relationship.track_tracker.load_data_if_needed()
        sim.relationship_tracker.set_relationship_score(bob_dow.sim_id, 100, friendship_track)
        score = sim.relationship_tracker.get_relationship_score(bob_dow.sim_id, friendship_track)
        output(f"Friendship score with Bob Dow is now {score}")

        can_romance = sim.age in (AGE_TEEN, AGE_YOUNGADULT, AGE_ADULT, AGE_ELDER) and bob_dow.age in (AGE_TEEN, AGE_YOUNGADULT, AGE_ADULT, AGE_ELDER)
        if not just_friends and can_romance:
            relationship.track_tracker.load_data_if_needed()
            sim.relationship_tracker.set_relationship_score(bob_dow.sim_id, 100, romance_track)
            score = sim.relationship_tracker.get_relationship_score(bob_dow.sim_id, romance_track)
            output(f"Romance score with Bob Dow is now {score}")
            tracker = sim.relationship_tracker
            bit_manager = services.get_instance_manager(Types.RELATIONSHIP_BIT)
            bit = bit_manager.get(get_resource_key(15745, Types.RELATIONSHIP_BIT))
            if bit:
                tracker.add_relationship_bit(bob_dow.sim_id, bit)
                output("Romantic interest set with Bob Dow")
        else:
            output(f"Set as friends with Bob Dow only")
    else:
        output(f"Bob Dow not found in current game session")


@sims4.commands.Command('gs.maxkidskills', command_type=sims4.commands.CommandType.Live)
def max_kid_skills(*args, _connection=None):
    client = services.client_manager().get(_connection)
    output = sims4.commands.CheatOutput(_connection)
    sim = resolve_sim(args, client)

    skill_manager = services.get_instance_manager(Types.STATISTIC)
    child_skills = [16718, 16719, 16720, 16721]
    toddler_skills = [140170, 140706, 136140, 144913, 140504]

    if sim.age == AGE_CHILD:
        _apply_skills(sim, output, skill_manager, child_skills)
    elif sim.age == AGE_TODDLER:
        _apply_skills(sim, output, skill_manager, toddler_skills)
    else:
        output("This command only applies to child or toddler Sims.")


@sims4.commands.Command('gs.removeschool', command_type=sims4.commands.CommandType.Live)
def remove_school_command(*args, _connection=None):
    client = services.client_manager().get(_connection)
    output = sims4.commands.CheatOutput(_connection)
    sim = resolve_sim(args, client)

    trait_manager = services.get_instance_manager(Types.TRAIT)
    ged_trait_id = 291086
    ged_trait = trait_manager.get(get_resource_key(ged_trait_id, Types.TRAIT))

    if sim.career_tracker is not None:
        if sim.age == AGE_TEEN:
            school = sim.career_tracker.get_career_by_uid(137624)
            if school:
                sim.career_tracker.remove_career(school)
                output(f"Removed school career from teen sim.")
        elif sim.age == AGE_CHILD:
            school = sim.career_tracker.get_career_by_uid(135606)
            if school:
                sim.career_tracker.remove_career(school)
                output(f"Removed school career from child sim.")

    if ged_trait and not sim.has_trait(ged_trait):
        sim.add_trait(ged_trait)
        output(f"Added GED trait: {ged_trait.__name__} (ID {ged_trait_id})")
