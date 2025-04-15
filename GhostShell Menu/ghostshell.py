import os
import services
import sims4.commands
import sims4.resources
from sims4.resources import Types, get_resource_key
from GS_enums.traits_enum import GSTrait
from GS_enums.skills_enum import GSSkill
from GS_enums.constants_enum import GSAge, GSCareer
from relationships.relationship_tracker import RelationshipTracker
from relationships.relationship_track import RelationshipTrack


# Helper functions
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
        output(f"Resolved skill: {getattr(skill, '__name__', 'None')}") if skill else output(f"Failed to resolve skill {skill_id}")
        if not skill:
            continue

        tracker = sim.get_tracker(skill)
        if tracker is None:
            output(f"No tracker found for skill {skill.__name__}. Adding tracker.")
            sim.add_tracker(skill)
            tracker = sim.get_tracker(skill)

        if not tracker.has_statistic(skill):
            output(f"Statistic for skill {skill.__name__} not found. Adding it.")
            tracker.add_statistic(skill)

        try:
            stat = tracker.get_statistic(skill, add=True)
            if stat and hasattr(stat, 'set_value'):
                stat.set_value(skill_levels[10])
                if hasattr(stat, 'show_on_ui'):
                    stat.show_on_ui = True
                output(f"Successfully applied skill {skill.__name__}.")
            else:
                output(f"Skill {skill.__name__} cannot be applied to this Sim.")
        except Exception as e:
            output(f"Error applying skill {skill.__name__}: {e}")
            continue  # Ensure the loop continues even if an error occurs


def set_relationship(sim_info_a, sim_info_b, friendship_score: float = 100.0, romance_score: float = 100.0):
    # Ensure both Sims have relationship trackers
    if not sim_info_a.relationship_tracker or not sim_info_b.relationship_tracker:
        return

    # Add relationship if it doesn't exist
    if not sim_info_a.relationship_tracker.has_relationship(sim_info_b.sim_id):
        sim_info_a.relationship_tracker.create_relationship(sim_info_b.sim_id)
        sim_info_b.relationship_tracker.create_relationship(sim_info_a.sim_id)

    # Set friendship score
    sim_info_a.relationship_tracker.set_relationship_score(sim_info_b.sim_id, friendship_score, track_type='friendship')

    # Set romance score
    sim_info_a.relationship_tracker.set_relationship_score(sim_info_b.sim_id, romance_score, track_type='romance')


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
    "royal": {
        "add": [
            GSTrait.ARCHAEOLOGYSKILL_GIVEAUTHENTICATIONMAIL_PROHIBIT, GSTrait.FAMETRAITS_SHINE_OFF,
            GSTrait.ACTIVE, GSTrait.CHAMPIONOFTHEPEOPLE, GSTrait.CONNECTIONS,
            GSTrait.DOCTOR_SICKNESSRESISTANT, GSTrait.FREESERVICES, GSTrait.FRUGAL,
            GSTrait.GENDEROPTIONS_ATTRACTEDTO_FEMALE, GSTrait.GENDEROPTIONS_SEXUALITY_EXPLORING,
            GSTrait.GYMRAT, GSTrait.HANDYPERSON_GOLDENWRENCH, GSTrait.HIGH_METABOLISM,
            GSTrait.INCREDIBLYFRIENDLY, GSTrait.INSIDER, GSTrait.INTHEKNOW,
            GSTrait.INVESTED, GSTrait.LEGENDARY, GSTrait.LIFESKILLS_GOODMANNERS,
            GSTrait.LIFESKILLS_RESPONSIBLE, GSTrait.LIFESTYLES_ENERGETIC, GSTrait.LIVINGVICARIOUSLY,
            GSTrait.MASTERTRAINER, GSTrait.MENTOR, GSTrait.PAMATRIARCH,
            GSTrait.PARENTINGSKILL_UNDERSTANDBABY, GSTrait.PHYSICALLYGIFTED, GSTrait.PROPER,
            GSTrait.QUICK_LEARNER, GSTrait.RELATABLE, GSTrait.SAVANT, GSTrait.SELFASSURED,
            GSTrait.SEXUALORIENTATION_WOOHOOINTERESTS_FEMALE, GSTrait.SICKNESSIMMUNITY, GSTrait.STORMCHASER,
            GSTrait.SUPERPARENT_ROLEMODEL, GSTrait.SURVIVALINSTINCT, GSTrait.TEMPERATURE_BURNINGMAN,
            GSTrait.TEMPERATURE_ICEMAN, GSTrait.THEKNACK, GSTrait.WATERPROOF, GSTrait.WISE,
            GSTrait.WORLDLYKNOWLEDGE, GSTrait.WICKEDWHIMS_NUDITYAVOIDER, GSTrait.WICKEDWHIMS_RELATIONSHIPS_POLY,
            GSTrait.WICKEDWHIMS_SEX_ALWAYSACCEPT, GSTrait.WICKEDWHIMS_SEX_ATTRIBUTE_GENEROUSLOVER
        ],
        "IfTeenAdd": [GSTrait.HSEXIT_GRADUATE_EARLY, GSTrait.WICKEDWHIMS_POSTPUBERTYTEEN],
        "IfMaleAdd": [
            GSTrait.BUSINESS_SAVVY, GSTrait.ICONIC, GSTrait.MOTIVATINGSPEAKER,
            GSTrait.UNIVERSITY_COMMUNICATIONSDEGREEBSHONORS, GSTrait.UNIVERSITY_ECONOMICSDEGREEBSHONORS, GSTrait.WICKEDWHIMS_SEX_CUCKOLD
        ],
        "IfFemaleAdd": [
            GSTrait.ALLURING, GSTrait.GENDEROPTIONS_ATTRACTEDTO_MALE, GSTrait.GREATKISSER,
            GSTrait.PERFECTHOST, GSTrait.SEXUALORIENTATION_WOOHOOINTERESTS_MALE, GSTrait.SOCIALLYGIFTED,
            GSTrait.UNIVERSITY_ARTHISTORYDEGREEBSHONORS, GSTrait.UNIVERSITY_HISTORYDEGREEBSHONORS,
            GSTrait.UNIVERSITY_LANGUAGEANDLITERATUREDEGREEBSHONORS, GSTrait.WELLNESS_SELFCAREEXPERTISE,
            GSTrait.WICKEDWHIMS_ATTRACTIVENESS_SIMPREFERENCE_LIKES_FACIALHAIR_BEARD, GSTrait.WICKEDWHIMS_ATTRACTIVENESS_SIMPREFERENCE_LIKES_HAIRCOLOR_BROWN,
            GSTrait.WICKEDWHIMS_BODYHAIR_PUBICHAIR_ISDISABLED, GSTrait.WICKEDWHIMS_CUMSLUT, GSTrait.WICKEDWHIMS_MENSTRUALCYCLE_NOBLEEDING,
            GSTrait.WICKEDWHIMS_RELATIONSHIPS_SEXCHEATER, GSTrait.WICKEDWHIMS_SEX_SEXUALLYALLURING, GSTrait.REWARD_INCEST
        ],
        "remove": [
            GSTrait.FAMETRAITS_CELEBRITYWALK_ON, GSTrait.FERTILE, GSTrait.GENDEROPTIONS_SEXUALITY_NOTEXPLORING, GSTrait.HIGHMAINTENANCE
        ],
        "IfFemaleRemove": [],
        "skills": [
            GSSkill.WW_SEXPERTISE, GSSkill.ARCHAEOLOGY, GSSkill.CHARISMA, GSSkill.COOKING,
            GSSkill.FITNESS, GSSkill.HANDINESS, GSSkill.LOGIC, GSSkill.PARENTING, GSSkill.PROGRAMMING,
            GSSkill.ROCKCLIMB, GSSkill.ROCKETSCIENCE, GSSkill.SKIING
        ],
        "IfFemaleSkills": [GSSkill.WELLNESS],
        "IfMaleSkills": [GSSkill.ENTREPRENEUR],
        "IfToddlerSkills": [
            GSSkill.COMMUNICATION, GSSkill.IMMAGINATION, GSSkill.MOVEMENT, GSSkill.POTTY, GSSkill.THINKING
        ],
        "IfChildSkills": [
            GSSkill.CREATIVITY, GSSkill.MENTAL, GSSkill.MOTOR, GSSkill.SOCIAL
        ],
        "IfTeenSkills": []
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

            if command in ["me", "my", "royal", "service"] and sim.career_tracker is not None:
                if sim.age == GSAge.TEEN:
                    school = sim.career_tracker.get_career_by_uid(137624)
                    if school:
                        sim.career_tracker.remove_career(school)
                        output("Removed school career from teen sim.")
                elif command == "my" and sim.age == GSAge.CHILD:
                    school = sim.career_tracker.get_career_by_uid(135606)
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
    ged_trait_id = 291086
    ged_trait = trait_manager.get(get_resource_key(ged_trait_id, Types.TRAIT))

    if sim.career_tracker is not None:
        if sim.age == GSAge.TEEN:
            school = sim.career_tracker.get_career_by_uid(137624)
            if school:
                sim.career_tracker.remove_career(school)
                output("Removed school career from teen sim.")
        elif sim.age == GSAge.CHILD:
            school = sim.career_tracker.get_career_by_uid(135606)
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

    # Output the Sim's ID
    output(f"{sim.first_name} {sim.last_name} has Sim ID: {sim.sim_id}")


@sims4.commands.Command('gs.bob', command_type=sims4.commands.CommandType.Live)
def add_relationship_with_bob(*args, _connection=None):
    client = services.client_manager().get(_connection)
    output = sims4.commands.CheatOutput(_connection)

    # Resolve Bob Dow
    bob = resolve_sim(["Bob", "Dow"], client)
    if not bob:
        output("Error: Could not resolve Bob Dow.")
        return

    # Resolve the active Sim
    sim = client.active_sim.sim_info
    if not sim:
        output("Error: Could not resolve the active Sim.")
        return

    # Set a friendly and romantic relationship with Bob Dow
    set_relationship(
        sim_info_a=sim,
        sim_info_b=bob,
        friendship_score=50,
        romance_score=30
    )
    output("Successfully set a friendly and romantic relationship with Bob Dow.")
