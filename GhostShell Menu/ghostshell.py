# ghostshell_main.pyc was compiled from the following Python source code:

import os
import sims4.commands
import services
from sims4.resources import Types, get_resource_key

# Helper functions for traits and skills


def _apply_traits(sim, output, trait_manager, traits):
    for trait_id in traits:
        trait = trait_manager.get(get_resource_key(trait_id, Types.TRAIT))
        if trait and not sim.has_trait(trait):
            sim.add_trait(trait)
            output(f"Added trait: {trait.__name__} (ID {trait_id})")


def _remove_traits(sim, output, trait_manager, traits):
    for trait_id in traits:
        trait = trait_manager.get(get_resource_key(trait_id, Types.TRAIT))
        if trait and sim.has_trait(trait):
            sim.remove_trait(trait)
            output(f"Removed trait {trait.__name__} (ID {trait_id})")


def _apply_skills(sim, output, skill_manager, skills):
    fitness_levels = [0, 100, 1540, 3700, 7300, 12580, 19780, 29920, 43360, 60460, 81580]

    for skill_id in skills:
        skill = skill_manager.get(get_resource_key(skill_id, Types.STATISTIC))
        if skill:
            tracker = sim.get_tracker(skill)
            if not tracker.has_statistic(skill):
                tracker.add_statistic(skill)
            stat = tracker.get_statistic(skill, add=True)
            if stat:
                stat.set_value(fitness_levels[10])
                output(f"Skill maxed: {skill.__name__} from ID {skill_id}")
            else:
                output(f"Failed to apply skill {skill.__name__} from ID {skill_id}")
        else:
            output(f"Failed to resolve skill {skill_id}")

# Dictionary populated from the spreadsheet logic
ghostshell_trait_commands = {
    "me": {
        "IfChildAdd": [],
        "IfToddlerAdd": [],
        "IfMaleAdd": [],
        "add": [],
        "IfChildAdd": [],
        "IfToddlerAdd": [],
        "IfMaleAdd": [],
        "remove": [],
        "IfFemaleAdd": [],
        "IfFemaleRemove": [],
        "IfTeenAdd": [3455194433],
        "skills": [],
        "IfTeenSkills": [],
        "IfChildSkills": [],
        "IfToddlerSkills": []
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
    }
}

for command, actions in ghostshell_trait_commands.items():
    def make_command(command, actions):
        @sims4.commands.Command(f'gs.{command}', command_type=sims4.commands.CommandType.Live)
        def command_fn(*args, _connection=None):
            from relationships.relationship_tracker import RelationshipTrackType
            from sims.sim_info_types import BodyType
            from sims.sim_info_manager import SimInfoManager
            sim = client.active_sim.sim_info
            if not sim:
                output("No active sim.")
                return

            # Get the household and sims in it
            household = sim.household
            if command == "myplayed":
                if household:
                    household.funds = 500000
                    sims_in_house = list(household.sim_info_gen())
                    for sim_a in sims_in_house:
                        for sim_b in sims_in_house:
                            if sim_a is not sim_b:
                                sim_a.relationship_tracker.add_relationship_score(sim_b.sim_id, 100, RelationshipTrackType.FRIENDSHIP_TRACK)

                    # Get Bob Dow by name and make each household sim friends with him
                    sim_manager = services.sim_info_manager()
                    for other_sim in sim_manager.get_all():
                        if other_sim.full_name.lower() == "bob dow":
                            for sim_a in sims_in_house:
                                sim_a.relationship_tracker.add_relationship_score(other_sim.sim_id, 100, RelationshipTrackType.FRIENDSHIP_TRACK)
                            break
                output("No active sim.")
                return

            trait_manager = services.get_instance_manager(Types.TRAIT)
            skill_manager = services.get_instance_manager(Types.STATISTIC)

            _remove_traits(sim, output, trait_manager, actions.get("remove", []))
            if sim.is_female:
                _remove_traits(sim, output, trait_manager, actions.get("IfFemaleRemove", []))

            if sim.is_female:
                _apply_traits(sim, output, trait_manager, actions.get("IfFemaleAdd", []))
            else:
                _apply_traits(sim, output, trait_manager, actions.get("IfMaleAdd", []))
            if sim.age == 2:
                _apply_traits(sim, output, trait_manager, actions.get("IfTeenAdd", []))
            elif sim.age == 1:
                _apply_traits(sim, output, trait_manager, actions.get("IfChildAdd", []))
            elif sim.age == 0:
                _apply_traits(sim, output, trait_manager, actions.get("IfToddlerAdd", []))
            _apply_traits(sim, output, trait_manager, actions.get("add", []))

            _apply_skills(sim, output, skill_manager, actions.get("skills", []))
            if sim.age == 2:
                _apply_skills(sim, output, skill_manager, actions.get("IfTeenSkills", []))
            elif sim.age == 1:
                _apply_skills(sim, output, skill_manager, actions.get("IfChildSkills", []))
            elif sim.age == 0:
                _apply_skills(sim, output, skill_manager, actions.get("IfToddlerSkills", []))

        return command_fn

    make_command(command, actions)
