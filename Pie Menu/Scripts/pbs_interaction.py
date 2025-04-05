import services, sims4
from interactions.base.super_interaction import SuperInteraction
from interactions.interaction_finisher import FinishingType
from sims4.tuning.instances import lock_instance_tunables
from sims4.tuning.tunable import Tunable

class PBS_SetActingMax(SuperInteraction):
    @classmethod
    def _run_interaction_gen(cls, timeline):
        # Get the target Sim (the one being clicked)
        sim = cls.sim
        target = cls.target

        output = sims4.commands.CheatOutput()
        output(f"🎭 Maxing Acting skill for {target.full_name}")

        # Max acting
        from sims4.resources import Types, get_resource_key
        skill_manager = services.get_instance_manager(Types.STATISTIC)
        S_ACTING = 194727
        acting_skill = skill_manager.get(S_ACTING)

        if acting_skill:
            tracker = target.get_tracker(acting_skill)
            if not tracker.has_statistic(acting_skill):
                tracker.add_statistic(acting_skill)

            tracker.set_value(acting_skill, float(acting_skill.max_level))
            output("✨ Acting skill maxed.")
        else:
            output("❌ Acting skill not found.")

        cls.cancel(FinishingType.NATURAL, 'Interaction complete')
        return True

class PBS_SetSkillsMax(SuperInteraction):
    @classmethod
    def _run_interaction_gen(cls, timeline):
        # Get the target Sim (the one being clicked)
        sim = cls.sim
        target = cls.target

        output = sims4.commands.CheatOutput()
        output(f"🎭 Maxing all skills for {target.full_name}")

        from sims4.resources import Types, get_resource_key
        skill_manager = services.get_instance_manager(Types.STATISTIC)
        all_skills = [s for s in skill_manager.types.values() if hasattr(s, 'max_level') and s.max_level > 0]

        for skill in all_skills:
            tracker = sim.get_tracker(skill)
            if not tracker.has_statistic(skill):
                tracker.add_statistic(skill)

            tracker.set_value(skill, float(skill.max_level))

        cls.cancel(FinishingType.NATURAL, 'Interaction complete')
        return True
