from sims4.resources import Types, get_resource_key
import sims4.commands
import services

TRAIT_THEKNACK = 27328

@sims4.commands.Command('gs.service', command_type=sims4.commands.CommandType.Live)
def add_trait(_connection=None):
    # Get the console output
    output = sims4.commands.CheatOutput(_connection)

    # Get the sim_info for the active sim
    sim_info = services.client_manager().get(_connection).active_sim.sim_info

    # Get the tuned trait instance from the tuning instance manager
    instance_manager = services.get_instance_manager(Types.TRAIT)
    trait_handy = instance_manager.get(get_resource_key(TRAIT_THEKNACK, Types.TRAIT))

    # Check if our sim already has that trait
    if sim_info.has_trait(trait_handy):
        output('Sim is already handy')
    else:
        # The sim doesn't have that trait, so add it
        sim_info.add_trait(trait_handy)
        output('Sim is now handy')

@sims4.commands.Command('gs.unservice', command_type=sims4.commands.CommandType.Live)
def remove_trait(_connection=None):
    output = sims4.commands.CheatOutput(_connection)
    sim_info = services.client_manager().get(_connection).active_sim.sim_info
    instance_manager = services.get_instance_manager(Types.TRAIT)
    trait_handy = instance_manager.get(get_resource_key(TRAIT_THEKNACK, Types.TRAIT))
    if not sim_info.has_trait(trait_handy):
        output('Sim is not handy. Nothing to remove')
    else:
        sim_info.remove_trait(trait_handy)
        output('Sim is no longer handy')
