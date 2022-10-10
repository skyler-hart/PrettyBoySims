from sims4.resources import Types, get_resource_key
from pbs_t_ids import *
from pbs_s_ids import *
import os
import services, sims4.commands


@sims4.commands.Command('pbs_bahonors', command_type=sims4.commands.CommandType.Live)
def pbs_bahonors(_connection=None):
    # Get the console output
    output = sims4.commands.CheatOutput(_connection)

    # Get the sim_info for the active sim
    sim = services.client_manager().get(_connection).active_sim.sim_info

    # Get the tuned trait instance from the tuning instance manager
    instance_manager = services.get_instance_manager(Types.TRAIT)

    # Remove or add traits from all sims
    trait_university_arthistorydegreebahonors = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_ARTHISTORYDEGREEBAHONORS, Types.TRAIT))
    trait_university_communicationsdegreebahonors = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_COMMUNICATIONSDEGREEBAHONORS, Types.TRAIT))
    trait_university_physicsdegreebahonors = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_PHYSICSDEGREEBAHONORS, Types.TRAIT))

    if not sim.has_trait(trait_university_arthistorydegreebahonors):
        sim.add_trait(trait_university_arthistorydegreebahonors)

    if not sim.has_trait(trait_university_communicationsdegreebahonors):
        sim.add_trait(trait_university_communicationsdegreebahonors)

    if not sim.has_trait(trait_university_physicsdegreebahonors):
        sim.add_trait(trait_university_physicsdegreebahonors)


@sims4.commands.Command('pbs_bshonors', command_type=sims4.commands.CommandType.Live)
def pbs_bahonors(_connection=None):
    # Get the console output
    output = sims4.commands.CheatOutput(_connection)

    # Get the sim_info for the active sim
    sim = services.client_manager().get(_connection).active_sim.sim_info

    # Get the tuned trait instance from the tuning instance manager
    instance_manager = services.get_instance_manager(Types.TRAIT)

    # Remove or add traits from all sims
    trait_university_arthistorydegreebshonors = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_ARTHISTORYDEGREEBSHONORS, Types.TRAIT))
    trait_university_communicationsdegreebshonors = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_COMMUNICATIONSDEGREEBSHONORS, Types.TRAIT))
    trait_university_physicsdegreebshonors = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_PHYSICSDEGREEBSHONORS, Types.TRAIT))


    if not sim.has_trait(trait_university_arthistorydegreebshonors):
        sim.add_trait(trait_university_arthistorydegreebshonors)

    if not sim.has_trait(trait_university_communicationsdegreebshonors):
        sim.add_trait(trait_university_communicationsdegreebshonors)

    if not sim.has_trait(trait_university_physicsdegreebshonors):
        sim.add_trait(trait_university_physicsdegreebshonors)


@sims4.commands.Command('pbs_csdegree', command_type=sims4.commands.CommandType.Live)
def pbs_csdegree(_connection=None):
    # Get the console output
    output = sims4.commands.CheatOutput(_connection)

    # Get the sim_info for the active sim
    sim = services.client_manager().get(_connection).active_sim.sim_info

    # Get the tuned trait instance from the tuning instance manager
    instance_manager = services.get_instance_manager(Types.TRAIT)

    # Remove or add traits from all sims
    trait_university_degreetraits_computerscience = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_DEGREETRAITS_COMPUTERSCIENCE, Types.TRAIT))
    trait_university_degreetraits_type_honors = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_DEGREETRAITS_TYPE_HONORS, Types.TRAIT))


    if not sim.has_trait(trait_university_degreetraits_computerscience):
        sim.add_trait(trait_university_degreetraits_computerscience)

    if not sim.has_trait(trait_university_degreetraits_type_honors):
        sim.add_trait(trait_university_degreetraits_type_honors)