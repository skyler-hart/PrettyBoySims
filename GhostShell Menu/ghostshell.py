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
            output(f"Added trait {trait_id}")

def _remove_traits(sim, output, trait_manager, traits):
    for trait_id in traits:
        trait = trait_manager.get(get_resource_key(trait_id, Types.TRAIT))
        if trait and sim.has_trait(trait):
            sim.remove_trait(trait)
            output(f"Removed trait {trait_id}")

def _apply_skills(sim, output, skill_manager, skills):
    for skill_id in skills:
        skill = skill_manager.get(skill_id)
        if skill:
            tracker = sim.get_tracker(skill)
            if not tracker.has_statistic(skill):
                tracker.add_statistic(skill)
            tracker.set_value(skill, float(skill.max_level))
            output(f"Maxed skill {skill_id}")

# Dictionary populated from the spreadsheet logic
ghostshell_trait_commands = {
    "me": {
        "add": [164099],
        "remove": [],
        "IfFemaleAdd": [],
        "IfFemaleRemove": [],
        "IfTeenAdd": [],
        "skills": [16704],
        "IfTeenSkills": [],
        "IfChildSkills": [],
        "IfToddlerSkills": []
    },
    "my": {
        "add": [168006],
        "remove": [],
        "IfFemaleAdd": [],
        "IfFemaleRemove": [],
        "IfTeenAdd": [],
        "skills": [],
        "IfTeenSkills": [],
        "IfChildSkills": [],
        "IfToddlerSkills": []
    },
    "maid": {
        "add": [170584],
        "remove": [],
        "IfFemaleAdd": [],
        "IfFemaleRemove": [],
        "IfTeenAdd": [],
        "skills": [],
        "IfTeenSkills": [],
        "IfChildSkills": [],
        "IfToddlerSkills": []
    },
    "nanny": {
        "add": [],
        "remove": [],
        "IfFemaleAdd": [],
        "IfFemaleRemove": [],
        "IfTeenAdd": [],
        "skills": [],
        "IfTeenSkills": [],
        "IfChildSkills": [],
        "IfToddlerSkills": []
    },
    "service": {
        "add": [],
        "remove": [],
        "IfFemaleAdd": [],
        "IfFemaleRemove": [],
        "IfTeenAdd": [],
        "skills": [],
        "IfTeenSkills": [],
        "IfChildSkills": [],
        "IfToddlerSkills": []
    },
    "slave": {
        "add": [],
        "remove": [],
        "IfFemaleAdd": [],
        "IfFemaleRemove": [],
        "IfTeenAdd": [],
        "skills": [],
        "IfTeenSkills": [],
        "IfChildSkills": [],
        "IfToddlerSkills": []
    },
    "hot": {
        "add": [],
        "remove": [],
        "IfFemaleAdd": [],
        "IfFemaleRemove": [],
        "IfTeenAdd": [],
        "skills": [],
        "IfTeenSkills": [],
        "IfChildSkills": [],
        "IfToddlerSkills": []
    },
    # Add more command blocks from spreadsheet here as needed
}

for command, actions in ghostshell_trait_commands.items():
    def make_command(command, actions):
        @sims4.commands.Command(f'gs.{command}', command_type=sims4.commands.CommandType.Live)
        def command_fn(*args, _connection=None):
            output = sims4.commands.CheatOutput(_connection)
            client = services.client_manager().get(_connection)
            if not client:
                output("No client found.")
                return

            sim = client.active_sim.sim_info
            if not sim:
                output("No active sim.")
                return

            trait_manager = services.get_instance_manager(Types.TRAIT)
            skill_manager = services.get_instance_manager(Types.STATISTIC)

            # Always remove these traits
            _remove_traits(sim, output, trait_manager, actions.get("remove", []))
            if sim.is_female:
                _remove_traits(sim, output, trait_manager, actions.get("IfFemaleRemove", []))

            if sim.is_female:
                _apply_traits(sim, output, trait_manager, actions.get("IfFemaleAdd", []))
            if sim.age == 2:  # Teen
                _apply_traits(sim, output, trait_manager, actions.get("IfTeenAdd", []))
            _apply_traits(sim, output, trait_manager, actions.get("add", []))

            _apply_skills(sim, output, skill_manager, actions.get("skills", []))
            if sim.age == 2:  # Teen
                _apply_skills(sim, output, skill_manager, actions.get("IfTeenSkills", []))
            elif sim.age == 1:  # Child
                _apply_skills(sim, output, skill_manager, actions.get("IfChildSkills", []))
            elif sim.age == 0:  # Toddler
                _apply_skills(sim, output, skill_manager, actions.get("IfToddlerSkills", []))

        return command_fn

    make_command(command, actions)
