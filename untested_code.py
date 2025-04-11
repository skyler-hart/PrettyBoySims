def _apply_traits(sim, output, trait_manager, traits):
    for trait_id in traits:
        output(f"Resolving trait ID: {trait_id}")
        key = get_resource_key(trait_id, Types.TRAIT)
        output(f"Generated resource key for trait {trait_id}: {key}")
        trait = trait_manager.get(key)
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
        key = get_resource_key(skill_id, Types.STATISTIC)
        output(f"Generated resource key for skill {skill_id}: {key}")
        skill = skill_manager.get(key)

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
        "add": [
            GSTraits.ACTIVE.value, GSTraits.GENIUS.value, GSTraits.THEKNACK.value
        ],
        "remove": [
            GSTraits.MEAN.value, GSTraits.HOT_HEADED.value, GSTraits.EVIL.value
        ],
        "IfFemaleAdd": [
            GSTraits.WICKEDWHIMS_BODYHAIR_PUBICHAIR_ISDISABLED.value,
            GSTraits.WICKEDWHIMS_BIRTHCONTROL_IUD.value,
            GSTraits.WICKEDWHIMS_MENSTRUALCYCLE_NOBLEEDING.value
        ],
        "IfFemaleRemove": [],
        "skills": [
            GSSkills.BAKING.value, GSSkills.CHARISMA.value, GSSkills.COOKING.value,
            GSSkills.FITNESS.value, GSSkills.HANDINESS.value, GSSkills.LOGIC.value,
            GSSkills.PARENTING.value, GSSkills.PROGRAMMING.value, GSSkills.ROCKET_SCIENCE.value
        ],
        "IfTeenSkills": [GSSkills.SNOWBOARDING.value],
        "IfChildSkills": [
            GSSkills.CREATIVITY.value, GSSkills.MENTAL.value, GSSkills.MOTOR.value, GSSkills.SOCIAL.value
        ],
        "IfToddlerSkills": [
            GSSkills.COMMUNICATION.value, GSSkills.IMMAGINATION.value, GSSkills.MOVEMENT.value,
            GSSkills.POTTY.value, GSSkills.THINKING.value
        ]
    },
    "my": {
        "IfChildAdd": [],
        "IfToddlerAdd": [],
        "IfMaleAdd": [],
        "add": [
            GSTraits.ACTIVE.value, GSTraits.GENIUS.value, GSTraits.THEKNACK.value
        ],
        "remove": [
            GSTraits.MEAN.value, GSTraits.HOT_HEADED.value, GSTraits.EVIL.value
        ],
        "IfFemaleAdd": [
            GSTraits.WICKEDWHIMS_BODYHAIR_PUBICHAIR_ISDISABLED.value,
            GSTraits.WICKEDWHIMS_BIRTHCONTROL_IUD.value,
            GSTraits.WICKEDWHIMS_MENSTRUALCYCLE_NOBLEEDING.value
        ],
        "IfFemaleRemove": [],
        "skills": [
            GSSkills.BAKING.value, GSSkills.CHARISMA.value, GSSkills.COOKING.value,
            GSSkills.FITNESS.value, GSSkills.HANDINESS.value, GSSkills.LOGIC.value,
            GSSkills.PARENTING.value, GSSkills.PROGRAMMING.value, GSSkills.ROCKET_SCIENCE.value
        ],
        "IfTeenSkills": [GSSkills.SNOWBOARDING.value],
        "IfChildSkills": [
            GSSkills.CREATIVITY.value, GSSkills.MENTAL.value, GSSkills.MOTOR.value, GSSkills.SOCIAL.value
        ],
        "IfToddlerSkills": [
            GSSkills.COMMUNICATION.value, GSSkills.IMMAGINATION.value, GSSkills.MOVEMENT.value,
            GSSkills.POTTY.value, GSSkills.THINKING.value
        ]
    },
    "myplayed": {
        "IfChildAdd": [GSTraits.GENIUS.value],
        "IfToddlerAdd": [],
        "IfMaleAdd": [],
        "add": [
            GSTraits.ACTIVE.value, GSTraits.GENIUS.value, GSTraits.THEKNACK.value
        ],
        "remove": [
            GSTraits.MEAN.value, GSTraits.HOT_HEADED.value, GSTraits.EVIL.value
        ],
        "IfFemaleAdd": [
            GSTraits.WICKEDWHIMS_BODYHAIR_PUBICHAIR_ISDISABLED.value,
            GSTraits.WICKEDWHIMS_BIRTHCONTROL_IUD.value,
            GSTraits.WICKEDWHIMS_MENSTRUALCYCLE_NOBLEEDING.value
        ],
        "IfFemaleRemove": [],
        "skills": [
            GSSkills.BAKING.value, GSSkills.CHARISMA.value, GSSkills.COOKING.value,
            GSSkills.FITNESS.value, GSSkills.HANDINESS.value, GSSkills.LOGIC.value,
            GSSkills.PARENTING.value, GSSkills.PROGRAMMING.value, GSSkills.ROCKET_SCIENCE.value
        ],
        "IfTeenSkills": [GSSkills.SNOWBOARDING.value],
        "IfChildSkills": [
            GSSkills.CREATIVITY.value, GSSkills.MENTAL.value, GSSkills.MOTOR.value, GSSkills.SOCIAL.value
        ],
        "IfToddlerSkills": [
            GSSkills.COMMUNICATION.value, GSSkills.IMMAGINATION.value, GSSkills.MOVEMENT.value,
            GSSkills.POTTY.value, GSSkills.THINKING.value
        ]
    },
    "service": {
        "IfChildAdd": [],
        "IfToddlerAdd": [],
        "IfMaleAdd": [],
        "add": [
            GSTraits.ACTIVE.value, GSTraits.GENIUS.value, GSTraits.THEKNACK.value
        ],
        "remove": [
            GSTraits.MEAN.value, GSTraits.HOT_HEADED.value, GSTraits.EVIL.value
        ],
        "IfFemaleAdd": [
            GSTraits.WICKEDWHIMS_BODYHAIR_PUBICHAIR_ISDISABLED.value,
            GSTraits.WICKEDWHIMS_BIRTHCONTROL_IUD.value,
            GSTraits.WICKEDWHIMS_MENSTRUALCYCLE_NOBLEEDING.value
        ],
        "IfFemaleRemove": [],
        "skills": [
            GSSkills.BAKING.value, GSSkills.CHARISMA.value, GSSkills.COOKING.value,
            GSSkills.FITNESS.value, GSSkills.HANDINESS.value, GSSkills.LOGIC.value,
            GSSkills.PARENTING.value, GSSkills.PROGRAMMING.value, GSSkills.ROCKET_SCIENCE.value
        ],
        "IfTeenSkills": [GSSkills.SNOWBOARDING.value],
        "IfChildSkills": [
            GSSkills.CREATIVITY.value, GSSkills.MENTAL.value, GSSkills.MOTOR.value, GSSkills.SOCIAL.value
        ],
        "IfToddlerSkills": [
            GSSkills.COMMUNICATION.value, GSSkills.IMMAGINATION.value, GSSkills.MOVEMENT.value,
            GSSkills.POTTY.value, GSSkills.THINKING.value
        ]
    }
}


for command, actions in ghostshell_trait_commands.items():
    def make_command(command=command, actions=actions):
        @sims4.commands.Command(f'gs.{command}', command_type=sims4.commands.CommandType.Live)
        def command_fn(*args, _connection=None):
            client = services.client_manager().get(_connection)
            output = sims4.commands.CheatOutput(_connection)
            sim = resolve_sim(args, client)

            trait_manager = services.get_instance_manager(Types.TRAIT)
            skill_manager = services.get_instance_manager(Types.STATISTIC)

            # Remove traits
            _remove_traits(sim, output, trait_manager, actions.get("remove", []))
            if sim.is_female:
                _remove_traits(sim, output, trait_manager, actions.get("IfFemaleRemove", []))
            elif sim.is_male:
                _remove_traits(sim, output, trait_manager, actions.get("IfMaleRemove", []))

            # Apply age-specific skills and general skills
            if sim.age == GSAge.TEEN.value:
                output("Applying teen-specific skills...")
                _apply_skills(sim, output, skill_manager, actions.get("IfTeenSkills", []))
            elif sim.age == GSAge.CHILD.value:
                output("Applying child-specific skills...")
                _apply_skills(sim, output, skill_manager, actions.get("IfChildSkills", []))
            elif sim.age == GSAge.TODDLER.value:
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
            if sim.age == GSAge.TEEN.value:
                _apply_traits(sim, output, trait_manager, actions.get("IfTeenAdd", []))
            elif sim.age == GSAge.CHILD.value:
                _apply_traits(sim, output, trait_manager, actions.get("IfChildAdd", []))
            elif sim.age == GSAge.TODDLER.value:
                _apply_traits(sim, output, trait_manager, actions.get("IfToddlerAdd", []))

            # Apply general traits
            _apply_traits(sim, output, trait_manager, actions.get("add", []))

            # Auto-pay bills for the household
            if command in ["me", "my", "service"]:
                household = sim.household
                if household and hasattr(household, 'bills_manager'):
                    bills = household.bills_manager
                    if hasattr(bills, 'pay_all_bills'):
                        bills.pay_all_bills()
                        output("Auto-paid household bills.")

            # Remove school career if applicable
            if command in ["me", "my", "service"] and sim.career_tracker is not None:
                school = None
                if sim.age == GSAge.TEEN.value:
                    school = sim.career_tracker.get_career_by_uid(137624)  # High School
                elif sim.age == GSAge.CHILD.value:
                    school = sim.career_tracker.get_career_by_uid(135606)  # Grade School

                if school:
                    sim.career_tracker.remove_career(school)
                    output(f"Removed school career from {'teen' if sim.age == GSAge.TEEN.value else 'child'} sim.")

        return command_fn

    make_command(command, actions)
