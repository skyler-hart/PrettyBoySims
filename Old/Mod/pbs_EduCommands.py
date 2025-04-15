from sims4.resources import Types, get_resource_key
from pbs_t_ids import *
from pbs_s_ids import *
import os
import services, sims4.commands


@sims4.commands.Command('pbs_artist', command_type=sims4.commands.CommandType.Live)
def pbs_artist(_connection=None):
    # Get the console output
    output = sims4.commands.CheatOutput(_connection)

    # Get the sim_info for the active sim
    sim = services.client_manager().get(_connection).active_sim.sim_info

    # Get the tuned trait instance from the tuning instance manager
    instance_manager = services.get_instance_manager(Types.TRAIT)

    # Remove or add traits from all sims
    trait_university_arthistorydegreebahonors = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_ARTHISTORYDEGREEBAHONORS, Types.TRAIT))
    if not sim.has_trait(trait_university_arthistorydegreebahonors):
        sim.add_trait(trait_university_arthistorydegreebahonors)

    trait_university_fineartdegreebahonors = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_FINEARTDEGREEBAHONORS, Types.TRAIT))
    if not sim.has_trait(trait_university_fineartdegreebahonors):
        sim.add_trait(trait_university_fineartdegreebahonors)


@sims4.commands.Command('pbs_business', command_type=sims4.commands.CommandType.Live)
def pbs_business(_connection=None):
    # Get the console output
    output = sims4.commands.CheatOutput(_connection)

    # Get the sim_info for the active sim
    sim = services.client_manager().get(_connection).active_sim.sim_info

    # Get the tuned trait instance from the tuning instance manager
    instance_manager = services.get_instance_manager(Types.TRAIT)

    # Remove or add traits from all sims
    trait_university_communicationsdegreebahonors = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_COMMUNICATIONSDEGREEBAHONORS, Types.TRAIT))
    if not sim.has_trait(trait_university_communicationsdegreebahonors):
        sim.add_trait(trait_university_communicationsdegreebahonors)

    trait_university_economicsdegreebshonors = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_ECONOMICSDEGREEBSHONORS, Types.TRAIT))
    if not sim.has_trait(trait_university_economicsdegreebshonors):
        sim.add_trait(trait_university_economicsdegreebshonors)


@sims4.commands.Command('pbs_education', command_type=sims4.commands.CommandType.Live)
def pbs_education(_connection=None):
    # Get the console output
    output = sims4.commands.CheatOutput(_connection)

    # Get the sim_info for the active sim
    sim = services.client_manager().get(_connection).active_sim.sim_info

    # Get the tuned trait instance from the tuning instance manager
    instance_manager = services.get_instance_manager(Types.TRAIT)

    # Remove or add traits from all sims
    trait_university_languageandliteraturedegreebahonors = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_LANGUAGEANDLITERATUREDEGREEBAHONORS, Types.TRAIT))
    if not sim.has_trait(trait_university_languageandliteraturedegreebahonors):
        sim.add_trait(trait_university_languageandliteraturedegreebahonors)

    trait_university_communicationsdegreebahonors = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_COMMUNICATIONSDEGREEBAHONORS, Types.TRAIT))
    if not sim.has_trait(trait_university_communicationsdegreebahonors):
        sim.add_trait(trait_university_communicationsdegreebahonors)

    trait_university_historydegreebahonors = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_HISTORYDEGREEBAHONORS, Types.TRAIT))
    if not sim.has_trait(trait_university_historydegreebahonors):
        sim.add_trait(trait_university_historydegreebahonors)

    trait_university_highereducation = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_HIGHEREDUCATION, Types.TRAIT))
    if not sim.has_trait(trait_university_highereducation):
        sim.add_trait(trait_university_highereducation)


@sims4.commands.Command('pbs_it', command_type=sims4.commands.CommandType.Live)
def pbs_it(_connection=None):
    # Get the console output
    output = sims4.commands.CheatOutput(_connection)

    # Get the sim_info for the active sim
    sim = services.client_manager().get(_connection).active_sim.sim_info

    # Get the tuned trait instance from the tuning instance manager
    instance_manager = services.get_instance_manager(Types.TRAIT)

    # Remove or add traits from all sims
    trait_university_computersciencedegreebshonors = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_COMPUTERSCIENCEDEGREEBSHONORS, Types.TRAIT))
    if not sim.has_trait(trait_university_computersciencedegreebshonors):
        sim.add_trait(trait_university_computersciencedegreebshonors)

    trait_university_economicsdegreebshonors = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_ECONOMICSDEGREEBSHONORS, Types.TRAIT))
    if not sim.has_trait(trait_university_economicsdegreebshonors):
        sim.add_trait(trait_university_economicsdegreebshonors)


@sims4.commands.Command('pbs_science', command_type=sims4.commands.CommandType.Live)
def pbs_science(_connection=None):
    # Get the console output
    output = sims4.commands.CheatOutput(_connection)

    # Get the sim_info for the active sim
    sim = services.client_manager().get(_connection).active_sim.sim_info

    # Get the tuned trait instance from the tuning instance manager
    instance_manager = services.get_instance_manager(Types.TRAIT)

    # Remove or add traits from all sims
    trait_university_biologydegreebshonors = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_BIOLOGYDEGREEBSHONORS, Types.TRAIT))
    if not sim.has_trait(trait_university_biologydegreebshonors):
        sim.add_trait(trait_university_biologydegreebshonors)

    trait_university_physicsdegreebshonors = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_PHYSICSDEGREEBSHONORS, Types.TRAIT))
    if not sim.has_trait(trait_university_physicsdegreebshonors):
        sim.add_trait(trait_university_physicsdegreebshonors)

    trait_university_psychologydegreebshonors = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_PSYCHOLOGYDEGREEBSHONORS, Types.TRAIT))
    if not sim.has_trait(trait_university_psychologydegreebshonors):
        sim.add_trait(trait_university_psychologydegreebshonors)


@sims4.commands.Command('pbs_writer', command_type=sims4.commands.CommandType.Live)
def pbs_writer(_connection=None):
    # Get the console output
    output = sims4.commands.CheatOutput(_connection)

    # Get the sim_info for the active sim
    sim = services.client_manager().get(_connection).active_sim.sim_info

    # Get the tuned trait instance from the tuning instance manager
    instance_manager = services.get_instance_manager(Types.TRAIT)

    # Remove or add traits from all sims
    trait_university_languageandliteraturedegreebahonors = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_LANGUAGEANDLITERATUREDEGREEBAHONORS, Types.TRAIT))
    if not sim.has_trait(trait_university_languageandliteraturedegreebahonors):
        sim.add_trait(trait_university_languageandliteraturedegreebahonors)


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
    if not sim.has_trait(trait_university_arthistorydegreebahonors):
        sim.add_trait(trait_university_arthistorydegreebahonors)

    trait_university_communicationsdegreebahonors = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_COMMUNICATIONSDEGREEBAHONORS, Types.TRAIT))
    if not sim.has_trait(trait_university_communicationsdegreebahonors):
        sim.add_trait(trait_university_communicationsdegreebahonors)

    trait_university_culinaryartsdegreebahonors = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_CULINARYARTSDEGREEBAHONORS, Types.TRAIT))
    if not sim.has_trait(trait_university_culinaryartsdegreebahonors):
        sim.add_trait(trait_university_culinaryartsdegreebahonors)

    trait_university_dramadegreebahonors = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_DRAMADEGREEBAHONORS, Types.TRAIT))
    if not sim.has_trait(trait_university_dramadegreebahonors):
        sim.add_trait(trait_university_dramadegreebahonors)

    trait_university_fineartdegreebahonors = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_FINEARTDEGREEBAHONORS, Types.TRAIT))
    if not sim.has_trait(trait_university_fineartdegreebahonors):
        sim.add_trait(trait_university_fineartdegreebahonors)

    trait_university_historydegreebahonors = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_HISTORYDEGREEBAHONORS, Types.TRAIT))
    if not sim.has_trait(trait_university_historydegreebahonors):
        sim.add_trait(trait_university_historydegreebahonors)

    trait_university_languageandliteraturedegreebahonors = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_LANGUAGEANDLITERATUREDEGREEBAHONORS, Types.TRAIT))
    if not sim.has_trait(trait_university_languageandliteraturedegreebahonors):
        sim.add_trait(trait_university_languageandliteraturedegreebahonors)
