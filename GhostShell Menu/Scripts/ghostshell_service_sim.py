import services
import sims4
from interactions.base.super_interaction import SuperInteraction
from interactions.interaction_finisher import FinishingType
from sims4.resources import Types, get_resource_key

class GhostShellServiceSimInteraction(SuperInteraction):
    @classmethod
    def _run_interaction_gen(cls, timeline):
        output = sims4.commands.CheatOutput()
        target = cls.target  # Sim being clicked

        # Handiness Skill
        HANDINESS_ID = 16654  # Official Handiness skill ID
        skill_manager = services.get_instance_manager(Types.STATISTIC)
        handiness = skill_manager.get(HANDINESS_ID)

        if handiness:
            tracker = target.get_tracker(handiness)
            if not tracker.has_statistic(handiness):
                tracker.add_statistic(handiness)
            tracker.set_value(handiness, float(handiness.max_level))
            output(f"🔧 {target.full_name} now has max Handiness.")
        else:
            output("❌ Handiness skill not found.")

        # Add The Knack Trait
        TRAIT_THEKNACK = 27328
        trait_manager = services.get_instance_manager(Types.TRAIT)
        the_knack = trait_manager.get(get_resource_key(TRAIT_THEKNACK, Types.TRAIT))

        if the_knack and not target.has_trait(the_knack):
            target.add_trait(the_knack)
            output(f"✨ {target.full_name} now has 'The Knack' trait.")
        elif the_knack:
            output(f"ℹ️ {target.full_name} already has 'The Knack'.")
        else:
            output("❌ 'The Knack' trait not found.")

        cls.cancel(FinishingType.NATURAL, "Service Sim complete")
        return True

print("GhostShell mod loaded.")
