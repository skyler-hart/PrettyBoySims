from sims4.resources import Types, get_resource_key
from pbs_t_ids import *
from pbs_s_ids import *
import os
import services, sims4.commands


@sims4.commands.Command('pbs_maid', command_type=sims4.commands.CommandType.Live)
def pbs_maid(_connection=None):
    # Get the console output
    output = sims4.commands.CheatOutput(_connection)

    # Get the sim_info for the active sim
    sim = services.client_manager().get(_connection).active_sim.sim_info

    # Get the tuned trait instance from the tuning instance manager
    instance_manager = services.get_instance_manager(Types.TRAIT)
    t_active = instance_manager.get(get_resource_key(T_ACTIVE, Types.TRAIT))
    t_beguling = instance_manager.get(get_resource_key(T_BEGULING, Types.TRAIT))
    t_cheerful = instance_manager.get(get_resource_key(T_CHEERFUL, Types.TRAIT))
    t_clumsy = instance_manager.get(get_resource_key(T_CLUMSY, Types.TRAIT))
    t_commitmentissues = instance_manager.get(get_resource_key(T_COMMITMENTISSUES, Types.TRAIT))
    t_connections = instance_manager.get(get_resource_key(T_CONNECTIONS, Types.TRAIT))
    t_creative = instance_manager.get(get_resource_key(T_CREATIVE, Types.TRAIT))
    t_dastardly = instance_manager.get(get_resource_key(T_DASTARDLY, Types.TRAIT))
    t_dauntless = instance_manager.get(get_resource_key(T_DAUNTLESS, Types.TRAIT))
    t_entrepreneur = instance_manager.get(get_resource_key(T_ENTREPRENEUR, Types.TRAIT))
    t_entrepreneurial = instance_manager.get(get_resource_key(T_ENTREPRENEURIAL, Types.TRAIT))
    t_essenceofflavor = instance_manager.get(get_resource_key(T_ESSENCEOFFLAVOR, Types.TRAIT))
    t_evil = instance_manager.get(get_resource_key(T_EVIL, Types.TRAIT))
    t_familyoriented = instance_manager.get(get_resource_key(T_FAMILYORIENT, Types.TRAIT))
    t_familysim = instance_manager.get(get_resource_key(T_FAMILYSIM, Types.TRAIT))
    t_fastfastidious = instance_manager.get(get_resource_key(T_FASTFASTIDIOUS, Types.TRAIT))
    t_fertile = instance_manager.get(get_resource_key(T_FERTILE, Types.TRAIT))
    t_filthdweller = instance_manager.get(get_resource_key(T_FILTHDWELLER, Types.TRAIT))
    t_foreverfresh = instance_manager.get(get_resource_key(T_FOREVERFRESH, Types.TRAIT))
    t_freeservices = instance_manager.get(get_resource_key(T_FREESERVICES, Types.TRAIT))
    t_freshchef = instance_manager.get(get_resource_key(T_FRESHCHEF, Types.TRAIT))
    t_frugal = instance_manager.get(get_resource_key(T_FRUGAL, Types.TRAIT))
    t_gloomy = instance_manager.get(get_resource_key(T_GLOOMY, Types.TRAIT))
    t_glutton = instance_manager.get(get_resource_key(T_GLUTTON, Types.TRAIT))
    t_good = instance_manager.get(get_resource_key(T_GOOD, Types.TRAIT))
    t_hateschildren = instance_manager.get(get_resource_key(T_HATESCHILDREN, Types.TRAIT))
    t_heatproof = instance_manager.get(get_resource_key(T_HEATPROOF, Types.TRAIT))
    t_highmetab = instance_manager.get(get_resource_key(T_HIGHMET, Types.TRAIT))
    t_hotheaded = instance_manager.get(get_resource_key(T_HOTHEADED, Types.TRAIT))
    t_hsexit_earnedged = instance_manager.get(get_resource_key(T_HSEXIT_EARNEDGED, Types.TRAIT))
    t_iceproof = instance_manager.get(get_resource_key(T_ICEPROOF, Types.TRAIT))
    t_incrediblyfriendly = instance_manager.get(get_resource_key(T_INCREDFRIENDLY, Types.TRAIT))
    t_influential = instance_manager.get(get_resource_key(T_INFLUENTIALINDIVIDUAL, Types.TRAIT))
    t_insane = instance_manager.get(get_resource_key(T_INSANE, Types.TRAIT))
    t_intheknow = instance_manager.get(get_resource_key(T_INTHEKNOW, Types.TRAIT))
    t_invested = instance_manager.get(get_resource_key(T_INVESTED, Types.TRAIT))
    t_jealous = instance_manager.get(get_resource_key(T_JEALOUS, Types.TRAIT))
    t_kindnessambasador = instance_manager.get(get_resource_key(T_KINDNESSAMB, Types.TRAIT))
    t_klepto = instance_manager.get(get_resource_key(T_KLEPTO, Types.TRAIT))
    t_lazy = instance_manager.get(get_resource_key(T_LAZY, Types.TRAIT))
    t_longevity = instance_manager.get(get_resource_key(T_LONGEVITY, Types.TRAIT))
    t_mean = instance_manager.get(get_resource_key(T_MEAN, Types.TRAIT))
    t_mountaineer3 = instance_manager.get(get_resource_key(T_MOUNTAINEER3, Types.TRAIT))
    t_naturalspeaker = instance_manager.get(get_resource_key(T_NATURALSPEAKER, Types.TRAIT))
    t_neat = instance_manager.get(get_resource_key(T_NEAT, Types.TRAIT))
    t_outgoing = instance_manager.get(get_resource_key(T_OUTGOING, Types.TRAIT))
    t_overachiever = instance_manager.get(get_resource_key(T_OVERACHIEVER, Types.TRAIT))
    t_overachievernew = instance_manager.get(get_resource_key(T_OVERACHIEVERNEW, Types.TRAIT))
    t_paranoid = instance_manager.get(get_resource_key(T_PARANOID, Types.TRAIT))
    t_partyanimal = instance_manager.get(get_resource_key(T_PARTYANIMAL, Types.TRAIT))
    t_perfecthost = instance_manager.get(get_resource_key(T_PERFECTHOST, Types.TRAIT))
    t_perfectionist = instance_manager.get(get_resource_key(T_PERFECTIONIST, Types.TRAIT))
    t_quicklearner = instance_manager.get(get_resource_key(T_QUICKLEARNER, Types.TRAIT))
    t_recycledisciple = instance_manager.get(get_resource_key(T_RECYCLEDISCIPLE, Types.TRAIT))
    t_relatable = instance_manager.get(get_resource_key(T_RELATABLE, Types.TRAIT))
    t_rolemodel = instance_manager.get(get_resource_key(T_ROLEMODEL, Types.TRAIT))
    t_selfassured = instance_manager.get(get_resource_key(T_SELFASSURED, Types.TRAIT))
    t_shameless = instance_manager.get(get_resource_key(T_SHAMELESS, Types.TRAIT))
    t_sicknessimmunity = instance_manager.get(get_resource_key(T_SICKNESSIMMUNITY, Types.TRAIT))
    t_slob = instance_manager.get(get_resource_key(T_SLOB, Types.TRAIT))
    t_snob = instance_manager.get(get_resource_key(T_SNOB, Types.TRAIT))
    t_snowhate = instance_manager.get(get_resource_key(T_SNOWHATE, Types.TRAIT))
    t_snowlove = instance_manager.get(get_resource_key(T_SNOWLOVE, Types.TRAIT))
    t_sociallyawkward = instance_manager.get(get_resource_key(T_SOCIALLYAWKWARD, Types.TRAIT))
    t_sociallygifted = instance_manager.get(get_resource_key(T_SOCIALLYGIFTED, Types.TRAIT))
    t_speedcleaner = instance_manager.get(get_resource_key(T_SPEEDCLEANER, Types.TRAIT))
    t_speedreader = instance_manager.get(get_resource_key(T_SPEEDREADER, Types.TRAIT))
    t_squemish = instance_manager.get(get_resource_key(T_SQUEMISH, Types.TRAIT))
    t_stormchaser = instance_manager.get(get_resource_key(T_STORMCHASER, Types.TRAIT))
    t_stovesandgrillmaster = instance_manager.get(get_resource_key(T_STOVESGRILLSMASTER, Types.TRAIT))
    t_theknack = instance_manager.get(get_resource_key(T_THEKNACK, Types.TRAIT))
    t_unflirty = instance_manager.get(get_resource_key(T_UNFLIRTY, Types.TRAIT))
    t_overclock = instance_manager.get(get_resource_key(T_UNLOCKEDOVERCLOCK, Types.TRAIT))
    t_vegetarian = instance_manager.get(get_resource_key(T_VEGETARIAN, Types.TRAIT))
    t_waterproof = instance_manager.get(get_resource_key(T_WATERPROOF, Types.TRAIT))
    t_webmaster = instance_manager.get(get_resource_key(T_WEBMASTER, Types.TRAIT))

    t_customgender = instance_manager.get(get_resource_key(T_PREG_CUSTOM, Types.TRAIT))
    t_romfemale = instance_manager.get(get_resource_key(T_ROM_ATTFEMALE, Types.TRAIT))
    t_rommale = instance_manager.get(get_resource_key(T_ROM_ATTMALE, Types.TRAIT))
    t_romnotfemale = instance_manager.get(get_resource_key(T_ROM_ATTNOTFEMALE, Types.TRAIT))
    t_romnotmale = instance_manager.get(get_resource_key(T_ROM_ATTNOTMALE, Types.TRAIT))
    t_romexplore = instance_manager.get(get_resource_key(T_ROM_EXPLORING, Types.TRAIT))
    t_romnotexplore = instance_manager.get(get_resource_key(T_ROM_NOTEXPLORING, Types.TRAIT))
    t_canbeimpregnated = instance_manager.get(get_resource_key(T_PREG_CANBEIMREGNATED, Types.TRAIT))
    t_canimpgregnate = instance_manager.get(get_resource_key(T_PREG_CANIMPREGNATE, Types.TRAIT))
    t_woohoofemale = instance_manager.get(get_resource_key(T_WOOHOO_FEMALE, Types.TRAIT))
    t_woohoomale = instance_manager.get(get_resource_key(T_WOOHOO_MALE, Types.TRAIT))
    t_woohoonotfemale = instance_manager.get(get_resource_key(T_WOOHOO_NOTFEMALE, Types.TRAIT))
    t_woohoonotmale = instance_manager.get(get_resource_key(T_WOOHOO_NOTMALE, Types.TRAIT))

    t_toddler = instance_manager.get(get_resource_key(T_TODDLER, Types.TRAIT))
    t_child = instance_manager.get(get_resource_key(T_CHILD, Types.TRAIT))
    t_teen = instance_manager.get(get_resource_key(T_TEEN, Types.TRAIT))
    t_yadult = instance_manager.get(get_resource_key(T_YADULT, Types.TRAIT))
    t_adult = instance_manager.get(get_resource_key(T_ADULT, Types.TRAIT))
    t_elder = instance_manager.get(get_resource_key(T_ELDER, Types.TRAIT))

    t_female = instance_manager.get(get_resource_key(T_FEMALE, Types.TRAIT))
    t_male = instance_manager.get(get_resource_key(T_MALE, Types.TRAIT))

    t_adulterer = instance_manager.get(get_resource_key(T_WW_ADULTERER, Types.TRAIT))
    t_antisocial = instance_manager.get(get_resource_key(T_WW_ANTISOCIAL, Types.TRAIT))
    t_cuck = instance_manager.get(get_resource_key(T_WW_CUCKOLD, Types.TRAIT))
    t_cumslut = instance_manager.get(get_resource_key(T_WW_CUMSLUT, Types.TRAIT))
    t_noeyebrown = instance_manager.get(get_resource_key(T_WW_DISLIKE_EYE_BROWN, Types.TRAIT))
    t_noeyeunnatural = instance_manager.get(get_resource_key(T_WW_DISLIKE_EYE_UNNATURAL, Types.TRAIT))
    t_noblackhair = instance_manager.get(get_resource_key(T_WW_DISLIKE_HAIR_BLACK, Types.TRAIT))
    t_nobluehair = instance_manager.get(get_resource_key(T_WW_DISLIKE_HAIR_BLUE, Types.TRAIT))
    t_nogreenhair = instance_manager.get(get_resource_key(T_WW_DISLIKE_HAIR_GREEN, Types.TRAIT))
    t_nopinkhair = instance_manager.get(get_resource_key(T_WW_DISLIKE_HAIR_PINK, Types.TRAIT))
    t_nofat = instance_manager.get(get_resource_key(T_WW_DISLIKE_FAT, Types.TRAIT))
    t_nolargebreasts = instance_manager.get(get_resource_key(T_WW_DISLIKE_BREASTS, Types.TRAIT))
    t_nobigbutt = instance_manager.get(get_resource_key(T_WW_DISLIKE_BUTT, Types.TRAIT))
    t_absorbancy = instance_manager.get(get_resource_key(T_WW_EXTRAABSORB, Types.TRAIT))
    t_genlover = instance_manager.get(get_resource_key(T_WW_GENLOVER, Types.TRAIT))
    t_incest = instance_manager.get(get_resource_key(T_WW_INCEST, Types.TRAIT))
    t_likeblondes = instance_manager.get(get_resource_key(T_WW_HAIR_BLONDE, Types.TRAIT))
    t_likebrunettes = instance_manager.get(get_resource_key(T_WW_HAIR_BROWN, Types.TRAIT))
    t_likeredheads = instance_manager.get(get_resource_key(T_WW_HAIR_RED, Types.TRAIT))
    t_beardlover = instance_manager.get(get_resource_key(T_WW_LIKESBEARD, Types.TRAIT))
    t_chubbychaser = instance_manager.get(get_resource_key(T_WW_LIKESFAT, Types.TRAIT))
    t_likegirls = instance_manager.get(get_resource_key(T_WW_LIKESFEMALES, Types.TRAIT))
    t_likefreckles = instance_manager.get(get_resource_key(T_WW_LIKESFRECKLES, Types.TRAIT))
    t_likemakeup = instance_manager.get(get_resource_key(T_WW_LIKESMAKEUP, Types.TRAIT))
    t_likeboys = instance_manager.get(get_resource_key(T_WW_LIKESMALES, Types.TRAIT))
    t_likeskinny = instance_manager.get(get_resource_key(T_WW_LIKESSKINNY, Types.TRAIT))
    t_likeflatchest = instance_manager.get(get_resource_key(T_WW_LIKESSMALLBREAST, Types.TRAIT))
    t_likeflatbutt = instance_manager.get(get_resource_key(T_WW_LIKESSMALLBUTT, Types.TRAIT))
    t_poly = instance_manager.get(get_resource_key(T_WW_POLY, Types.TRAIT))
    t_postpuberty = instance_manager.get(get_resource_key(T_WW_POSTPUBERTY, Types.TRAIT))
    t_sexuallyalluring = instance_manager.get(get_resource_key(T_WW_SEXUALLYALLURING, Types.TRAIT))

    if sim.has_trait(t_toddler) or sim.has_trait(t_child):
        output = sims4.commands.CheatOutput(_connection)
        output("Skipping WW traits as sim is a minor")

    # If teen or older, set gender and sexual orientation traits
    if sim.has_trait(t_teen) or sim.has_trait(t_adult) or sim.has_trait(t_yadult) or sim.has_trait(t_elder):
        if sim.has_trait(t_female):
            sim.add_trait(t_absorbancy)
            sim.add_trait(t_cumslut)

            sim.add_trait(t_beardlover)
            sim.add_trait(t_chubbychaser)
            sim.add_trait(t_likeboys)

            if not sim.has_trait(t_customgender):
                sim.add_trait(t_customgender)

            if sim.has_trait(t_canimpgregnate):
                sim.remove_trait(t_canimpgregnate)

            if sim.has_trait(t_romnotmale):
                sim.remove_trait(t_romnotmale)

            if not sim.has_trait(t_rommale):
                sim.add_trait(t_rommale)

            if sim.has_trait(t_woohoonotfemale):
                sim.remove_trait(t_woohoonotfemale)

            if not sim.has_trait(t_woohoofemale):
                sim.add_trait(t_woohoofemale)

            if sim.has_trait(t_woohoonotmale):
                sim.remove_trait(t_woohoonotmale)

            if not sim.has_trait(t_woohoofemale):
                sim.add_trait(t_woohoomale)

        if sim.has_trait(t_male):
            sim.add_trait(t_nofat)
            sim.add_trait(t_likemakeup)
            sim.add_trait(t_likeskinny)

            if sim.has_trait(t_canbeimpregnated):
                sim.remove_trait(t_canbeimpregnated)

            if sim.has_trait(t_woohoomale):
                sim.remove_trait(t_woohoomale)

            if not sim.has_trait(t_woohoonotmale):
                sim.add_trait(t_woohoonotmale)

        if sim.has_trait(t_romnotexplore):
            sim.remove_trait(t_romnotexplore)
            sim.add_trait(t_romexplore)

        if not sim.has_trait(t_romexplore):
            sim.add_trait(t_romexplore)

        if sim.has_trait(t_romnotfemale):
            sim.remove_trait(t_romnotfemale)
            sim.add_trait(t_romfemale)

        if not sim.has_trait(t_romfemale):
            sim.add_trait(t_romfemale)

        if not sim.has_trait(t_woohoofemale):
            sim.add_trait(t_woohoofemale)

        if sim.has_trait(t_teen):
            sim.add_trait(t_postpuberty)

        sim.add_trait(t_adulterer)
        sim.add_trait(t_antisocial)
        sim.add_trait(t_cuck)
        sim.add_trait(t_genlover)
        sim.add_trait(t_incest)
        sim.add_trait(t_poly)
        sim.add_trait(t_sexuallyalluring)

        sim.add_trait(t_likegirls)

        sim.add_trait(t_noeyebrown)
        sim.add_trait(t_noeyeunnatural)
        sim.add_trait(t_noblackhair)
        sim.add_trait(t_nobluehair)
        sim.add_trait(t_nogreenhair)
        sim.add_trait(t_nopinkhair)
        sim.add_trait(t_nolargebreasts)
        sim.add_trait(t_nobigbutt)
        sim.add_trait(t_likeblondes)
        sim.add_trait(t_likebrunettes)
        sim.add_trait(t_likeredheads)
        sim.add_trait(t_likefreckles)
        sim.add_trait(t_likeflatchest)
        sim.add_trait(t_likeflatbutt)
# Things above apply to teen or older

# Any age
    if sim.has_trait(t_beguling):
        sim.remove_trait(t_beguling)

    if sim.has_trait(t_clumsy):
        sim.remove_trait(t_clumsy)

    if sim.has_trait(t_commitmentissues):
        sim.remove_trait(t_commitmentissues)

    if sim.has_trait(t_connections):
        sim.remove_trait(t_connections)

    if sim.has_trait(t_creative):
        sim.remove_trait(t_creative)

    if sim.has_trait(t_dastardly):
        sim.remove_trait(t_dastardly)

    if sim.has_trait(t_dauntless):
        sim.remove_trait(t_dauntless)

    if sim.has_trait(t_entrepreneur):
        sim.remove_trait(t_entrepreneur)

    if sim.has_trait(t_entrepreneurial):
        sim.remove_trait(t_entrepreneurial)

    if sim.has_trait(t_evil):
        sim.remove_trait(t_evil)

    if sim.has_trait(t_familyoriented):
        sim.remove_trait(t_familyoriented)

    if sim.has_trait(t_familysim):
        sim.remove_trait(t_familysim)

    if sim.has_trait(t_fertile):
        sim.remove_trait(t_fertile)

    if sim.has_trait(t_filthdweller):
        sim.remove_trait(t_filthdweller)

    if sim.has_trait(t_gloomy):
        sim.remove_trait(t_gloomy)

    if sim.has_trait(t_glutton):
        sim.remove_trait(t_glutton)

    if sim.has_trait(t_hateschildren):
        sim.remove_trait(t_hateschildren)

    if sim.has_trait(t_hotheaded):
        sim.remove_trait(t_hotheaded)

    if sim.has_trait(t_incrediblyfriendly):
        sim.remove_trait(t_incrediblyfriendly)

    if sim.has_trait(t_influential):
        sim.remove_trait(t_influential)

    if sim.has_trait(t_insane):
        sim.remove_trait(t_insane)

    if sim.has_trait(t_intheknow):
        sim.remove_trait(t_intheknow)

    if sim.has_trait(t_jealous):
        sim.remove_trait(t_jealous)

    if sim.has_trait(t_kindnessambasador):
        sim.remove_trait(t_kindnessambasador)

    if sim.has_trait(t_klepto):
        sim.remove_trait(t_klepto)

    if sim.has_trait(t_lazy):
        sim.remove_trait(t_lazy)

    if sim.has_trait(t_mean):
        sim.remove_trait(t_mean)

    if sim.has_trait(t_naturalspeaker):
        sim.remove_trait(t_naturalspeaker)

    if sim.has_trait(t_outgoing):
        sim.remove_trait(t_outgoing)

    if sim.has_trait(t_overachiever):
        sim.remove_trait(t_overachiever)

    if sim.has_trait(t_overachievernew):
        sim.remove_trait(t_overachievernew)

    if sim.has_trait(t_paranoid):
        sim.remove_trait(t_paranoid)

    if sim.has_trait(t_partyanimal):
        sim.remove_trait(t_partyanimal)

    if sim.has_trait(t_perfecthost):
        sim.remove_trait(t_perfecthost)

    if sim.has_trait(t_quicklearner):
        sim.remove_trait(t_quicklearner)

    if sim.has_trait(t_relatable):
        sim.remove_trait(t_relatable)

    if sim.has_trait(t_rolemodel):
        sim.remove_trait(t_rolemodel)

    if sim.has_trait(t_slob):
        sim.remove_trait(t_slob)

    if sim.has_trait(t_snob):
        sim.remove_trait(t_snob)

    if sim.has_trait(t_snowhate):
        sim.remove_trait(t_snowhate)

    if sim.has_trait(t_sociallygifted):
        sim.remove_trait(t_sociallygifted)

    if sim.has_trait(t_squemish):
        sim.remove_trait(t_squemish)

    if sim.has_trait(t_unflirty):
        sim.remove_trait(t_unflirty)

    if sim.has_trait(t_vegetarian):
        sim.remove_trait(t_vegetarian)

    if not sim.has_trait(t_active):
        sim.add_trait(t_active)

    if not sim.has_trait(t_cheerful):
        sim.add_trait(t_cheerful)

    if not sim.has_trait(t_essenceofflavor):
        sim.add_trait(t_essenceofflavor)

    if not sim.has_trait(t_fastfastidious):
        sim.add_trait(t_fastfastidious)

    if not sim.has_trait(t_foreverfresh):
        sim.add_trait(t_foreverfresh)

    if not sim.has_trait(t_freeservices):
        sim.add_trait(t_freeservices)

    if not sim.has_trait(t_freshchef):
        sim.add_trait(t_freshchef)

    if not sim.has_trait(t_frugal):
        sim.add_trait(t_frugal)

    if not sim.has_trait(t_good):
        sim.add_trait(t_good)

    if not sim.has_trait(t_heatproof):
        sim.add_trait(t_heatproof)

    if not sim.has_trait(t_highmetab):
        sim.add_trait(t_highmetab)

    if not sim.has_trait(t_hsexit_earnedged):
        sim.add_trait(t_hsexit_earnedged)

    if not sim.has_trait(t_iceproof):
        sim.add_trait(t_iceproof)

    if not sim.has_trait(t_invested):
        sim.add_trait(t_invested)

    if not sim.has_trait(t_longevity):
        sim.add_trait(t_longevity)

    if not sim.has_trait(t_mountaineer3):
        sim.add_trait(t_mountaineer3)

    if not sim.has_trait(t_neat):
        sim.add_trait(t_neat)

    if not sim.has_trait(t_perfectionist):
        sim.add_trait(t_perfectionist)

    if not sim.has_trait(t_recycledisciple):
        sim.add_trait(t_recycledisciple)

    if not sim.has_trait(t_selfassured):
        sim.add_trait(t_selfassured)

    if not sim.has_trait(t_shameless):
        sim.add_trait(t_shameless)

    if not sim.has_trait(t_sicknessimmunity):
        sim.add_trait(t_sicknessimmunity)

    if not sim.has_trait(t_snowlove):
        sim.add_trait(t_snowlove)

    if not sim.has_trait(t_sociallyawkward):
        sim.add_trait(t_sociallyawkward)

    if not sim.has_trait(t_speedcleaner):
        sim.add_trait(t_speedcleaner)

    if not sim.has_trait(t_speedreader):
        sim.add_trait(t_speedreader)

    if not sim.has_trait(t_stormchaser):
        sim.add_trait(t_stormchaser)

    if not sim.has_trait(t_stovesandgrillmaster):
        sim.add_trait(t_stovesandgrillmaster)

    if not sim.has_trait(t_theknack):
        sim.add_trait(t_theknack)

    if not sim.has_trait(t_overclock):
        sim.add_trait(t_overclock)

    if not sim.has_trait(t_waterproof):
        sim.add_trait(t_waterproof)

    if not sim.has_trait(t_webmaster):
        sim.add_trait(t_webmaster)


@sims4.commands.Command('pbs_mysim', command_type=sims4.commands.CommandType.Live)
def pbs_mysim(_connection=None):
    # Get the console output
    output = sims4.commands.CheatOutput(_connection)

    # Get the sim_info for the active sim
    sim = services.client_manager().get(_connection).active_sim.sim_info

    # Get the tuned trait instance from the tuning instance manager
    instance_manager = services.get_instance_manager(Types.TRAIT)
    t_active = instance_manager.get(get_resource_key(T_ACTIVE, Types.TRAIT))
    t_adventurous = instance_manager.get(get_resource_key(T_ADVENTUROUS, Types.TRAIT))
    t_alluring = instance_manager.get(get_resource_key(T_ALLURING, Types.TRAIT))
    t_alwayswelcome = instance_manager.get(get_resource_key(T_ALWAYSWELCOME, Types.TRAIT))
    t_ambitious = instance_manager.get(get_resource_key(T_AMBITIOUS, Types.TRAIT))
    t_angler = instance_manager.get(get_resource_key(T_ANGLER, Types.TRAIT))
    t_animalattraction = instance_manager.get(get_resource_key(T_ANIMALATTRACT, Types.TRAIT))
    t_animalenthusiast = instance_manager.get(get_resource_key(T_ANIMALENTHUSIAST, Types.TRAIT))
    t_animalwhisperer = instance_manager.get(get_resource_key(T_ANIMALWHISPERER, Types.TRAIT))
    t_antiseptic = instance_manager.get(get_resource_key(T_ANTISEPTIC, Types.TRAIT))
    t_appraiser = instance_manager.get(get_resource_key(T_APPRAISER, Types.TRAIT))
    t_artlover = instance_manager.get(get_resource_key(T_ARTLOVER, Types.TRAIT))
    t_beguling = instance_manager.get(get_resource_key(T_BEGULING, Types.TRAIT))
    t_bookworm = instance_manager.get(get_resource_key(T_BOOKWORM, Types.TRAIT))
    t_brave = instance_manager.get(get_resource_key(T_BRAVE, Types.TRAIT))
    t_bro = instance_manager.get(get_resource_key(T_BRO, Types.TRAIT))
    t_businesssavvy = instance_manager.get(get_resource_key(T_BUSINESSSAVVY, Types.TRAIT))
    t_careerminded = instance_manager.get(get_resource_key(T_CAREERMINDED, Types.TRAIT))
    t_carefree = instance_manager.get(get_resource_key(T_CAREFREE, Types.TRAIT))
    t_catlover = instance_manager.get(get_resource_key(T_CATLOVER, Types.TRAIT))
    t_champofpeople = instance_manager.get(get_resource_key(T_CHAMPOFPEOPLE, Types.TRAIT))
    t_crooner = instance_manager.get(get_resource_key(T_CHARISMATICCROONER, Types.TRAIT))
    t_cheerful = instance_manager.get(get_resource_key(T_CHEERFUL, Types.TRAIT))
    t_childish = instance_manager.get(get_resource_key(T_CHILDISH, Types.TRAIT))
    t_childofocean = instance_manager.get(get_resource_key(T_CHILDOFOCEAN, Types.TRAIT))
    t_chopsticks = instance_manager.get(get_resource_key(T_CHOPSTICKS, Types.TRAIT))
    t_chronicler = instance_manager.get(get_resource_key(T_CHRONICLER, Types.TRAIT))
    t_clumsy = instance_manager.get(get_resource_key(T_CLUMSY, Types.TRAIT))
    t_collector = instance_manager.get(get_resource_key(T_COLLECTOR, Types.TRAIT))
    t_commitmentissues = instance_manager.get(get_resource_key(T_COMMITMENTISSUES, Types.TRAIT))
    t_connections = instance_manager.get(get_resource_key(T_CONNECTIONS, Types.TRAIT))
    t_creative = instance_manager.get(get_resource_key(T_CREATIVE, Types.TRAIT))
    t_creativelygifted = instance_manager.get(get_resource_key(T_CREATIVELYGIFTED, Types.TRAIT))
    t_creativevisionary = instance_manager.get(get_resource_key(T_CREATIVEVISIONARY, Types.TRAIT))
    t_dancemachine = instance_manager.get(get_resource_key(T_DANCEMACHINE, Types.TRAIT))
    t_dastardly = instance_manager.get(get_resource_key(T_DASTARDLY, Types.TRAIT))
    t_dauntless = instance_manager.get(get_resource_key(T_DAUNTLESS, Types.TRAIT))
    t_doglover = instance_manager.get(get_resource_key(T_DOGLOVER, Types.TRAIT))
    t_ecoengineer = instance_manager.get(get_resource_key(T_ECOENGINEER, Types.TRAIT))
    t_ecomaster = instance_manager.get(get_resource_key(T_ECOMASTER, Types.TRAIT))
    t_entrepreneur = instance_manager.get(get_resource_key(T_ENTREPRENEUR, Types.TRAIT))
    t_entrepreneurial = instance_manager.get(get_resource_key(T_ENTREPRENEURIAL, Types.TRAIT))
    t_epicpoet = instance_manager.get(get_resource_key(T_EPICPOET, Types.TRAIT))
    t_essenceofflavor = instance_manager.get(get_resource_key(T_ESSENCEOFFLAVOR, Types.TRAIT))
    t_eternalbond = instance_manager.get(get_resource_key(T_ETERNALBOND, Types.TRAIT))
    t_evil = instance_manager.get(get_resource_key(T_EVIL, Types.TRAIT))
    t_expressionistic = instance_manager.get(get_resource_key(T_EXPRESSIONISTIC, Types.TRAIT))
    t_fakegenius = instance_manager.get(get_resource_key(T_FAKEGENIUS, Types.TRAIT))
    t_familyoriented = instance_manager.get(get_resource_key(T_FAMILYORIENT, Types.TRAIT))
    t_familysim = instance_manager.get(get_resource_key(T_FAMILYSIM, Types.TRAIT))
    t_fastfastidious = instance_manager.get(get_resource_key(T_FASTFASTIDIOUS, Types.TRAIT))
    t_fertile = instance_manager.get(get_resource_key(T_FERTILE, Types.TRAIT))
    t_filthdweller = instance_manager.get(get_resource_key(T_FILTHDWELLER, Types.TRAIT))
    t_fizzyhead = instance_manager.get(get_resource_key(T_FIZZYHEAD, Types.TRAIT))
    t_foodie = instance_manager.get(get_resource_key(T_FOODIE, Types.TRAIT))
    t_foreverfresh = instance_manager.get(get_resource_key(T_FOREVERFRESH, Types.TRAIT))
    t_foreverfull = instance_manager.get(get_resource_key(T_FOREVERFULL, Types.TRAIT))
    t_freegan = instance_manager.get(get_resource_key(T_FREEGAN, Types.TRAIT))
    t_freeservices = instance_manager.get(get_resource_key(T_FREESERVICES, Types.TRAIT))
    t_freshchef = instance_manager.get(get_resource_key(T_FRESHCHEF, Types.TRAIT))
    t_friendofsea = instance_manager.get(get_resource_key(T_FRIENDOFSEA, Types.TRAIT))
    t_frugal = instance_manager.get(get_resource_key(T_FRUGAL, Types.TRAIT))
    t_geek = instance_manager.get(get_resource_key(T_GEEK, Types.TRAIT))
    t_genius = instance_manager.get(get_resource_key(T_GENIUS, Types.TRAIT))
    t_gloomy = instance_manager.get(get_resource_key(T_GLOOMY, Types.TRAIT))
    t_glutton = instance_manager.get(get_resource_key(T_GLUTTON, Types.TRAIT))
    t_good = instance_manager.get(get_resource_key(T_GOOD, Types.TRAIT))
    t_goofball = instance_manager.get(get_resource_key(T_GOOFBALL, Types.TRAIT))
    t_goodstories = instance_manager.get(get_resource_key(T_GOODSTRORIES, Types.TRAIT))
    t_gschoola = instance_manager.get(get_resource_key(T_GSCHOOLA, Types.TRAIT))
    t_gschoolb = instance_manager.get(get_resource_key(T_GSCHOOLB, Types.TRAIT))
    t_gschoolc = instance_manager.get(get_resource_key(T_GSCHOOLC, Types.TRAIT))
    t_gschoold = instance_manager.get(get_resource_key(T_GSCHOOLD, Types.TRAIT))
    t_gschoolf = instance_manager.get(get_resource_key(T_GSCHOOLF, Types.TRAIT))
    t_greatkisser = instance_manager.get(get_resource_key(T_GREATKISSER, Types.TRAIT))
    t_greenfiend = instance_manager.get(get_resource_key(T_GREENFIEND, Types.TRAIT))
    t_gregarious = instance_manager.get(get_resource_key(T_GREGARIOUS, Types.TRAIT))
    t_gymrat = instance_manager.get(get_resource_key(T_GYMRAT, Types.TRAIT))
    t_happytoddler = instance_manager.get(get_resource_key(T_HAPPYTODDLER, Types.TRAIT))
    t_hardlyhungry = instance_manager.get(get_resource_key(T_HARDLYHUNGRY, Types.TRAIT))
    t_hateschildren = instance_manager.get(get_resource_key(T_HATESCHILDREN, Types.TRAIT))
    t_heatproof = instance_manager.get(get_resource_key(T_HEATPROOF, Types.TRAIT))
    t_heroicpresence = instance_manager.get(get_resource_key(T_HEROICPRESENCE, Types.TRAIT))
    t_heroofstrange = instance_manager.get(get_resource_key(T_HEROOFSTRANGE, Types.TRAIT))
    t_highereducation = instance_manager.get(get_resource_key(T_HIGHEREDUCATION, Types.TRAIT))
    t_highflier = instance_manager.get(get_resource_key(T_HIGHFLIER, Types.TRAIT))
    t_highmaintenance = instance_manager.get(get_resource_key(T_HIGHMAINT, Types.TRAIT))
    t_highmetab = instance_manager.get(get_resource_key(T_HIGHMET, Types.TRAIT))
    t_hilarious = instance_manager.get(get_resource_key(T_HILARIOUS, Types.TRAIT))
    t_hometurf = instance_manager.get(get_resource_key(T_HOMETURF, Types.TRAIT))
    t_hotheaded = instance_manager.get(get_resource_key(T_HOTHEADED, Types.TRAIT))
    t_hschoola = instance_manager.get(get_resource_key(T_HSCHOOLA, Types.TRAIT))
    t_hschoolb = instance_manager.get(get_resource_key(T_HSCHOOLB, Types.TRAIT))
    t_hschoolc = instance_manager.get(get_resource_key(T_HSCHOOLC, Types.TRAIT))
    t_hschoold = instance_manager.get(get_resource_key(T_HSCHOOLD, Types.TRAIT))
    t_hschoolf = instance_manager.get(get_resource_key(T_HSCHOOLF, Types.TRAIT))
    t_hsexit_dropout = instance_manager.get(get_resource_key(T_HSEXIT_DROPOUT, Types.TRAIT))
    t_hsexit_earnedged = instance_manager.get(get_resource_key(T_HSEXIT_EARNEDGED, Types.TRAIT))
    t_hsexit_expel = instance_manager.get(get_resource_key(T_HSEXIT_EXPEL, Types.TRAIT))
    t_hsexit_early = instance_manager.get(get_resource_key(T_HSEXIT_EARLY, Types.TRAIT))
    t_hsexit_honors = instance_manager.get(get_resource_key(T_HSEXIT_HONORS, Types.TRAIT))
    t_hsexit_valedictorian = instance_manager.get(get_resource_key(T_HSEXIT_VALEDICT, Types.TRAIT))
    t_hsteamrewardcheer = instance_manager.get(get_resource_key(T_HSTEAMCHEERREWARD, Types.TRAIT))
    t_hsteamrewardchess = instance_manager.get(get_resource_key(T_HSTEAMCHESSREWARD, Types.TRAIT))
    t_hsteamrewardcomp = instance_manager.get(get_resource_key(T_HSTEAMCOMPREWARD, Types.TRAIT))
    t_hsteamrewardfootb = instance_manager.get(get_resource_key(T_HSTEAMFOOTBALLREWARD, Types.TRAIT))
    t_iceproof = instance_manager.get(get_resource_key(T_ICEPROOF, Types.TRAIT))
    t_iconic = instance_manager.get(get_resource_key(T_ICONIC, Types.TRAIT))
    t_incrediblyfriendly = instance_manager.get(get_resource_key(T_INCREDFRIENDLY, Types.TRAIT))
    t_independent = instance_manager.get(get_resource_key(T_INDEPENDENT, Types.TRAIT))
    t_influential = instance_manager.get(get_resource_key(T_INFLUENTIALINDIVIDUAL, Types.TRAIT))
    t_insane = instance_manager.get(get_resource_key(T_INSANE, Types.TRAIT))
    t_insider = instance_manager.get(get_resource_key(T_INSIDER, Types.TRAIT))
    t_inspiredexplorer = instance_manager.get(get_resource_key(T_INSPIREDEXPLORER, Types.TRAIT))
    t_intheknow = instance_manager.get(get_resource_key(T_INTHEKNOW, Types.TRAIT))
    t_invested = instance_manager.get(get_resource_key(T_INVESTED, Types.TRAIT))
    t_jealous = instance_manager.get(get_resource_key(T_JEALOUS, Types.TRAIT))
    t_kindnessambasador = instance_manager.get(get_resource_key(T_KINDNESSAMB, Types.TRAIT))
    t_klepto = instance_manager.get(get_resource_key(T_KLEPTO, Types.TRAIT))
    t_lactoseintol = instance_manager.get(get_resource_key(T_LACTOSEINTOLERANT, Types.TRAIT))
    t_lazy = instance_manager.get(get_resource_key(T_LAZY, Types.TRAIT))
    t_legendary = instance_manager.get(get_resource_key(T_LEGENDARY, Types.TRAIT))
    t_legendarystamina = instance_manager.get(get_resource_key(T_LEGENDARYSTAMINA, Types.TRAIT))
    t_livingvicariously = instance_manager.get(get_resource_key(T_LIVINGVICARIOUS, Types.TRAIT))
    t_loner = instance_manager.get(get_resource_key(T_LONER, Types.TRAIT))
    t_longevity = instance_manager.get(get_resource_key(T_LONGEVITY, Types.TRAIT))
    t_lovesoutdoors = instance_manager.get(get_resource_key(T_LOVESOUTDOORS, Types.TRAIT))
    t_lskill_argumentative = instance_manager.get(get_resource_key(T_LSKILL_ARGUMENTATIVE, Types.TRAIT))
    t_lskill_badmanners = instance_manager.get(get_resource_key(T_LSKILL_BADMANNERS, Types.TRAIT))
    t_lskill_compassionate = instance_manager.get(get_resource_key(T_LSKILL_COMPASSIONATE, Types.TRAIT))
    t_lskill_emotionalcontrol = instance_manager.get(get_resource_key(T_LSKILL_EMOTIONALCONTROL, Types.TRAIT))
    t_lskill_goodmanners = instance_manager.get(get_resource_key(T_LSKILL_GOODMANNERS, Types.TRAIT))
    t_lskill_irresponsible = instance_manager.get(get_resource_key(T_LSKILL_IRRESPONSIBLE, Types.TRAIT))
    t_lskill_mediator = instance_manager.get(get_resource_key(T_LSKILL_MEDIATOR, Types.TRAIT))
    t_lskill_responsible = instance_manager.get(get_resource_key(T_LSKILL_RESPONSIBLE, Types.TRAIT))
    t_lskill_uncontrolledemotion = instance_manager.get(get_resource_key(T_LSKILL_UNCONTROLEMOTION, Types.TRAIT))
    t_lskill_unfeeling = instance_manager.get(get_resource_key(T_LSKILL_UNFEELING, Types.TRAIT))
    t_maker = instance_manager.get(get_resource_key(T_MAKER, Types.TRAIT))
    t_marketable = instance_manager.get(get_resource_key(T_MARKETABLE, Types.TRAIT))
    t_mastermaker = instance_manager.get(get_resource_key(T_MASTERMAKER, Types.TRAIT))
    t_mastermind = instance_manager.get(get_resource_key(T_MASTERMIND, Types.TRAIT))
    t_mastermixer = instance_manager.get(get_resource_key(T_MASTERMIXER, Types.TRAIT))
    t_materialistic = instance_manager.get(get_resource_key(T_MATERIALISTIC, Types.TRAIT))
    t_mean = instance_manager.get(get_resource_key(T_MEAN, Types.TRAIT))
    t_meltmaster = instance_manager.get(get_resource_key(T_MELTMASTER, Types.TRAIT))
    t_memorable = instance_manager.get(get_resource_key(T_MEMORABLE, Types.TRAIT))
    t_mentallygifted = instance_manager.get(get_resource_key(T_MENTALLYGIFTED, Types.TRAIT))
    t_mentor = instance_manager.get(get_resource_key(T_MENTOR, Types.TRAIT))
    t_morningperson = instance_manager.get(get_resource_key(T_MORNINGPERSON, Types.TRAIT))
    t_mountaineer3 = instance_manager.get(get_resource_key(T_MOUNTAINEER3, Types.TRAIT))
    t_muser = instance_manager.get(get_resource_key(T_MUSER, Types.TRAIT))
    t_museumpatron = instance_manager.get(get_resource_key(T_MUSEUMPATRON, Types.TRAIT))
    t_musiclover = instance_manager.get(get_resource_key(T_MUSICLOVER, Types.TRAIT))
    t_naturalspeaker = instance_manager.get(get_resource_key(T_NATURALSPEAKER, Types.TRAIT))
    t_neat = instance_manager.get(get_resource_key(T_NEAT, Types.TRAIT))
    t_needsnoone = instance_manager.get(get_resource_key(T_NEEDSNOONE, Types.TRAIT))
    t_neverweary = instance_manager.get(get_resource_key(T_NEVERWEARY, Types.TRAIT))
    t_nightowl = instance_manager.get(get_resource_key(T_NIGHTOWL, Types.TRAIT))
    t_observant = instance_manager.get(get_resource_key(T_OBSERVANT, Types.TRAIT))
    t_onewithnature = instance_manager.get(get_resource_key(T_ONEWITHNATURE, Types.TRAIT))
    t_outgoing = instance_manager.get(get_resource_key(T_OUTGOING, Types.TRAIT))
    t_overachiever = instance_manager.get(get_resource_key(T_OVERACHIEVER, Types.TRAIT))
    t_overachievernew = instance_manager.get(get_resource_key(T_OVERACHIEVERNEW, Types.TRAIT))
    t_pamatriarch = instance_manager.get(get_resource_key(T_PAMATRIARCH, Types.TRAIT))
    t_paranoid = instance_manager.get(get_resource_key(T_PARANOID, Types.TRAIT))
    t_paranormallicense = instance_manager.get(get_resource_key(T_PARANORMLICENSE, Types.TRAIT))
    t_partyanimal = instance_manager.get(get_resource_key(T_PARTYANIMAL, Types.TRAIT))
    t_perfecthost = instance_manager.get(get_resource_key(T_PERFECTHOST, Types.TRAIT))
    t_perfectionist = instance_manager.get(get_resource_key(T_PERFECTIONIST, Types.TRAIT))
    t_physicallygifted = instance_manager.get(get_resource_key(T_PHYSICALLYGIFTED, Types.TRAIT))
    t_piper = instance_manager.get(get_resource_key(T_PIPER, Types.TRAIT))
    t_player = instance_manager.get(get_resource_key(T_PLAYER, Types.TRAIT))
    t_potionmaster = instance_manager.get(get_resource_key(T_POTIONMASTER, Types.TRAIT))
    t_prankster = instance_manager.get(get_resource_key(T_PRANKSTER, Types.TRAIT))
    t_preparedvoyager = instance_manager.get(get_resource_key(T_PREPAREDVOYAGER, Types.TRAIT))
    t_professionalslacker = instance_manager.get(get_resource_key(T_PROFSLACKER, Types.TRAIT))
    t_proper = instance_manager.get(get_resource_key(T_PROPER, Types.TRAIT))
    t_quicklearner = instance_manager.get(get_resource_key(T_QUICKLEARNER, Types.TRAIT))
    t_recycledisciple = instance_manager.get(get_resource_key(T_RECYCLEDISCIPLE, Types.TRAIT))
    t_regainedhumanity = instance_manager.get(get_resource_key(T_REGAINEDHUMANITY, Types.TRAIT))
    t_relatable = instance_manager.get(get_resource_key(T_RELATABLE, Types.TRAIT))
    t_reprankpristine = instance_manager.get(get_resource_key(T_REPRANK7PRISTINE, Types.TRAIT))
    t_rolemodel = instance_manager.get(get_resource_key(T_ROLEMODEL, Types.TRAIT))
    t_romantic = instance_manager.get(get_resource_key(T_ROMANTIC, Types.TRAIT))
    t_sacredknitknowledge = instance_manager.get(get_resource_key(T_SACREDKNITKNOWLEDGE, Types.TRAIT))
    t_savant = instance_manager.get(get_resource_key(T_SAVANT, Types.TRAIT))
    t_scoutingaptitude = instance_manager.get(get_resource_key(T_SCOUTINGAPTITUDE, Types.TRAIT))
    t_seasonedgamer = instance_manager.get(get_resource_key(T_SEASONEDGAMER, Types.TRAIT))
    t_seldomsleepy = instance_manager.get(get_resource_key(T_SELDOMSLEEPY, Types.TRAIT))
    t_selfabsorbed = instance_manager.get(get_resource_key(T_SELFABSORBED, Types.TRAIT))
    t_selfassured = instance_manager.get(get_resource_key(T_SELFASSURED, Types.TRAIT))
    t_shameless = instance_manager.get(get_resource_key(T_SHAMELESS, Types.TRAIT))
    t_sicknessimmunity = instance_manager.get(get_resource_key(T_SICKNESSIMMUNITY, Types.TRAIT))
    t_sincere = instance_manager.get(get_resource_key(T_SINCERE, Types.TRAIT))
    t_slingerofspells = instance_manager.get(get_resource_key(T_SLINGEROFSPELLS, Types.TRAIT))
    t_slob = instance_manager.get(get_resource_key(T_SLOB, Types.TRAIT))
    t_snob = instance_manager.get(get_resource_key(T_SNOB, Types.TRAIT))
    t_snowhate = instance_manager.get(get_resource_key(T_SNOWHATE, Types.TRAIT))
    t_snowlove = instance_manager.get(get_resource_key(T_SNOWLOVE, Types.TRAIT))
    t_sociallyawkward = instance_manager.get(get_resource_key(T_SOCIALLYAWKWARD, Types.TRAIT))
    t_sociallygifted = instance_manager.get(get_resource_key(T_SOCIALLYGIFTED, Types.TRAIT))
    t_speedcleaner = instance_manager.get(get_resource_key(T_SPEEDCLEANER, Types.TRAIT))
    t_speedreader = instance_manager.get(get_resource_key(T_SPEEDREADER, Types.TRAIT))
    t_spicehound = instance_manager.get(get_resource_key(T_SPICEHOUND, Types.TRAIT))
    t_squemish = instance_manager.get(get_resource_key(T_SQUEMISH, Types.TRAIT))
    t_steelbladder = instance_manager.get(get_resource_key(T_STEELBLADDER, Types.TRAIT))
    t_stormchaser = instance_manager.get(get_resource_key(T_STORMCHASER, Types.TRAIT))
    t_stovesandgrillmaster = instance_manager.get(get_resource_key(T_STOVESGRILLSMASTER, Types.TRAIT))
    t_supergreenthumb = instance_manager.get(get_resource_key(T_SUPERGREENTHUMB, Types.TRAIT))
    t_supremeauthority = instance_manager.get(get_resource_key(T_SUPREMEAUTHORITY, Types.TRAIT))
    t_survivalinstinct = instance_manager.get(get_resource_key(T_SURVIVALINSTINCT, Types.TRAIT))
    t_survivalist = instance_manager.get(get_resource_key(T_SURVIVALIST, Types.TRAIT))
    t_theknack = instance_manager.get(get_resource_key(T_THEKNACK, Types.TRAIT))
    t_theknowledge = instance_manager.get(get_resource_key(T_THEKNOWLEDGE, Types.TRAIT))
    t_themaster = instance_manager.get(get_resource_key(T_THEMASTER, Types.TRAIT))
    t_toddler_angelic = instance_manager.get(get_resource_key(T_TODDLER_ANGELIC, Types.TRAIT))
    t_toddler_charmer = instance_manager.get(get_resource_key(T_TODDLER_CHARMER, Types.TRAIT))
    t_toddler_clingy = instance_manager.get(get_resource_key(T_TODDLER_CLINGY, Types.TRAIT))
    t_toddler_fussy = instance_manager.get(get_resource_key(T_TODDLER_FUSSY, Types.TRAIT))
    t_toddler_independent = instance_manager.get(get_resource_key(T_TODDLER_INDEPENDENT, Types.TRAIT))
    t_toddler_inquisitive = instance_manager.get(get_resource_key(T_TODDLER_INQUISITIVE, Types.TRAIT))
    t_toddler_silly = instance_manager.get(get_resource_key(T_TODDLER_SILLY, Types.TRAIT))
    t_toddler_wild = instance_manager.get(get_resource_key(T_TODDLER_WILD, Types.TRAIT))
    t_toddler_topnotch = instance_manager.get(get_resource_key(T_TODDLER_TOPNOTCH, Types.TRAIT))
    t_treasurehunter = instance_manager.get(get_resource_key(T_TREASUREHUNTER, Types.TRAIT))
    t_treasurehunterbg = instance_manager.get(get_resource_key(T_TREASUREHUNTERBG, Types.TRAIT))
    t_truemaster = instance_manager.get(get_resource_key(T_TRUEMASTER, Types.TRAIT))
    t_unflirty = instance_manager.get(get_resource_key(T_UNFLIRTY, Types.TRAIT))
    t_overclock = instance_manager.get(get_resource_key(T_UNLOCKEDOVERCLOCK, Types.TRAIT))
    t_unstoppablefame = instance_manager.get(get_resource_key(T_UNSTOPFAME, Types.TRAIT))
    t_untroubled = instance_manager.get(get_resource_key(T_UNTROUBLED, Types.TRAIT))
    t_valuedcustomer = instance_manager.get(get_resource_key(T_VALUEDCUSTOMER, Types.TRAIT))
    t_vegetarian = instance_manager.get(get_resource_key(T_VEGETARIAN, Types.TRAIT))
    t_waterproof = instance_manager.get(get_resource_key(T_WATERPROOF, Types.TRAIT))
    t_webmaster = instance_manager.get(get_resource_key(T_WEBMASTER, Types.TRAIT))
    t_worldlyknowledge = instance_manager.get(get_resource_key(T_WORDLYKNOWLEDGE, Types.TRAIT))
    t_renownedactor = instance_manager.get(get_resource_key(T_WORLDRENOWNEDACTOR, Types.TRAIT))
    t_calmingaura = instance_manager.get(get_resource_key(T_WELLNESS_CALMINGAURA, Types.TRAIT))
    t_clearperspective = instance_manager.get(get_resource_key(T_WELLNESS_CLEARPERSPEC, Types.TRAIT))
    t_momentofclarity = instance_manager.get(get_resource_key(T_WELLNESS_MOMENTOFCLARITY, Types.TRAIT))
    t_selfcareexpert = instance_manager.get(get_resource_key(T_WELLNESS_SELFCAREEXPERTISE, Types.TRAIT))
    t_spamember = instance_manager.get(get_resource_key(T_WELLNESS_SPAMEMBER, Types.TRAIT))

    t_customgender = instance_manager.get(get_resource_key(T_PREG_CUSTOM, Types.TRAIT))
    t_romfemale = instance_manager.get(get_resource_key(T_ROM_ATTFEMALE, Types.TRAIT))
    t_rommale = instance_manager.get(get_resource_key(T_ROM_ATTMALE, Types.TRAIT))
    t_romnotfemale = instance_manager.get(get_resource_key(T_ROM_ATTNOTFEMALE, Types.TRAIT))
    t_romnotmale = instance_manager.get(get_resource_key(T_ROM_ATTNOTMALE, Types.TRAIT))
    t_romexplore = instance_manager.get(get_resource_key(T_ROM_EXPLORING, Types.TRAIT))
    t_romnotexplore = instance_manager.get(get_resource_key(T_ROM_NOTEXPLORING, Types.TRAIT))
    t_canbeimpregnated = instance_manager.get(get_resource_key(T_PREG_CANBEIMREGNATED, Types.TRAIT))
    t_canimpgregnate = instance_manager.get(get_resource_key(T_PREG_CANIMPREGNATE, Types.TRAIT))
    t_woohoofemale = instance_manager.get(get_resource_key(T_WOOHOO_FEMALE, Types.TRAIT))
    t_woohoomale = instance_manager.get(get_resource_key(T_WOOHOO_MALE, Types.TRAIT))
    t_woohoonotfemale = instance_manager.get(get_resource_key(T_WOOHOO_NOTFEMALE, Types.TRAIT))
    t_woohoonotmale = instance_manager.get(get_resource_key(T_WOOHOO_NOTMALE, Types.TRAIT))

    t_toddler = instance_manager.get(get_resource_key(T_TODDLER, Types.TRAIT))
    t_child = instance_manager.get(get_resource_key(T_CHILD, Types.TRAIT))
    t_teen = instance_manager.get(get_resource_key(T_TEEN, Types.TRAIT))
    t_yadult = instance_manager.get(get_resource_key(T_YADULT, Types.TRAIT))
    t_adult = instance_manager.get(get_resource_key(T_ADULT, Types.TRAIT))
    t_elder = instance_manager.get(get_resource_key(T_ELDER, Types.TRAIT))

    t_female = instance_manager.get(get_resource_key(T_FEMALE, Types.TRAIT))
    t_male = instance_manager.get(get_resource_key(T_MALE, Types.TRAIT))

    t_adulterer = instance_manager.get(get_resource_key(T_WW_ADULTERER, Types.TRAIT))
    t_antisocial = instance_manager.get(get_resource_key(T_WW_ANTISOCIAL, Types.TRAIT))
    t_cuck = instance_manager.get(get_resource_key(T_WW_CUCKOLD, Types.TRAIT))
    t_cumslut = instance_manager.get(get_resource_key(T_WW_CUMSLUT, Types.TRAIT))
    t_noeyebrown = instance_manager.get(get_resource_key(T_WW_DISLIKE_EYE_BROWN, Types.TRAIT))
    t_noeyeunnatural = instance_manager.get(get_resource_key(T_WW_DISLIKE_EYE_UNNATURAL, Types.TRAIT))
    t_noblackhair = instance_manager.get(get_resource_key(T_WW_DISLIKE_HAIR_BLACK, Types.TRAIT))
    t_nobluehair = instance_manager.get(get_resource_key(T_WW_DISLIKE_HAIR_BLUE, Types.TRAIT))
    t_nogreenhair = instance_manager.get(get_resource_key(T_WW_DISLIKE_HAIR_GREEN, Types.TRAIT))
    t_nopinkhair = instance_manager.get(get_resource_key(T_WW_DISLIKE_HAIR_PINK, Types.TRAIT))
    t_nofat = instance_manager.get(get_resource_key(T_WW_DISLIKE_FAT, Types.TRAIT))
    t_nolargebreasts = instance_manager.get(get_resource_key(T_WW_DISLIKE_BREASTS, Types.TRAIT))
    t_nobigbutt = instance_manager.get(get_resource_key(T_WW_DISLIKE_BUTT, Types.TRAIT))
    t_nofemales = instance_manager.get(get_resource_key(T_WW_DISLIKE_FEMALE, Types.TRAIT))
    t_nomales = instance_manager.get(get_resource_key(T_WW_DISLIKE_MALE, Types.TRAIT))
    t_absorbancy = instance_manager.get(get_resource_key(T_WW_EXTRAABSORB, Types.TRAIT))
    t_genlover = instance_manager.get(get_resource_key(T_WW_GENLOVER, Types.TRAIT))
    t_incest = instance_manager.get(get_resource_key(T_WW_INCEST, Types.TRAIT))
    t_likeblondes = instance_manager.get(get_resource_key(T_WW_HAIR_BLONDE, Types.TRAIT))
    t_likebrunettes = instance_manager.get(get_resource_key(T_WW_HAIR_BROWN, Types.TRAIT))
    t_likeredheads = instance_manager.get(get_resource_key(T_WW_HAIR_RED, Types.TRAIT))
    t_beardlover = instance_manager.get(get_resource_key(T_WW_LIKESBEARD, Types.TRAIT))
    t_chubbychaser = instance_manager.get(get_resource_key(T_WW_LIKESFAT, Types.TRAIT))
    t_likegirls = instance_manager.get(get_resource_key(T_WW_LIKESFEMALES, Types.TRAIT))
    t_likefreckles = instance_manager.get(get_resource_key(T_WW_LIKESFRECKLES, Types.TRAIT))
    t_likehulk = instance_manager.get(get_resource_key(T_WW_LIKESHULK, Types.TRAIT))
    t_likejewelry = instance_manager.get(get_resource_key(T_WW_LIKESJEWELRY, Types.TRAIT))
    t_likemakeup = instance_manager.get(get_resource_key(T_WW_LIKESMAKEUP, Types.TRAIT))
    t_likeboys = instance_manager.get(get_resource_key(T_WW_LIKESMALES, Types.TRAIT))
    t_likeskinny = instance_manager.get(get_resource_key(T_WW_LIKESSKINNY, Types.TRAIT))
    t_likeflatchest = instance_manager.get(get_resource_key(T_WW_LIKESSMALLBREAST, Types.TRAIT))
    t_likeflatbutt = instance_manager.get(get_resource_key(T_WW_LIKESSMALLBUTT, Types.TRAIT))
    t_nounderwear = instance_manager.get(get_resource_key(T_WW_NOUNDERWEAR, Types.TRAIT))
    t_poly = instance_manager.get(get_resource_key(T_WW_POLY, Types.TRAIT))
    t_postpuberty = instance_manager.get(get_resource_key(T_WW_POSTPUBERTY, Types.TRAIT))
    t_sexuallyalluring = instance_manager.get(get_resource_key(T_WW_SEXUALLYALLURING, Types.TRAIT))

    if sim.has_trait(t_adventurous):
        sim.remove_trait(t_adventurous)

    if sim.has_trait(t_ambitious):
        sim.remove_trait(t_ambitious)

    if sim.has_trait(t_angler):
        sim.remove_trait(t_angler)

    if sim.has_trait(t_animalattraction):
        sim.remove_trait(t_animalattraction)

    if sim.has_trait(t_animalenthusiast):
        sim.remove_trait(t_animalenthusiast)

    if sim.has_trait(t_animalwhisperer):
        sim.remove_trait(t_animalwhisperer)

    if sim.has_trait(t_antiseptic):
        sim.remove_trait(t_antiseptic)

    if sim.has_trait(t_bro):
        sim.remove_trait(t_bro)

    if sim.has_trait(t_catlover):
        sim.remove_trait(t_catlover)

    if sim.has_trait(t_childofocean):
        sim.remove_trait(t_childofocean)

    if sim.has_trait(t_chopsticks):
        sim.remove_trait(t_chopsticks)

    if sim.has_trait(t_clumsy):
        sim.remove_trait(t_clumsy)

    if sim.has_trait(t_commitmentissues):
        sim.remove_trait(t_commitmentissues)

    if sim.has_trait(t_dastardly):
        sim.remove_trait(t_dastardly)

    if sim.has_trait(t_dauntless):
        sim.remove_trait(t_dauntless)

    if sim.has_trait(t_doglover):
        sim.remove_trait(t_doglover)

    if sim.has_trait(t_ecoengineer):
        sim.remove_trait(t_ecoengineer)

    if sim.has_trait(t_ecomaster):
        sim.remove_trait(t_ecomaster)

    if sim.has_trait(t_evil):
        sim.remove_trait(t_evil)

    if sim.has_trait(t_fakegenius):
        sim.remove_trait(t_fakegenius)

    if sim.has_trait(t_fertile):
        sim.remove_trait(t_fertile)

    if sim.has_trait(t_filthdweller):
        sim.remove_trait(t_filthdweller)

    if sim.has_trait(t_fizzyhead):
        sim.remove_trait(t_fizzyhead)

    if sim.has_trait(t_foodie):
        sim.remove_trait(t_foodie)

    if sim.has_trait(t_freegan):
        sim.remove_trait(t_freegan)

    if sim.has_trait(t_friendofsea):
        sim.remove_trait(t_friendofsea)

    if sim.has_trait(t_gloomy):
        sim.remove_trait(t_gloomy)

    if sim.has_trait(t_glutton):
        sim.remove_trait(t_glutton)

    if sim.has_trait(t_greenfiend):
        sim.remove_trait(t_greenfiend)

    if sim.has_trait(t_hateschildren):
        sim.remove_trait(t_hateschildren)

    if sim.has_trait(t_highmaintenance):
        sim.remove_trait(t_highmaintenance)

    if sim.has_trait(t_hotheaded):
        sim.remove_trait(t_hotheaded)

    if sim.has_trait(t_insane):
        sim.remove_trait(t_insane)

    if sim.has_trait(t_jealous):
        sim.remove_trait(t_jealous)

    if sim.has_trait(t_klepto):
        sim.remove_trait(t_klepto)

    if sim.has_trait(t_lactoseintol):
        sim.remove_trait(t_lactoseintol)

    if sim.has_trait(t_lazy):
        sim.remove_trait(t_lazy)

    if sim.has_trait(t_materialistic):
        sim.remove_trait(t_materialistic)

    if sim.has_trait(t_mean):
        sim.remove_trait(t_mean)

    if sim.has_trait(t_paranoid):
        sim.remove_trait(t_paranoid)

    if sim.has_trait(t_partyanimal):
        sim.remove_trait(t_partyanimal)

    if sim.has_trait(t_perfecthost):
        sim.remove_trait(t_perfecthost)

    if sim.has_trait(t_perfectionist):
        sim.remove_trait(t_perfectionist)

    if sim.has_trait(t_sacredknitknowledge):
        sim.remove_trait(t_sacredknitknowledge)

    if sim.has_trait(t_selfabsorbed):
        sim.remove_trait(t_selfabsorbed)

    if sim.has_trait(t_slob):
        sim.remove_trait(t_slob)

    if sim.has_trait(t_snob):
        sim.remove_trait(t_snob)

    if sim.has_trait(t_snowhate):
        sim.remove_trait(t_snowhate)

    if sim.has_trait(t_sociallyawkward):
        sim.remove_trait(t_sociallyawkward)

    if sim.has_trait(t_squemish):
        sim.remove_trait(t_squemish)

    if sim.has_trait(t_unflirty):
        sim.remove_trait(t_unflirty)

    if sim.has_trait(t_unstoppablefame):
        sim.remove_trait(t_unstoppablefame)

    if sim.has_trait(t_untroubled):
        sim.remove_trait(t_untroubled)

    if sim.has_trait(t_vegetarian):
        sim.remove_trait(t_vegetarian)

    if sim.has_trait(t_toddler) or sim.has_trait(t_child):
        output = sims4.commands.CheatOutput(_connection)
        output("Skipping WW traits as sim is a minor")

    if sim.has_trait(t_child):
        if sim.has_trait(t_gschoolb):
            sim.remove_trait(t_gschoolb)

        if sim.has_trait(t_gschoolc):
            sim.remove_trait(t_gschoolc)

        if sim.has_trait(t_gschoold):
            sim.remove_trait(t_gschoold)

        if sim.has_trait(t_gschoolf):
            sim.remove_trait(t_gschoolf)

        if not sim.has_trait(t_gschoola):
            sim.add_trait(t_gschoola)

    if sim.has_trait(t_teen):
        if sim.has_trait(t_hschoolb):
            sim.remove_trait(t_hschoolb)

        if sim.has_trait(t_hschoolc):
            sim.remove_trait(t_hschoolc)

        if sim.has_trait(t_hschoold):
            sim.remove_trait(t_hschoold)

        if sim.has_trait(t_hschoolf):
            sim.remove_trait(t_hschoolf)

        if not sim.has_trait(t_hschoola):
            sim.add_trait(t_hschoola)

        if sim.has_trait(t_hsexit_dropout):
            sim.remove_trait(t_hsexit_dropout)

        if sim.has_trait(t_hsexit_expel):
            sim.remove_trait(t_hsexit_expel)

        if sim.has_trait(t_hsexit_early):
            sim.remove_trait(t_hsexit_early)

        if sim.has_trait(t_hsexit_honors):
            sim.remove_trait(t_hsexit_honors)

        if sim.has_trait(t_hsexit_valedictorian):
            sim.remove_trait(t_hsexit_valedictorian)

        if not sim.has_trait(t_hsexit_earnedged):
            sim.add_trait(t_hsexit_earnedged)

    # If teen or older, set gender and sexual orientation traits
    if sim.has_trait(t_teen) or sim.has_trait(t_adult) or sim.has_trait(t_yadult) or sim.has_trait(t_elder):
        if sim.has_trait(t_female):
            sim.add_trait(t_absorbancy)
            sim.add_trait(t_cumslut)

            sim.add_trait(t_beardlover)
            sim.add_trait(t_chubbychaser)
            sim.add_trait(t_likeboys)

            if not sim.has_trait(t_customgender):
                sim.add_trait(t_customgender)

            if sim.has_trait(t_canimpgregnate):
                sim.remove_trait(t_canimpgregnate)

            if not sim.has_trait(t_rommale):
                sim.add_trait(t_rommale)

            if sim.has_trait(t_romnotmale):
                sim.remove_trait(t_romnotmale)
                sim.add_trait(t_rommale)

            if not sim.has_trait(t_rommale):
                sim.add_trait(t_rommale)

            if sim.has_trait(t_woohoonotfemale):
                sim.remove_trait(t_woohoonotfemale)
                sim.add_trait(t_woohoofemale)

            if not sim.has_trait(t_woohoofemale):
                sim.add_trait(t_woohoofemale)

            if not sim.has_trait(t_romfemale):
                sim.add_trait(t_romfemale)

            if sim.has_trait(t_woohoonotmale):
                sim.remove_trait(t_woohoonotmale)
                sim.add_trait(t_woohoomale)

        if sim.has_trait(t_male):
            sim.add_trait(t_nomales)
            sim.add_trait(t_nofat)
            sim.add_trait(t_likemakeup)
            sim.add_trait(t_likeskinny)
            sim.add_trait(t_likegirls)

            if sim.has_trait(t_canbeimpregnated):
                sim.remove_trait(t_canbeimpregnated)

            if sim.has_trait(t_woohoomale):
                sim.remove_trait(t_woohoomale)

            if not sim.has_trait(t_woohoonotmale):
                sim.add_trait(t_woohoonotmale)

        if sim.has_trait(t_romnotexplore):
            sim.remove_trait(t_romnotexplore)
            sim.add_trait(t_romexplore)

        if not sim.has_trait(t_romexplore):
            sim.add_trait(t_romexplore)

        if sim.has_trait(t_romnotfemale):
            sim.remove_trait(t_romnotfemale)
            sim.add_trait(t_romfemale)

        if not sim.has_trait(t_romfemale):
            sim.add_trait(t_romfemale)

        if not sim.has_trait(t_woohoofemale):
            sim.add_trait(t_woohoofemale)

        if sim.has_trait(t_teen):
            sim.add_trait(t_postpuberty)

        sim.add_trait(t_adulterer)
        sim.add_trait(t_cuck)
        sim.add_trait(t_genlover)
        sim.add_trait(t_incest)
        sim.add_trait(t_poly)
        sim.add_trait(t_sexuallyalluring)

        sim.add_trait(t_noeyebrown)
        sim.add_trait(t_noeyeunnatural)
        sim.add_trait(t_noblackhair)
        sim.add_trait(t_nobluehair)
        sim.add_trait(t_nogreenhair)
        sim.add_trait(t_nopinkhair)
        sim.add_trait(t_nolargebreasts)
        sim.add_trait(t_nobigbutt)
        sim.add_trait(t_likeblondes)
        sim.add_trait(t_likebrunettes)
        sim.add_trait(t_likeredheads)
        sim.add_trait(t_likefreckles)
        sim.add_trait(t_likehulk)
        sim.add_trait(t_likejewelry)
        sim.add_trait(t_likeflatchest)
        sim.add_trait(t_likeflatbutt)

    if sim.has_trait(t_adult) or sim.has_trait(t_yadult) or sim.has_trait(t_elder):
        if not sim.has_trait(t_pamatriarch):
            sim.add_trait(t_pamatriarch)

        if sim.has_trait(t_female):
            if sim.has_trait(t_lskill_argumentative):
                sim.remove_trait(t_lskill_argumentative)

            if sim.has_trait(t_lskill_badmanners):
                sim.remove_trait(t_lskill_badmanners)

            if sim.has_trait(t_lskill_irresponsible):
                sim.remove_trait(t_lskill_irresponsible)

            if sim.has_trait(t_lskill_uncontrolledemotion):
                sim.remove_trait(t_lskill_uncontrolledemotion)

            if sim.has_trait(t_lskill_unfeeling):
                sim.remove_trait(t_lskill_unfeeling)

            if not sim.has_trait(t_lskill_compassionate):
                sim.add_trait(t_lskill_compassionate)

            if not sim.has_trait(t_lskill_goodmanners):
                sim.add_trait(t_lskill_goodmanners)
# Things above apply to teen or older

# Any age
    if sim.has_trait(t_female):
        if not sim.has_trait(t_alluring):
            sim.add_trait(t_alluring)

    if not sim.has_trait(t_active):
        sim.add_trait(t_active)

    if not sim.has_trait(t_alwayswelcome):
        sim.add_trait(t_alwayswelcome)

    if not sim.has_trait(t_brave):
        sim.add_trait(t_brave)

    if not sim.has_trait(t_carefree):
        sim.add_trait(t_carefree)

    if not sim.has_trait(t_essenceofflavor):
        sim.add_trait(t_essenceofflavor)

    if not sim.has_trait(t_eternalbond):
        sim.add_trait(t_eternalbond)

    if not sim.has_trait(t_foreverfresh):
        sim.add_trait(t_foreverfresh)

    if not sim.has_trait(t_freeservices):
        sim.add_trait(t_freeservices)

    if not sim.has_trait(t_freshchef):
        sim.add_trait(t_freshchef)

    if not sim.has_trait(t_frugal):
        sim.add_trait(t_frugal)

    if not sim.has_trait(t_geek):
        sim.add_trait(t_geek)

    if not sim.has_trait(t_genius):
        sim.add_trait(t_genius)

    if not sim.has_trait(t_good):
        sim.add_trait(t_good)

    if not sim.has_trait(t_greatkisser):
        sim.add_trait(t_greatkisser)

    if not sim.has_trait(t_heatproof):
        sim.add_trait(t_heatproof)

    if not sim.has_trait(t_highmetab):
        sim.add_trait(t_highmetab)

    if not sim.has_trait(t_iceproof):
        sim.add_trait(t_iceproof)

    if not sim.has_trait(t_invested):
        sim.add_trait(t_invested)

    if not sim.has_trait(t_longevity):
        sim.add_trait(t_longevity)

    if not sim.has_trait(t_mastermixer):
        sim.add_trait(t_mastermixer)

    if not sim.has_trait(t_mentor):
        sim.add_trait(t_mentor)

    if not sim.has_trait(t_mountaineer3):
        sim.add_trait(t_mountaineer3)

    if not sim.has_trait(t_observant):
        sim.add_trait(t_observant)

    if not sim.has_trait(t_onewithnature):
        sim.add_trait(t_onewithnature)

    if not sim.has_trait(t_player):
        sim.add_trait(t_player)

    if not sim.has_trait(t_reprankpristine):
        sim.add_trait(t_reprankpristine)

    if not sim.has_trait(t_rolemodel):
        sim.add_trait(t_rolemodel)

    if not sim.has_trait(t_romantic):
        sim.add_trait(t_romantic)

    if not sim.has_trait(t_selfassured):
        sim.add_trait(t_selfassured)

    if not sim.has_trait(t_shameless):
        sim.add_trait(t_shameless)

    if not sim.has_trait(t_sicknessimmunity):
        sim.add_trait(t_sicknessimmunity)

    if not sim.has_trait(t_snowlove):
        sim.add_trait(t_snowlove)

    if not sim.has_trait(t_speedcleaner):
        sim.add_trait(t_speedcleaner)

    if not sim.has_trait(t_speedreader):
        sim.add_trait(t_speedreader)

    if not sim.has_trait(t_stormchaser):
        sim.add_trait(t_stormchaser)

    if not sim.has_trait(t_stovesandgrillmaster):
        sim.add_trait(t_stovesandgrillmaster)

    if not sim.has_trait(t_supergreenthumb):
        sim.add_trait(t_supergreenthumb)

    if not sim.has_trait(t_survivalist):
        sim.add_trait(t_survivalist)

    if not sim.has_trait(t_theknack):
        sim.add_trait(t_theknack)

    if not sim.has_trait(t_theknowledge):
        sim.add_trait(t_theknowledge)

    if not sim.has_trait(t_overclock):
        sim.add_trait(t_overclock)

    if not sim.has_trait(t_waterproof):
        sim.add_trait(t_waterproof)

    if not sim.has_trait(t_webmaster):
        sim.add_trait(t_webmaster)

    if not sim.has_trait(t_selfcareexpert):
        sim.add_trait(t_selfcareexpert)

    if not sim.has_trait(t_spamember):
        sim.add_trait(t_spamember)


@sims4.commands.Command('pbs_nanny', command_type=sims4.commands.CommandType.Live)
def pbs_nanny(_connection=None):
    # Get the console output
    output = sims4.commands.CheatOutput(_connection)

    # Get the sim_info for the active sim
    sim = services.client_manager().get(_connection).active_sim.sim_info

    # Get the tuned trait instance from the tuning instance manager
    instance_manager = services.get_instance_manager(Types.TRAIT)
    t_active = instance_manager.get(get_resource_key(T_ACTIVE, Types.TRAIT))
    t_alluring = instance_manager.get(get_resource_key(T_ALLURING, Types.TRAIT))
    t_bookworm = instance_manager.get(get_resource_key(T_BOOKWORM, Types.TRAIT))
    t_cheerful = instance_manager.get(get_resource_key(T_CHEERFUL, Types.TRAIT))
    t_childish = instance_manager.get(get_resource_key(T_CHILDISH, Types.TRAIT))
    t_commitmentissues = instance_manager.get(get_resource_key(T_COMMITMENTISSUES, Types.TRAIT))
    t_dastardly = instance_manager.get(get_resource_key(T_DASTARDLY, Types.TRAIT))
    t_dauntless = instance_manager.get(get_resource_key(T_DAUNTLESS, Types.TRAIT))
    t_essenceofflavor = instance_manager.get(get_resource_key(T_ESSENCEOFFLAVOR, Types.TRAIT))
    t_evil = instance_manager.get(get_resource_key(T_EVIL, Types.TRAIT))
    t_familysim = instance_manager.get(get_resource_key(T_FAMILYSIM, Types.TRAIT))
    t_fastfastidious = instance_manager.get(get_resource_key(T_FASTFASTIDIOUS, Types.TRAIT))
    t_fertile = instance_manager.get(get_resource_key(T_FERTILE, Types.TRAIT))
    t_filthdweller = instance_manager.get(get_resource_key(T_FILTHDWELLER, Types.TRAIT))
    t_freeservices = instance_manager.get(get_resource_key(T_FREESERVICES, Types.TRAIT))
    t_freshchef = instance_manager.get(get_resource_key(T_FRESHCHEF, Types.TRAIT))
    t_frugal = instance_manager.get(get_resource_key(T_FRUGAL, Types.TRAIT))
    t_geek = instance_manager.get(get_resource_key(T_GEEK, Types.TRAIT))
    t_genius = instance_manager.get(get_resource_key(T_GENIUS, Types.TRAIT))
    t_gloomy = instance_manager.get(get_resource_key(T_GLOOMY, Types.TRAIT))
    t_glutton = instance_manager.get(get_resource_key(T_GLUTTON, Types.TRAIT))
    t_good = instance_manager.get(get_resource_key(T_GOOD, Types.TRAIT))
    t_goofball = instance_manager.get(get_resource_key(T_GOOFBALL, Types.TRAIT))
    t_goodstories = instance_manager.get(get_resource_key(T_GOODSTRORIES, Types.TRAIT))
    t_hateschildren = instance_manager.get(get_resource_key(T_HATESCHILDREN, Types.TRAIT))
    t_heatproof = instance_manager.get(get_resource_key(T_HEATPROOF, Types.TRAIT))
    t_highmetab = instance_manager.get(get_resource_key(T_HIGHMET, Types.TRAIT))
    t_hilarious = instance_manager.get(get_resource_key(T_HILARIOUS, Types.TRAIT))
    t_hotheaded = instance_manager.get(get_resource_key(T_HOTHEADED, Types.TRAIT))
    t_iceproof = instance_manager.get(get_resource_key(T_ICEPROOF, Types.TRAIT))
    t_incrediblyfriendly = instance_manager.get(get_resource_key(T_INCREDFRIENDLY, Types.TRAIT))
    t_insane = instance_manager.get(get_resource_key(T_INSANE, Types.TRAIT))
    t_invested = instance_manager.get(get_resource_key(T_INVESTED, Types.TRAIT))
    t_jealous = instance_manager.get(get_resource_key(T_JEALOUS, Types.TRAIT))
    t_kindnessambasador = instance_manager.get(get_resource_key(T_KINDNESSAMB, Types.TRAIT))
    t_klepto = instance_manager.get(get_resource_key(T_KLEPTO, Types.TRAIT))
    t_lactoseintol = instance_manager.get(get_resource_key(T_LACTOSEINTOLERANT, Types.TRAIT))
    t_lazy = instance_manager.get(get_resource_key(T_LAZY, Types.TRAIT))
    t_loner = instance_manager.get(get_resource_key(T_LONER, Types.TRAIT))
    t_longevity = instance_manager.get(get_resource_key(T_LONGEVITY, Types.TRAIT))
    t_lskill_argumentative = instance_manager.get(get_resource_key(T_LSKILL_ARGUMENTATIVE, Types.TRAIT))
    t_lskill_badmanners = instance_manager.get(get_resource_key(T_LSKILL_BADMANNERS, Types.TRAIT))
    t_lskill_irresponsible = instance_manager.get(get_resource_key(T_LSKILL_IRRESPONSIBLE, Types.TRAIT))
    t_lskill_uncontrolledemotion = instance_manager.get(get_resource_key(T_LSKILL_UNCONTROLEMOTION, Types.TRAIT))
    t_lskill_unfeeling = instance_manager.get(get_resource_key(T_LSKILL_UNFEELING, Types.TRAIT))
    t_materialistic = instance_manager.get(get_resource_key(T_MATERIALISTIC, Types.TRAIT))
    t_mean = instance_manager.get(get_resource_key(T_MEAN, Types.TRAIT))
    t_mentor = instance_manager.get(get_resource_key(T_MENTOR, Types.TRAIT))
    t_neat = instance_manager.get(get_resource_key(T_NEAT, Types.TRAIT))
    t_observant = instance_manager.get(get_resource_key(T_OBSERVANT, Types.TRAIT))
    t_outgoing = instance_manager.get(get_resource_key(T_OUTGOING, Types.TRAIT))
    t_paranoid = instance_manager.get(get_resource_key(T_PARANOID, Types.TRAIT))
    t_perfectionist = instance_manager.get(get_resource_key(T_PERFECTIONIST, Types.TRAIT))
    t_professionalslacker = instance_manager.get(get_resource_key(T_PROFSLACKER, Types.TRAIT))
    t_proper = instance_manager.get(get_resource_key(T_PROPER, Types.TRAIT))
    t_quicklearner = instance_manager.get(get_resource_key(T_QUICKLEARNER, Types.TRAIT))
    t_recycledisciple = instance_manager.get(get_resource_key(T_RECYCLEDISCIPLE, Types.TRAIT))
    t_rolemodel = instance_manager.get(get_resource_key(T_ROLEMODEL, Types.TRAIT))
    t_selfassured = instance_manager.get(get_resource_key(T_SELFASSURED, Types.TRAIT))
    t_slob = instance_manager.get(get_resource_key(T_SLOB, Types.TRAIT))
    t_snob = instance_manager.get(get_resource_key(T_SNOB, Types.TRAIT))
    t_snowhate = instance_manager.get(get_resource_key(T_SNOWHATE, Types.TRAIT))
    t_snowlove = instance_manager.get(get_resource_key(T_SNOWLOVE, Types.TRAIT))
    t_sociallyawkward = instance_manager.get(get_resource_key(T_SOCIALLYAWKWARD, Types.TRAIT))
    t_sociallygifted = instance_manager.get(get_resource_key(T_SOCIALLYGIFTED, Types.TRAIT))
    t_speedcleaner = instance_manager.get(get_resource_key(T_SPEEDCLEANER, Types.TRAIT))
    t_speedreader = instance_manager.get(get_resource_key(T_SPEEDREADER, Types.TRAIT))
    t_squemish = instance_manager.get(get_resource_key(T_SQUEMISH, Types.TRAIT))
    t_stormchaser = instance_manager.get(get_resource_key(T_STORMCHASER, Types.TRAIT))
    t_theknack = instance_manager.get(get_resource_key(T_THEKNACK, Types.TRAIT))
    t_unflirty = instance_manager.get(get_resource_key(T_UNFLIRTY, Types.TRAIT))
    t_untroubled = instance_manager.get(get_resource_key(T_UNTROUBLED, Types.TRAIT))
    t_waterproof = instance_manager.get(get_resource_key(T_WATERPROOF, Types.TRAIT))

    t_customgender = instance_manager.get(get_resource_key(T_PREG_CUSTOM, Types.TRAIT))
    t_romfemale = instance_manager.get(get_resource_key(T_ROM_ATTFEMALE, Types.TRAIT))
    t_rommale = instance_manager.get(get_resource_key(T_ROM_ATTMALE, Types.TRAIT))
    t_romnotfemale = instance_manager.get(get_resource_key(T_ROM_ATTNOTFEMALE, Types.TRAIT))
    t_romnotmale = instance_manager.get(get_resource_key(T_ROM_ATTNOTMALE, Types.TRAIT))
    t_romexplore = instance_manager.get(get_resource_key(T_ROM_EXPLORING, Types.TRAIT))
    t_romnotexplore = instance_manager.get(get_resource_key(T_ROM_NOTEXPLORING, Types.TRAIT))
    t_canbeimpregnated = instance_manager.get(get_resource_key(T_PREG_CANBEIMREGNATED, Types.TRAIT))
    t_canimpgregnate = instance_manager.get(get_resource_key(T_PREG_CANIMPREGNATE, Types.TRAIT))
    t_woohoofemale = instance_manager.get(get_resource_key(T_WOOHOO_FEMALE, Types.TRAIT))
    t_woohoomale = instance_manager.get(get_resource_key(T_WOOHOO_MALE, Types.TRAIT))
    t_woohoonotfemale = instance_manager.get(get_resource_key(T_WOOHOO_NOTFEMALE, Types.TRAIT))
    t_woohoonotmale = instance_manager.get(get_resource_key(T_WOOHOO_NOTMALE, Types.TRAIT))

    t_teen = instance_manager.get(get_resource_key(T_TEEN, Types.TRAIT))
    t_yadult = instance_manager.get(get_resource_key(T_YADULT, Types.TRAIT))
    t_adult = instance_manager.get(get_resource_key(T_ADULT, Types.TRAIT))
    t_elder = instance_manager.get(get_resource_key(T_ELDER, Types.TRAIT))

    t_female = instance_manager.get(get_resource_key(T_FEMALE, Types.TRAIT))

    t_adulterer = instance_manager.get(get_resource_key(T_WW_ADULTERER, Types.TRAIT))
    t_cuck = instance_manager.get(get_resource_key(T_WW_CUCKOLD, Types.TRAIT))
    t_cumslut = instance_manager.get(get_resource_key(T_WW_CUMSLUT, Types.TRAIT))
    t_noeyebrown = instance_manager.get(get_resource_key(T_WW_DISLIKE_EYE_BROWN, Types.TRAIT))
    t_noeyeunnatural = instance_manager.get(get_resource_key(T_WW_DISLIKE_EYE_UNNATURAL, Types.TRAIT))
    t_noblackhair = instance_manager.get(get_resource_key(T_WW_DISLIKE_HAIR_BLACK, Types.TRAIT))
    t_nobluehair = instance_manager.get(get_resource_key(T_WW_DISLIKE_HAIR_BLUE, Types.TRAIT))
    t_nogreenhair = instance_manager.get(get_resource_key(T_WW_DISLIKE_HAIR_GREEN, Types.TRAIT))
    t_nopinkhair = instance_manager.get(get_resource_key(T_WW_DISLIKE_HAIR_PINK, Types.TRAIT))
    t_nolargebreasts = instance_manager.get(get_resource_key(T_WW_DISLIKE_BREASTS, Types.TRAIT))
    t_nobigbutt = instance_manager.get(get_resource_key(T_WW_DISLIKE_BUTT, Types.TRAIT))
    t_absorbancy = instance_manager.get(get_resource_key(T_WW_EXTRAABSORB, Types.TRAIT))
    t_genlover = instance_manager.get(get_resource_key(T_WW_GENLOVER, Types.TRAIT))
    t_likeblondes = instance_manager.get(get_resource_key(T_WW_HAIR_BLONDE, Types.TRAIT))
    t_likebrunettes = instance_manager.get(get_resource_key(T_WW_HAIR_BROWN, Types.TRAIT))
    t_likeredheads = instance_manager.get(get_resource_key(T_WW_HAIR_RED, Types.TRAIT))
    t_beardlover = instance_manager.get(get_resource_key(T_WW_LIKESBEARD, Types.TRAIT))
    t_chubbychaser = instance_manager.get(get_resource_key(T_WW_LIKESFAT, Types.TRAIT))
    t_likegirls = instance_manager.get(get_resource_key(T_WW_LIKESFEMALES, Types.TRAIT))
    t_likefreckles = instance_manager.get(get_resource_key(T_WW_LIKESFRECKLES, Types.TRAIT))
    t_likejewelry = instance_manager.get(get_resource_key(T_WW_LIKESJEWELRY, Types.TRAIT))
    t_likeboys = instance_manager.get(get_resource_key(T_WW_LIKESMALES, Types.TRAIT))
    t_likeflatchest = instance_manager.get(get_resource_key(T_WW_LIKESSMALLBREAST, Types.TRAIT))
    t_likeflatbutt = instance_manager.get(get_resource_key(T_WW_LIKESSMALLBUTT, Types.TRAIT))
    t_poly = instance_manager.get(get_resource_key(T_WW_POLY, Types.TRAIT))
    t_postpuberty = instance_manager.get(get_resource_key(T_WW_POSTPUBERTY, Types.TRAIT))

    #If teen or older, set gender and sexual orientation traits
    if sim.has_trait(t_teen) or sim.has_trait(t_adult) or sim.has_trait(t_yadult) or sim.has_trait(t_elder):
        #If teen
        if sim.has_trait(t_teen):
            sim.add_trait(t_postpuberty)

        #If female
        if sim.has_trait(t_female):
            sim.add_trait(t_absorbancy)
            sim.add_trait(t_cumslut)

            sim.add_trait(t_beardlover)
            sim.add_trait(t_chubbychaser)
            sim.add_trait(t_likeboys)

            if not sim.has_trait(t_customgender):
                sim.add_trait(t_customgender)

            if sim.has_trait(t_canbeimpregnated):
                sim.remove_trait(t_canbeimpregnated)

            if sim.has_trait(t_canimpgregnate):
                sim.remove_trait(t_canimpgregnate)

            if not sim.has_trait(t_rommale):
                sim.add_trait(t_rommale)

            if sim.has_trait(t_romnotmale):
                sim.remove_trait(t_romnotmale)
                sim.add_trait(t_rommale)

            if sim.has_trait(t_woohoonotfemale):
                sim.remove_trait(t_woohoonotfemale)
                sim.add_trait(t_woohoofemale)

            if sim.has_trait(t_woohoonotmale):
                sim.remove_trait(t_woohoonotmale)
                sim.add_trait(t_woohoomale)

            if not sim.has_trait(t_woohoomale):
                sim.add_trait(t_woohoomale)

        #For all teen or older
        if sim.has_trait(t_romnotexplore):
            sim.remove_trait(t_romnotexplore)
            sim.add_trait(t_romexplore)

        if not sim.has_trait(t_romexplore):
            sim.add_trait(t_romexplore)

        if sim.has_trait(t_romnotfemale):
            sim.remove_trait(t_romnotfemale)
            sim.add_trait(t_romfemale)

        if not sim.has_trait(t_romfemale):
            sim.add_trait(t_romfemale)

        if not sim.has_trait(t_woohoofemale):
            sim.add_trait(t_woohoofemale)

        sim.add_trait(t_adulterer)
        sim.add_trait(t_cuck)
        sim.add_trait(t_genlover)
        sim.add_trait(t_poly)

        sim.add_trait(t_likegirls)
        sim.add_trait(t_noeyebrown)
        sim.add_trait(t_noeyeunnatural)
        sim.add_trait(t_noblackhair)
        sim.add_trait(t_nobluehair)
        sim.add_trait(t_nogreenhair)
        sim.add_trait(t_nopinkhair)
        sim.add_trait(t_nolargebreasts)
        sim.add_trait(t_nobigbutt)
        sim.add_trait(t_likeblondes)
        sim.add_trait(t_likebrunettes)
        sim.add_trait(t_likeredheads)
        sim.add_trait(t_likefreckles)
        sim.add_trait(t_likejewelry)
        sim.add_trait(t_likeflatchest)
        sim.add_trait(t_likeflatbutt)
# Things above apply to teen or older

# Any age
    if sim.has_trait(t_female):
        if not sim.has_trait(t_alluring):
            sim.add_trait(t_alluring)

    if not sim.has_trait(t_active):
        sim.add_trait(t_active)

    if not sim.has_trait(t_bookworm):
        sim.add_trait(t_bookworm)

    if not sim.has_trait(t_cheerful):
        sim.add_trait(t_cheerful)

    if not sim.has_trait(t_childish):
        sim.add_trait(t_childish)

    if sim.has_trait(t_commitmentissues):
        sim.remove_trait(t_commitmentissues)

    if sim.has_trait(t_dastardly):
        sim.remove_trait(t_dastardly)

    if sim.has_trait(t_dauntless):
        sim.remove_trait(t_dauntless)

    if not sim.has_trait(t_essenceofflavor):
        sim.add_trait(t_essenceofflavor)

    if sim.has_trait(t_evil):
        sim.remove_trait(t_evil)

    if not sim.has_trait(t_familysim):
        sim.add_trait(t_familysim)

    if not sim.has_trait(t_fastfastidious):
        sim.add_trait(t_fastfastidious)

    if sim.has_trait(t_fertile):
        sim.remove_trait(t_fertile)

    if sim.has_trait(t_filthdweller):
        sim.remove_trait(t_filthdweller)

    if not sim.has_trait(t_freeservices):
        sim.add_trait(t_freeservices)

    if not sim.has_trait(t_freshchef):
        sim.add_trait(t_freshchef)

    if not sim.has_trait(t_frugal):
        sim.add_trait(t_frugal)

    if not sim.has_trait(t_geek):
        sim.add_trait(t_geek)

    if not sim.has_trait(t_genius):
        sim.add_trait(t_genius)

    if sim.has_trait(t_gloomy):
        sim.remove_trait(t_gloomy)

    if sim.has_trait(t_glutton):
        sim.remove_trait(t_glutton)

    if not sim.has_trait(t_good):
        sim.add_trait(t_good)

    if not sim.has_trait(t_goodstories):
        sim.add_trait(t_goodstories)

    if not sim.has_trait(t_goofball):
        sim.add_trait(t_goofball)

    if sim.has_trait(t_hateschildren):
        sim.remove_trait(t_hateschildren)

    if not sim.has_trait(t_heatproof):
        sim.add_trait(t_heatproof)

    if not sim.has_trait(t_highmetab):
        sim.add_trait(t_highmetab)

    if not sim.has_trait(t_hilarious):
        sim.add_trait(t_hilarious)

    if sim.has_trait(t_hotheaded):
        sim.remove_trait(t_hotheaded)

    if not sim.has_trait(t_iceproof):
        sim.add_trait(t_iceproof)

    if not sim.has_trait(t_incrediblyfriendly):
        sim.add_trait(t_incrediblyfriendly)

    if sim.has_trait(t_insane):
        sim.remove_trait(t_insane)

    if not sim.has_trait(t_invested):
        sim.add_trait(t_invested)

    if sim.has_trait(t_jealous):
        sim.remove_trait(t_jealous)

    if not sim.has_trait(t_kindnessambasador):
        sim.add_trait(t_kindnessambasador)

    if sim.has_trait(t_klepto):
        sim.remove_trait(t_klepto)

    if sim.has_trait(t_lactoseintol):
        sim.remove_trait(t_lactoseintol)

    if sim.has_trait(t_lazy):
        sim.remove_trait(t_lazy)

    if sim.has_trait(t_loner):
        sim.remove_trait(t_loner)

    if not sim.has_trait(t_longevity):
        sim.add_trait(t_longevity)

    if sim.has_trait(t_lskill_argumentative):
        sim.remove_trait(t_lskill_argumentative)

    if sim.has_trait(t_lskill_badmanners):
        sim.remove_trait(t_lskill_badmanners)

    if sim.has_trait(t_lskill_irresponsible):
        sim.remove_trait(t_lskill_irresponsible)

    if sim.has_trait(t_lskill_uncontrolledemotion):
        sim.remove_trait(t_lskill_uncontrolledemotion)

    if sim.has_trait(t_lskill_unfeeling):
        sim.remove_trait(t_lskill_unfeeling)

    if sim.has_trait(t_materialistic):
        sim.remove_trait(t_materialistic)

    if sim.has_trait(t_mean):
        sim.remove_trait(t_mean)

    if not sim.has_trait(t_mentor):
        sim.add_trait(t_mentor)

    if not sim.has_trait(t_neat):
        sim.add_trait(t_neat)

    if not sim.has_trait(t_observant):
        sim.add_trait(t_observant)

    if not sim.has_trait(t_outgoing):
        sim.add_trait(t_outgoing)

    if sim.has_trait(t_paranoid):
        sim.remove_trait(t_paranoid)

    if not sim.has_trait(t_perfectionist):
        sim.add_trait(t_perfectionist)

    if sim.has_trait(t_professionalslacker):
        sim.remove_trait(t_professionalslacker)

    if sim.has_trait(t_proper):
        sim.remove_trait(t_proper)

    if sim.has_trait(t_quicklearner):
        sim.remove_trait(t_quicklearner)

    if not sim.has_trait(t_recycledisciple):
        sim.add_trait(t_recycledisciple)

    if not sim.has_trait(t_rolemodel):
        sim.add_trait(t_rolemodel)

    if not sim.has_trait(t_selfassured):
        sim.add_trait(t_selfassured)

    if sim.has_trait(t_slob):
        sim.remove_trait(t_slob)

    if sim.has_trait(t_snob):
        sim.remove_trait(t_snob)

    if sim.has_trait(t_snowhate):
        sim.remove_trait(t_snowhate)

    if not sim.has_trait(t_snowlove):
        sim.add_trait(t_snowlove)

    if sim.has_trait(t_sociallyawkward):
        sim.remove_trait(t_sociallyawkward)

    if not sim.has_trait(t_sociallygifted):
        sim.add_trait(t_sociallygifted)

    if not sim.has_trait(t_speedcleaner):
        sim.add_trait(t_speedcleaner)

    if not sim.has_trait(t_speedreader):
        sim.add_trait(t_speedreader)

    if sim.has_trait(t_squemish):
        sim.remove_trait(t_squemish)

    if not sim.has_trait(t_stormchaser):
        sim.add_trait(t_stormchaser)

    if not sim.has_trait(t_theknack):
        sim.add_trait(t_theknack)

    if sim.has_trait(t_unflirty):
        sim.remove_trait(t_unflirty)

    if sim.has_trait(t_untroubled):
        sim.remove_trait(t_untroubled)

    if not sim.has_trait(t_waterproof):
        sim.add_trait(t_waterproof)


@sims4.commands.Command('pbs_sex', command_type=sims4.commands.CommandType.Live)
def pbs_sex(_connection=None):
    # Get the console output
    output = sims4.commands.CheatOutput(_connection)

    # Get the sim_info for the active sim
    sim = services.client_manager().get(_connection).active_sim.sim_info

    # Get the tuned trait instance from the tuning instance manager
    instance_manager = services.get_instance_manager(Types.TRAIT)
    T_customgender = instance_manager.get(get_resource_key(T_PREG_CUSTOM, Types.TRAIT))
    T_romfemale = instance_manager.get(get_resource_key(T_ROM_ATTFEMALE, Types.TRAIT))
    T_rommale = instance_manager.get(get_resource_key(T_ROM_ATTMALE, Types.TRAIT))
    T_romnotfemale = instance_manager.get(get_resource_key(T_ROM_ATTNOTFEMALE, Types.TRAIT))
    T_romnotmale = instance_manager.get(get_resource_key(T_ROM_ATTNOTMALE, Types.TRAIT))
    T_romexplore = instance_manager.get(get_resource_key(T_ROM_EXPLORING, Types.TRAIT))
    T_romnotexplore = instance_manager.get(get_resource_key(T_ROM_NOTEXPLORING, Types.TRAIT))
    T_canbeimpregnated = instance_manager.get(get_resource_key(T_PREG_CANBEIMREGNATED, Types.TRAIT))
    T_canimpgregnate = instance_manager.get(get_resource_key(T_PREG_CANIMPREGNATE, Types.TRAIT))
    T_woohoofemale = instance_manager.get(get_resource_key(T_WOOHOO_FEMALE, Types.TRAIT))
    T_woohoomale = instance_manager.get(get_resource_key(T_WOOHOO_MALE, Types.TRAIT))
    T_woohoonotfemale = instance_manager.get(get_resource_key(T_WOOHOO_NOTFEMALE, Types.TRAIT))
    T_woohoonotmale = instance_manager.get(get_resource_key(T_WOOHOO_NOTMALE, Types.TRAIT))

    # Set the traits desired
    if not sim.has_trait(T_customgender):
        sim.add_trait(T_customgender)

    if sim.has_trait(T_canimpgregnate):
        sim.remove_trait(T_canimpgregnate)

    if sim.has_trait(T_canbeimpregnated):
        sim.remove_trait(T_canbeimpregnated)

    if sim.has_trait(T_romnotexplore):
        sim.remove_trait(T_romnotexplore)
        sim.add_trait(T_romexplore)

    if not sim.has_trait(T_romexplore):
        sim.add_trait(T_romexplore)

    if sim.has_trait(T_romnotfemale):
        sim.remove_trait(T_romnotfemale)
        sim.add_trait(T_romfemale)

    if not sim.has_trait(T_romfemale):
        sim.add_trait(T_romfemale)

    if sim.has_trait(T_romnotmale):
        sim.remove_trait(T_romnotmale)
        sim.add_trait(T_rommale)

    if not sim.has_trait(T_rommale):
        sim.add_trait(T_rommale)

    if sim.has_trait(T_woohoonotfemale):
        sim.remove_trait(T_woohoonotfemale)
        sim.add_trait(T_woohoofemale)

    if not sim.has_trait(T_woohoofemale):
        sim.add_trait(T_woohoofemale)

    if sim.has_trait(T_woohoonotmale):
        sim.remove_trait(T_woohoonotmale)
        sim.add_trait(T_woohoomale)

    if not sim.has_trait(T_woohoomale):
        sim.add_trait(T_woohoomale)


@sims4.commands.Command('pbs_traits', command_type=sims4.commands.CommandType.Live)
def pbs_traits(_connection=None):
    # Get the console output
    output = sims4.commands.CheatOutput(_connection)

    # Get the sim_info for the active sim
    sim = services.client_manager().get(_connection).active_sim.sim_info

    # Get the tuned trait instance from the tuning instance manager
    instance_manager = services.get_instance_manager(Types.TRAIT)
    t_active = instance_manager.get(get_resource_key(T_ACTIVE, Types.TRAIT))
    t_adventurous = instance_manager.get(get_resource_key(T_ADVENTUROUS, Types.TRAIT))
    t_alluring = instance_manager.get(get_resource_key(T_ALLURING, Types.TRAIT))
    t_alwayswelcome = instance_manager.get(get_resource_key(T_ALWAYSWELCOME, Types.TRAIT))
    t_ambitious = instance_manager.get(get_resource_key(T_AMBITIOUS, Types.TRAIT))
    t_angler = instance_manager.get(get_resource_key(T_ANGLER, Types.TRAIT))
    t_animalattraction = instance_manager.get(get_resource_key(T_ANIMALATTRACT, Types.TRAIT))
    t_animalenthusiast = instance_manager.get(get_resource_key(T_ANIMALENTHUSIAST, Types.TRAIT))
    t_animalwhisperer = instance_manager.get(get_resource_key(T_ANIMALWHISPERER, Types.TRAIT))
    t_antiseptic = instance_manager.get(get_resource_key(T_ANTISEPTIC, Types.TRAIT))
    t_appraiser = instance_manager.get(get_resource_key(T_APPRAISER, Types.TRAIT))
    t_artlover = instance_manager.get(get_resource_key(T_ARTLOVER, Types.TRAIT))
    t_beguling = instance_manager.get(get_resource_key(T_BEGULING, Types.TRAIT))
    t_bookworm = instance_manager.get(get_resource_key(T_BOOKWORM, Types.TRAIT))
    t_brave = instance_manager.get(get_resource_key(T_BRAVE, Types.TRAIT))
    t_bro = instance_manager.get(get_resource_key(T_BRO, Types.TRAIT))
    t_businesssavvy = instance_manager.get(get_resource_key(T_BUSINESSSAVVY, Types.TRAIT))
    t_careerminded = instance_manager.get(get_resource_key(T_CAREERMINDED, Types.TRAIT))
    t_carefree = instance_manager.get(get_resource_key(T_CAREFREE, Types.TRAIT))
    t_catlover = instance_manager.get(get_resource_key(T_CATLOVER, Types.TRAIT))
    t_champofpeople = instance_manager.get(get_resource_key(T_CHAMPOFPEOPLE, Types.TRAIT))
    t_crooner = instance_manager.get(get_resource_key(T_CHARISMATICCROONER, Types.TRAIT))
    t_cheerful = instance_manager.get(get_resource_key(T_CHEERFUL, Types.TRAIT))
    t_childish = instance_manager.get(get_resource_key(T_CHILDISH, Types.TRAIT))
    t_childofocean = instance_manager.get(get_resource_key(T_CHILDOFOCEAN, Types.TRAIT))
    t_chopsticks = instance_manager.get(get_resource_key(T_CHOPSTICKS, Types.TRAIT))
    t_chronicler = instance_manager.get(get_resource_key(T_CHRONICLER, Types.TRAIT))
    t_clumsy = instance_manager.get(get_resource_key(T_CLUMSY, Types.TRAIT))
    t_collector = instance_manager.get(get_resource_key(T_COLLECTOR, Types.TRAIT))
    t_commitmentissues = instance_manager.get(get_resource_key(T_COMMITMENTISSUES, Types.TRAIT))
    t_connections = instance_manager.get(get_resource_key(T_CONNECTIONS, Types.TRAIT))
    t_creative = instance_manager.get(get_resource_key(T_CREATIVE, Types.TRAIT))
    t_creativelygifted = instance_manager.get(get_resource_key(T_CREATIVELYGIFTED, Types.TRAIT))
    t_creativevisionary = instance_manager.get(get_resource_key(T_CREATIVEVISIONARY, Types.TRAIT))
    t_dancemachine = instance_manager.get(get_resource_key(T_DANCEMACHINE, Types.TRAIT))
    t_dastardly = instance_manager.get(get_resource_key(T_DASTARDLY, Types.TRAIT))
    t_dauntless = instance_manager.get(get_resource_key(T_DAUNTLESS, Types.TRAIT))
    t_doglover = instance_manager.get(get_resource_key(T_DOGLOVER, Types.TRAIT))
    t_ecoengineer = instance_manager.get(get_resource_key(T_ECOENGINEER, Types.TRAIT))
    t_ecomaster = instance_manager.get(get_resource_key(T_ECOMASTER, Types.TRAIT))
    t_entrepreneur = instance_manager.get(get_resource_key(T_ENTREPRENEUR, Types.TRAIT))
    t_entrepreneurial = instance_manager.get(get_resource_key(T_ENTREPRENEURIAL, Types.TRAIT))
    t_epicpoet = instance_manager.get(get_resource_key(T_EPICPOET, Types.TRAIT))
    t_essenceofflavor = instance_manager.get(get_resource_key(T_ESSENCEOFFLAVOR, Types.TRAIT))
    t_eternalbond = instance_manager.get(get_resource_key(T_ETERNALBOND, Types.TRAIT))
    t_evil = instance_manager.get(get_resource_key(T_EVIL, Types.TRAIT))
    t_expressionistic = instance_manager.get(get_resource_key(T_EXPRESSIONISTIC, Types.TRAIT))
    t_fakegenius = instance_manager.get(get_resource_key(T_FAKEGENIUS, Types.TRAIT))
    t_familyoriented = instance_manager.get(get_resource_key(T_FAMILYORIENT, Types.TRAIT))
    t_familysim = instance_manager.get(get_resource_key(T_FAMILYSIM, Types.TRAIT))
    t_fastfastidious = instance_manager.get(get_resource_key(T_FASTFASTIDIOUS, Types.TRAIT))
    t_fertile = instance_manager.get(get_resource_key(T_FERTILE, Types.TRAIT))
    t_filthdweller = instance_manager.get(get_resource_key(T_FILTHDWELLER, Types.TRAIT))
    t_fizzyhead = instance_manager.get(get_resource_key(T_FIZZYHEAD, Types.TRAIT))
    t_foodie = instance_manager.get(get_resource_key(T_FOODIE, Types.TRAIT))
    t_foreverfresh = instance_manager.get(get_resource_key(T_FOREVERFRESH, Types.TRAIT))
    t_foreverfull = instance_manager.get(get_resource_key(T_FOREVERFULL, Types.TRAIT))
    t_freegan = instance_manager.get(get_resource_key(T_FREEGAN, Types.TRAIT))
    t_freeservices = instance_manager.get(get_resource_key(T_FREESERVICES, Types.TRAIT))
    t_freshchef = instance_manager.get(get_resource_key(T_FRESHCHEF, Types.TRAIT))
    t_friendofsea = instance_manager.get(get_resource_key(T_FRIENDOFSEA, Types.TRAIT))
    t_frugal = instance_manager.get(get_resource_key(T_FRUGAL, Types.TRAIT))
    t_geek = instance_manager.get(get_resource_key(T_GEEK, Types.TRAIT))
    t_genius = instance_manager.get(get_resource_key(T_GENIUS, Types.TRAIT))
    t_gloomy = instance_manager.get(get_resource_key(T_GLOOMY, Types.TRAIT))
    t_glutton = instance_manager.get(get_resource_key(T_GLUTTON, Types.TRAIT))
    t_good = instance_manager.get(get_resource_key(T_GOOD, Types.TRAIT))
    t_goofball = instance_manager.get(get_resource_key(T_GOOFBALL, Types.TRAIT))
    t_goodstories = instance_manager.get(get_resource_key(T_GOODSTRORIES, Types.TRAIT))
    t_gschoola = instance_manager.get(get_resource_key(T_GSCHOOLA, Types.TRAIT))
    t_gschoolb = instance_manager.get(get_resource_key(T_GSCHOOLB, Types.TRAIT))
    t_gschoolc = instance_manager.get(get_resource_key(T_GSCHOOLC, Types.TRAIT))
    t_gschoold = instance_manager.get(get_resource_key(T_GSCHOOLD, Types.TRAIT))
    t_gschoolf = instance_manager.get(get_resource_key(T_GSCHOOLF, Types.TRAIT))
    t_greatkisser = instance_manager.get(get_resource_key(T_GREATKISSER, Types.TRAIT))
    t_greenfiend = instance_manager.get(get_resource_key(T_GREENFIEND, Types.TRAIT))
    t_gregarious = instance_manager.get(get_resource_key(T_GREGARIOUS, Types.TRAIT))
    t_gymrat = instance_manager.get(get_resource_key(T_GYMRAT, Types.TRAIT))
    t_happytoddler = instance_manager.get(get_resource_key(T_HAPPYTODDLER, Types.TRAIT))
    t_hardlyhungry = instance_manager.get(get_resource_key(T_HARDLYHUNGRY, Types.TRAIT))
    t_hateschildren = instance_manager.get(get_resource_key(T_HATESCHILDREN, Types.TRAIT))
    t_heatproof = instance_manager.get(get_resource_key(T_HEATPROOF, Types.TRAIT))
    t_heroicpresence = instance_manager.get(get_resource_key(T_HEROICPRESENCE, Types.TRAIT))
    t_heroofstrange = instance_manager.get(get_resource_key(T_HEROOFSTRANGE, Types.TRAIT))
    t_highereducation = instance_manager.get(get_resource_key(T_HIGHEREDUCATION, Types.TRAIT))
    t_highflier = instance_manager.get(get_resource_key(T_HIGHFLIER, Types.TRAIT))
    t_highmaintenance = instance_manager.get(get_resource_key(T_HIGHMAINT, Types.TRAIT))
    t_highmetab = instance_manager.get(get_resource_key(T_HIGHMET, Types.TRAIT))
    t_hilarious = instance_manager.get(get_resource_key(T_HILARIOUS, Types.TRAIT))
    t_hometurf = instance_manager.get(get_resource_key(T_HOMETURF, Types.TRAIT))
    t_hotheaded = instance_manager.get(get_resource_key(T_HOTHEADED, Types.TRAIT))
    t_hschoola = instance_manager.get(get_resource_key(T_HSCHOOLA, Types.TRAIT))
    t_hschoolb = instance_manager.get(get_resource_key(T_HSCHOOLB, Types.TRAIT))
    t_hschoolc = instance_manager.get(get_resource_key(T_HSCHOOLC, Types.TRAIT))
    t_hschoold = instance_manager.get(get_resource_key(T_HSCHOOLD, Types.TRAIT))
    t_hschoolf = instance_manager.get(get_resource_key(T_HSCHOOLF, Types.TRAIT))
    t_hsexit_dropout = instance_manager.get(get_resource_key(T_HSEXIT_DROPOUT, Types.TRAIT))
    t_hsexit_earnedged = instance_manager.get(get_resource_key(T_HSEXIT_EARNEDGED, Types.TRAIT))
    t_hsexit_expel = instance_manager.get(get_resource_key(T_HSEXIT_EXPEL, Types.TRAIT))
    t_hsexit_early = instance_manager.get(get_resource_key(T_HSEXIT_EARLY, Types.TRAIT))
    t_hsexit_honors = instance_manager.get(get_resource_key(T_HSEXIT_HONORS, Types.TRAIT))
    t_hsexit_valedictorian = instance_manager.get(get_resource_key(T_HSEXIT_VALEDICT, Types.TRAIT))
    t_hsteamrewardcheer = instance_manager.get(get_resource_key(T_HSTEAMCHEERREWARD, Types.TRAIT))
    t_hsteamrewardchess = instance_manager.get(get_resource_key(T_HSTEAMCHESSREWARD, Types.TRAIT))
    t_hsteamrewardcomp = instance_manager.get(get_resource_key(T_HSTEAMCOMPREWARD, Types.TRAIT))
    t_hsteamrewardfootb = instance_manager.get(get_resource_key(T_HSTEAMFOOTBALLREWARD, Types.TRAIT))
    t_iceproof = instance_manager.get(get_resource_key(T_ICEPROOF, Types.TRAIT))
    t_iconic = instance_manager.get(get_resource_key(T_ICONIC, Types.TRAIT))
    t_incrediblyfriendly = instance_manager.get(get_resource_key(T_INCREDFRIENDLY, Types.TRAIT))
    t_independent = instance_manager.get(get_resource_key(T_INDEPENDENT, Types.TRAIT))
    t_influential = instance_manager.get(get_resource_key(T_INFLUENTIALINDIVIDUAL, Types.TRAIT))
    t_insane = instance_manager.get(get_resource_key(T_INSANE, Types.TRAIT))
    t_insider = instance_manager.get(get_resource_key(T_INSIDER, Types.TRAIT))
    t_inspiredexplorer = instance_manager.get(get_resource_key(T_INSPIREDEXPLORER, Types.TRAIT))
    t_intheknow = instance_manager.get(get_resource_key(T_INTHEKNOW, Types.TRAIT))
    t_invested = instance_manager.get(get_resource_key(T_INVESTED, Types.TRAIT))
    t_jealous = instance_manager.get(get_resource_key(T_JEALOUS, Types.TRAIT))
    t_kindnessambasador = instance_manager.get(get_resource_key(T_KINDNESSAMB, Types.TRAIT))
    t_klepto = instance_manager.get(get_resource_key(T_KLEPTO, Types.TRAIT))
    t_lactoseintol = instance_manager.get(get_resource_key(T_LACTOSEINTOLERANT, Types.TRAIT))
    t_lazy = instance_manager.get(get_resource_key(T_LAZY, Types.TRAIT))
    t_legendary = instance_manager.get(get_resource_key(T_LEGENDARY, Types.TRAIT))
    t_legendarystamina = instance_manager.get(get_resource_key(T_LEGENDARYSTAMINA, Types.TRAIT))
    t_livingvicariously = instance_manager.get(get_resource_key(T_LIVINGVICARIOUS, Types.TRAIT))
    t_loner = instance_manager.get(get_resource_key(T_LONER, Types.TRAIT))
    t_longevity = instance_manager.get(get_resource_key(T_LONGEVITY, Types.TRAIT))
    t_lovesoutdoors = instance_manager.get(get_resource_key(T_LOVESOUTDOORS, Types.TRAIT))
    t_lskill_argumentative = instance_manager.get(get_resource_key(T_LSKILL_ARGUMENTATIVE, Types.TRAIT))
    t_lskill_badmanners = instance_manager.get(get_resource_key(T_LSKILL_BADMANNERS, Types.TRAIT))
    t_lskill_compassionate = instance_manager.get(get_resource_key(T_LSKILL_COMPASSIONATE, Types.TRAIT))
    t_lskill_emotionalcontrol = instance_manager.get(get_resource_key(T_LSKILL_EMOTIONALCONTROL, Types.TRAIT))
    t_lskill_goodmanners = instance_manager.get(get_resource_key(T_LSKILL_GOODMANNERS, Types.TRAIT))
    t_lskill_irresponsible = instance_manager.get(get_resource_key(T_LSKILL_IRRESPONSIBLE, Types.TRAIT))
    t_lskill_mediator = instance_manager.get(get_resource_key(T_LSKILL_MEDIATOR, Types.TRAIT))
    t_lskill_responsible = instance_manager.get(get_resource_key(T_LSKILL_RESPONSIBLE, Types.TRAIT))
    t_lskill_uncontrolledemotion = instance_manager.get(get_resource_key(T_LSKILL_UNCONTROLEMOTION, Types.TRAIT))
    t_lskill_unfeeling = instance_manager.get(get_resource_key(T_LSKILL_UNFEELING, Types.TRAIT))
    t_maker = instance_manager.get(get_resource_key(T_MAKER, Types.TRAIT))
    t_marketable = instance_manager.get(get_resource_key(T_MARKETABLE, Types.TRAIT))
    t_mastermaker = instance_manager.get(get_resource_key(T_MASTERMAKER, Types.TRAIT))
    t_mastermind = instance_manager.get(get_resource_key(T_MASTERMIND, Types.TRAIT))
    t_mastermixer = instance_manager.get(get_resource_key(T_MASTERMIXER, Types.TRAIT))
    t_materialistic = instance_manager.get(get_resource_key(T_MATERIALISTIC, Types.TRAIT))
    t_mean = instance_manager.get(get_resource_key(T_MEAN, Types.TRAIT))
    t_meltmaster = instance_manager.get(get_resource_key(T_MELTMASTER, Types.TRAIT))
    t_memorable = instance_manager.get(get_resource_key(T_MEMORABLE, Types.TRAIT))
    t_mentallygifted = instance_manager.get(get_resource_key(T_MENTALLYGIFTED, Types.TRAIT))
    t_mentor = instance_manager.get(get_resource_key(T_MENTOR, Types.TRAIT))
    t_morningperson = instance_manager.get(get_resource_key(T_MORNINGPERSON, Types.TRAIT))
    t_mountaineer3 = instance_manager.get(get_resource_key(T_MOUNTAINEER3, Types.TRAIT))
    t_muser = instance_manager.get(get_resource_key(T_MUSER, Types.TRAIT))
    t_museumpatron = instance_manager.get(get_resource_key(T_MUSEUMPATRON, Types.TRAIT))
    t_musiclover = instance_manager.get(get_resource_key(T_MUSICLOVER, Types.TRAIT))
    t_naturalspeaker = instance_manager.get(get_resource_key(T_NATURALSPEAKER, Types.TRAIT))
    t_neat = instance_manager.get(get_resource_key(T_NEAT, Types.TRAIT))
    t_needsnoone = instance_manager.get(get_resource_key(T_NEEDSNOONE, Types.TRAIT))
    t_neverweary = instance_manager.get(get_resource_key(T_NEVERWEARY, Types.TRAIT))
    t_nightowl = instance_manager.get(get_resource_key(T_NIGHTOWL, Types.TRAIT))
    t_observant = instance_manager.get(get_resource_key(T_OBSERVANT, Types.TRAIT))
    t_onewithnature = instance_manager.get(get_resource_key(T_ONEWITHNATURE, Types.TRAIT))
    t_outgoing = instance_manager.get(get_resource_key(T_OUTGOING, Types.TRAIT))
    t_overachiever = instance_manager.get(get_resource_key(T_OVERACHIEVER, Types.TRAIT))
    t_overachievernew = instance_manager.get(get_resource_key(T_OVERACHIEVERNEW, Types.TRAIT))
    t_pamatriarch = instance_manager.get(get_resource_key(T_PAMATRIARCH, Types.TRAIT))
    t_paranoid = instance_manager.get(get_resource_key(T_PARANOID, Types.TRAIT))
    t_paranormallicense = instance_manager.get(get_resource_key(T_PARANORMLICENSE, Types.TRAIT))
    t_partyanimal = instance_manager.get(get_resource_key(T_PARTYANIMAL, Types.TRAIT))
    t_perfecthost = instance_manager.get(get_resource_key(T_PERFECTHOST, Types.TRAIT))
    t_perfectionist = instance_manager.get(get_resource_key(T_PERFECTIONIST, Types.TRAIT))
    t_physicallygifted = instance_manager.get(get_resource_key(T_PHYSICALLYGIFTED, Types.TRAIT))
    t_piper = instance_manager.get(get_resource_key(T_PIPER, Types.TRAIT))
    t_player = instance_manager.get(get_resource_key(T_PLAYER, Types.TRAIT))
    t_potionmaster = instance_manager.get(get_resource_key(T_POTIONMASTER, Types.TRAIT))
    t_prankster = instance_manager.get(get_resource_key(T_PRANKSTER, Types.TRAIT))
    t_preparedvoyager = instance_manager.get(get_resource_key(T_PREPAREDVOYAGER, Types.TRAIT))
    t_professionalslacker = instance_manager.get(get_resource_key(T_PROFSLACKER, Types.TRAIT))
    t_proper = instance_manager.get(get_resource_key(T_PROPER, Types.TRAIT))
    t_quicklearner = instance_manager.get(get_resource_key(T_QUICKLEARNER, Types.TRAIT))
    t_recycledisciple = instance_manager.get(get_resource_key(T_RECYCLEDISCIPLE, Types.TRAIT))
    t_regainedhumanity = instance_manager.get(get_resource_key(T_REGAINEDHUMANITY, Types.TRAIT))
    t_relatable = instance_manager.get(get_resource_key(T_RELATABLE, Types.TRAIT))
    t_reprankpristine = instance_manager.get(get_resource_key(T_REPRANK7PRISTINE, Types.TRAIT))
    t_rolemodel = instance_manager.get(get_resource_key(T_ROLEMODEL, Types.TRAIT))
    t_romantic = instance_manager.get(get_resource_key(T_ROMANTIC, Types.TRAIT))
    t_sacredknitknowledge = instance_manager.get(get_resource_key(T_SACREDKNITKNOWLEDGE, Types.TRAIT))
    t_savant = instance_manager.get(get_resource_key(T_SAVANT, Types.TRAIT))
    t_scoutingaptitude = instance_manager.get(get_resource_key(T_SCOUTINGAPTITUDE, Types.TRAIT))
    t_seasonedgamer = instance_manager.get(get_resource_key(T_SEASONEDGAMER, Types.TRAIT))
    t_seldomsleepy = instance_manager.get(get_resource_key(T_SELDOMSLEEPY, Types.TRAIT))
    t_selfabsorbed = instance_manager.get(get_resource_key(T_SELFABSORBED, Types.TRAIT))
    t_selfassured = instance_manager.get(get_resource_key(T_SELFASSURED, Types.TRAIT))
    t_shameless = instance_manager.get(get_resource_key(T_SHAMELESS, Types.TRAIT))
    t_sicknessimmunity = instance_manager.get(get_resource_key(T_SICKNESSIMMUNITY, Types.TRAIT))
    t_sincere = instance_manager.get(get_resource_key(T_SINCERE, Types.TRAIT))
    t_slingerofspells = instance_manager.get(get_resource_key(T_SLINGEROFSPELLS, Types.TRAIT))
    t_slob = instance_manager.get(get_resource_key(T_SLOB, Types.TRAIT))
    t_snob = instance_manager.get(get_resource_key(T_SNOB, Types.TRAIT))
    t_snowhate = instance_manager.get(get_resource_key(T_SNOWHATE, Types.TRAIT))
    t_snowlove = instance_manager.get(get_resource_key(T_SNOWLOVE, Types.TRAIT))
    t_sociallyawkward = instance_manager.get(get_resource_key(T_SOCIALLYAWKWARD, Types.TRAIT))
    t_sociallygifted = instance_manager.get(get_resource_key(T_SOCIALLYGIFTED, Types.TRAIT))
    t_speedcleaner = instance_manager.get(get_resource_key(T_SPEEDCLEANER, Types.TRAIT))
    t_speedreader = instance_manager.get(get_resource_key(T_SPEEDREADER, Types.TRAIT))
    t_spicehound = instance_manager.get(get_resource_key(T_SPICEHOUND, Types.TRAIT))
    t_squemish = instance_manager.get(get_resource_key(T_SQUEMISH, Types.TRAIT))
    t_steelbladder = instance_manager.get(get_resource_key(T_STEELBLADDER, Types.TRAIT))
    t_stormchaser = instance_manager.get(get_resource_key(T_STORMCHASER, Types.TRAIT))
    t_stovesandgrillmaster = instance_manager.get(get_resource_key(T_STOVESGRILLSMASTER, Types.TRAIT))
    t_supergreenthumb = instance_manager.get(get_resource_key(T_SUPERGREENTHUMB, Types.TRAIT))
    t_supremeauthority = instance_manager.get(get_resource_key(T_SUPREMEAUTHORITY, Types.TRAIT))
    t_survivalinstinct = instance_manager.get(get_resource_key(T_SURVIVALINSTINCT, Types.TRAIT))
    t_survivalist = instance_manager.get(get_resource_key(T_SURVIVALIST, Types.TRAIT))
    t_theknack = instance_manager.get(get_resource_key(T_THEKNACK, Types.TRAIT))
    t_theknowledge = instance_manager.get(get_resource_key(T_THEKNOWLEDGE, Types.TRAIT))
    t_themaster = instance_manager.get(get_resource_key(T_THEMASTER, Types.TRAIT))
    t_toddler_angelic = instance_manager.get(get_resource_key(T_TODDLER_ANGELIC, Types.TRAIT))
    t_toddler_charmer = instance_manager.get(get_resource_key(T_TODDLER_CHARMER, Types.TRAIT))
    t_toddler_clingy = instance_manager.get(get_resource_key(T_TODDLER_CLINGY, Types.TRAIT))
    t_toddler_fussy = instance_manager.get(get_resource_key(T_TODDLER_FUSSY, Types.TRAIT))
    t_toddler_independent = instance_manager.get(get_resource_key(T_TODDLER_INDEPENDENT, Types.TRAIT))
    t_toddler_inquisitive = instance_manager.get(get_resource_key(T_TODDLER_INQUISITIVE, Types.TRAIT))
    t_toddler_silly = instance_manager.get(get_resource_key(T_TODDLER_SILLY, Types.TRAIT))
    t_toddler_wild = instance_manager.get(get_resource_key(T_TODDLER_WILD, Types.TRAIT))
    t_toddler_topnotch = instance_manager.get(get_resource_key(T_TODDLER_TOPNOTCH, Types.TRAIT))
    t_treasurehunter = instance_manager.get(get_resource_key(T_TREASUREHUNTER, Types.TRAIT))
    t_treasurehunterbg = instance_manager.get(get_resource_key(T_TREASUREHUNTERBG, Types.TRAIT))
    t_truemaster = instance_manager.get(get_resource_key(T_TRUEMASTER, Types.TRAIT))
    t_unflirty = instance_manager.get(get_resource_key(T_UNFLIRTY, Types.TRAIT))
    t_overclock = instance_manager.get(get_resource_key(T_UNLOCKEDOVERCLOCK, Types.TRAIT))
    t_unstoppablefame = instance_manager.get(get_resource_key(T_UNSTOPFAME, Types.TRAIT))
    t_untroubled = instance_manager.get(get_resource_key(T_UNTROUBLED, Types.TRAIT))
    t_valuedcustomer = instance_manager.get(get_resource_key(T_VALUEDCUSTOMER, Types.TRAIT))
    t_vegetarian = instance_manager.get(get_resource_key(T_VEGETARIAN, Types.TRAIT))
    t_waterproof = instance_manager.get(get_resource_key(T_WATERPROOF, Types.TRAIT))
    t_webmaster = instance_manager.get(get_resource_key(T_WEBMASTER, Types.TRAIT))
    t_worldlyknowledge = instance_manager.get(get_resource_key(T_WORDLYKNOWLEDGE, Types.TRAIT))
    t_renownedactor = instance_manager.get(get_resource_key(T_WORLDRENOWNEDACTOR, Types.TRAIT))
    t_calmingaura = instance_manager.get(get_resource_key(T_WELLNESS_CALMINGAURA, Types.TRAIT))
    t_clearperspective = instance_manager.get(get_resource_key(T_WELLNESS_CLEARPERSPEC, Types.TRAIT))
    t_momentofclarity = instance_manager.get(get_resource_key(T_WELLNESS_MOMENTOFCLARITY, Types.TRAIT))
    t_selfcareexpert = instance_manager.get(get_resource_key(T_WELLNESS_SELFCAREEXPERTISE, Types.TRAIT))
    t_spamember = instance_manager.get(get_resource_key(T_WELLNESS_SPAMEMBER, Types.TRAIT))

    t_customgender = instance_manager.get(get_resource_key(T_PREG_CUSTOM, Types.TRAIT))
    t_romfemale = instance_manager.get(get_resource_key(T_ROM_ATTFEMALE, Types.TRAIT))
    t_rommale = instance_manager.get(get_resource_key(T_ROM_ATTMALE, Types.TRAIT))
    t_romnotfemale = instance_manager.get(get_resource_key(T_ROM_ATTNOTFEMALE, Types.TRAIT))
    t_romnotmale = instance_manager.get(get_resource_key(T_ROM_ATTNOTMALE, Types.TRAIT))
    t_romexplore = instance_manager.get(get_resource_key(T_ROM_EXPLORING, Types.TRAIT))
    t_romnotexplore = instance_manager.get(get_resource_key(T_ROM_NOTEXPLORING, Types.TRAIT))
    t_canbeimpregnated = instance_manager.get(get_resource_key(T_PREG_CANBEIMREGNATED, Types.TRAIT))
    t_canimpgregnate = instance_manager.get(get_resource_key(T_PREG_CANIMPREGNATE, Types.TRAIT))
    t_woohoofemale = instance_manager.get(get_resource_key(T_WOOHOO_FEMALE, Types.TRAIT))
    t_woohoomale = instance_manager.get(get_resource_key(T_WOOHOO_MALE, Types.TRAIT))
    t_woohoonotfemale = instance_manager.get(get_resource_key(T_WOOHOO_NOTFEMALE, Types.TRAIT))
    t_woohoonotmale = instance_manager.get(get_resource_key(T_WOOHOO_NOTMALE, Types.TRAIT))

    t_toddler = instance_manager.get(get_resource_key(T_TODDLER, Types.TRAIT))
    t_child = instance_manager.get(get_resource_key(T_CHILD, Types.TRAIT))
    t_teen = instance_manager.get(get_resource_key(T_TEEN, Types.TRAIT))
    t_yadult = instance_manager.get(get_resource_key(T_YADULT, Types.TRAIT))
    t_adult = instance_manager.get(get_resource_key(T_ADULT, Types.TRAIT))
    t_elder = instance_manager.get(get_resource_key(T_ELDER, Types.TRAIT))

    t_female = instance_manager.get(get_resource_key(T_FEMALE, Types.TRAIT))
    t_male = instance_manager.get(get_resource_key(T_MALE, Types.TRAIT))

    t_adulterer = instance_manager.get(get_resource_key(T_WW_ADULTERER, Types.TRAIT))
    t_antisocial = instance_manager.get(get_resource_key(T_WW_ANTISOCIAL, Types.TRAIT))
    t_cuck = instance_manager.get(get_resource_key(T_WW_CUCKOLD, Types.TRAIT))
    t_cumslut = instance_manager.get(get_resource_key(T_WW_CUMSLUT, Types.TRAIT))
    t_noeyebrown = instance_manager.get(get_resource_key(T_WW_DISLIKE_EYE_BROWN, Types.TRAIT))
    t_noeyeunnatural = instance_manager.get(get_resource_key(T_WW_DISLIKE_EYE_UNNATURAL, Types.TRAIT))
    t_noblackhair = instance_manager.get(get_resource_key(T_WW_DISLIKE_HAIR_BLACK, Types.TRAIT))
    t_nobluehair = instance_manager.get(get_resource_key(T_WW_DISLIKE_HAIR_BLUE, Types.TRAIT))
    t_nogreenhair = instance_manager.get(get_resource_key(T_WW_DISLIKE_HAIR_GREEN, Types.TRAIT))
    t_nopinkhair = instance_manager.get(get_resource_key(T_WW_DISLIKE_HAIR_PINK, Types.TRAIT))
    t_nofat = instance_manager.get(get_resource_key(T_WW_DISLIKE_FAT, Types.TRAIT))
    t_nolargebreasts = instance_manager.get(get_resource_key(T_WW_DISLIKE_BREASTS, Types.TRAIT))
    t_nobigbutt = instance_manager.get(get_resource_key(T_WW_DISLIKE_BUTT, Types.TRAIT))
    t_nofemales = instance_manager.get(get_resource_key(T_WW_DISLIKE_FEMALE, Types.TRAIT))
    t_nomales = instance_manager.get(get_resource_key(T_WW_DISLIKE_MALE, Types.TRAIT))
    t_absorbancy = instance_manager.get(get_resource_key(T_WW_EXTRAABSORB, Types.TRAIT))
    t_genlover = instance_manager.get(get_resource_key(T_WW_GENLOVER, Types.TRAIT))
    t_incest = instance_manager.get(get_resource_key(T_WW_INCEST, Types.TRAIT))
    t_likeblondes = instance_manager.get(get_resource_key(T_WW_HAIR_BLONDE, Types.TRAIT))
    t_likebrunettes = instance_manager.get(get_resource_key(T_WW_HAIR_BROWN, Types.TRAIT))
    t_likeredheads = instance_manager.get(get_resource_key(T_WW_HAIR_RED, Types.TRAIT))
    t_beardlover = instance_manager.get(get_resource_key(T_WW_LIKESBEARD, Types.TRAIT))
    t_chubbychaser = instance_manager.get(get_resource_key(T_WW_LIKESFAT, Types.TRAIT))
    t_likegirls = instance_manager.get(get_resource_key(T_WW_LIKESFEMALES, Types.TRAIT))
    t_likefreckles = instance_manager.get(get_resource_key(T_WW_LIKESFRECKLES, Types.TRAIT))
    t_likehulk = instance_manager.get(get_resource_key(T_WW_LIKESHULK, Types.TRAIT))
    t_likejewelry = instance_manager.get(get_resource_key(T_WW_LIKESJEWELRY, Types.TRAIT))
    t_likemakeup = instance_manager.get(get_resource_key(T_WW_LIKESMAKEUP, Types.TRAIT))
    t_likeboys = instance_manager.get(get_resource_key(T_WW_LIKESMALES, Types.TRAIT))
    t_likeskinny = instance_manager.get(get_resource_key(T_WW_LIKESSKINNY, Types.TRAIT))
    t_likeflatchest = instance_manager.get(get_resource_key(T_WW_LIKESSMALLBREAST, Types.TRAIT))
    t_likeflatbutt = instance_manager.get(get_resource_key(T_WW_LIKESSMALLBUTT, Types.TRAIT))
    t_nounderwear = instance_manager.get(get_resource_key(T_WW_NOUNDERWEAR, Types.TRAIT))
    t_poly = instance_manager.get(get_resource_key(T_WW_POLY, Types.TRAIT))
    t_postpuberty = instance_manager.get(get_resource_key(T_WW_POSTPUBERTY, Types.TRAIT))
    t_sexuallyalluring = instance_manager.get(get_resource_key(T_WW_SEXUALLYALLURING, Types.TRAIT))

    if sim.has_trait(t_toddler) or sim.has_trait(t_child):
        output = sims4.commands.CheatOutput(_connection)
        output("Skipping WW traits as sim is a minor")

    # If teen or older, set gender and sexual orientation traits
    if sim.has_trait(t_teen) or sim.has_trait(t_adult) or sim.has_trait(t_yadult) or sim.has_trait(t_elder):
        if sim.has_trait(t_female):
            sim.add_trait(t_absorbancy)
            sim.add_trait(t_cumslut)
            sim.add_trait(t_nounderwear)

            sim.add_trait(t_beardlover)
            sim.add_trait(t_chubbychaser)
            sim.add_trait(t_likeboys)

            if not sim.has_trait(t_customgender):
                sim.add_trait(t_customgender)

            if sim.has_trait(t_canimpgregnate):
                sim.remove_trait(t_canimpgregnate)

            if not sim.has_trait(t_rommale):
                sim.add_trait(t_rommale)

            if sim.has_trait(t_romnotmale):
                sim.remove_trait(t_romnotmale)
                sim.add_trait(t_rommale)

            if sim.has_trait(t_woohoonotfemale):
                sim.remove_trait(t_woohoonotfemale)
                sim.add_trait(t_woohoofemale)

            if sim.has_trait(t_woohoonotmale):
                sim.remove_trait(t_woohoonotmale)
                sim.add_trait(t_woohoomale)

        if sim.has_trait(t_male):
            sim.add_trait(t_nomales)
            sim.add_trait(t_nofat)
            sim.add_trait(t_likemakeup)
            sim.add_trait(t_likeskinny)

            if sim.has_trait(t_canbeimpregnated):
                sim.remove_trait(t_canbeimpregnated)

            if sim.has_trait(t_woohoomale):
                sim.remove_trait(t_woohoomale)

            if not sim.has_trait(t_woohoonotmale):
                sim.add_trait(t_woohoonotmale)

        if sim.has_trait(t_romnotexplore):
            sim.remove_trait(t_romnotexplore)
            sim.add_trait(t_romexplore)

        if not sim.has_trait(t_romexplore):
            sim.add_trait(t_romexplore)

        if sim.has_trait(t_romnotfemale):
            sim.remove_trait(t_romnotfemale)
            sim.add_trait(t_romfemale)

        if not sim.has_trait(t_romfemale):
            sim.add_trait(t_romfemale)

        if not sim.has_trait(t_woohoofemale):
            sim.add_trait(t_woohoofemale)

        if sim.has_trait(t_teen):
            sim.add_trait(t_postpuberty)

        sim.add_trait(t_adulterer)
        sim.add_trait(t_antisocial)
        sim.add_trait(t_cuck)
        sim.add_trait(t_genlover)
        sim.add_trait(t_incest)
        sim.add_trait(t_poly)
        sim.add_trait(t_sexuallyalluring)

        sim.add_trait(t_nofemales)
        sim.add_trait(t_likegirls)

        sim.add_trait(t_noeyebrown)
        sim.add_trait(t_noeyeunnatural)
        sim.add_trait(t_noblackhair)
        sim.add_trait(t_nobluehair)
        sim.add_trait(t_nogreenhair)
        sim.add_trait(t_nopinkhair)
        sim.add_trait(t_nolargebreasts)
        sim.add_trait(t_nobigbutt)
        sim.add_trait(t_likeblondes)
        sim.add_trait(t_likebrunettes)
        sim.add_trait(t_likeredheads)
        sim.add_trait(t_likefreckles)
        sim.add_trait(t_likehulk)
        sim.add_trait(t_likejewelry)
        sim.add_trait(t_likeflatchest)
        sim.add_trait(t_likeflatbutt)
# Things above apply to teen or older

# Any age
    if sim.has_trait(t_female):
        if not sim.has_trait(t_alluring):
            sim.add_trait(t_alluring)

    if not sim.has_trait(t_active):
        sim.add_trait(t_active)

    if not sim.has_trait(t_adventurous):
        sim.add_trait(t_adventurous)

    if not sim.has_trait(t_alwayswelcome):
        sim.add_trait(t_alwayswelcome)

    if not sim.has_trait(t_ambitious):
        sim.add_trait(t_ambitious)

    if not sim.has_trait(t_angler):
        sim.add_trait(t_angler)

    if not sim.has_trait(t_animalattraction):
        sim.add_trait(t_animalattraction)

    if not sim.has_trait(t_animalenthusiast):
        sim.add_trait(t_animalenthusiast)

    if not sim.has_trait(t_animalwhisperer):
        sim.add_trait(t_animalwhisperer)

    if not sim.has_trait(t_antiseptic):
        sim.add_trait(t_antiseptic)

    if not sim.has_trait(t_appraiser):
        sim.add_trait(t_appraiser)

    if not sim.has_trait(t_artlover):
        sim.add_trait(t_artlover)

    if not sim.has_trait(t_beguling):
        sim.add_trait(t_beguling)

    if not sim.has_trait(t_bookworm):
        sim.add_trait(t_bookworm)

    if not sim.has_trait(t_brave):
        sim.add_trait(t_brave)

    if not sim.has_trait(t_bro):
        sim.add_trait(t_bro)

    if not sim.has_trait(t_businesssavvy):
        sim.add_trait(t_businesssavvy)

    if not sim.has_trait(t_careerminded):
        sim.add_trait(t_careerminded)

    if not sim.has_trait(t_carefree):
        sim.add_trait(t_carefree)

    if not sim.has_trait(t_catlover):
        sim.add_trait(t_catlover)

    if not sim.has_trait(t_champofpeople):
        sim.add_trait(t_champofpeople)

    if not sim.has_trait(t_crooner):
        sim.add_trait(t_crooner)

    if not sim.has_trait(t_cheerful):
        sim.add_trait(t_cheerful)

    if not sim.has_trait(t_childish):
        sim.add_trait(t_childish)

    if not sim.has_trait(t_childofocean):
        sim.add_trait(t_childofocean)

    if not sim.has_trait(t_chopsticks):
        sim.add_trait(t_chopsticks)

    if not sim.has_trait(t_chronicler):
        sim.add_trait(t_chronicler)

    if not sim.has_trait(t_clumsy):
        sim.add_trait(t_clumsy)

    if not sim.has_trait(t_collector):
        sim.add_trait(t_collector)

    if not sim.has_trait(t_commitmentissues):
        sim.add_trait(t_commitmentissues)

    if not sim.has_trait(t_connections):
        sim.add_trait(t_connections)

    if not sim.has_trait(t_creative):
        sim.add_trait(t_creative)

    if not sim.has_trait(t_creativelygifted):
        sim.add_trait(t_creativelygifted)

    if not sim.has_trait(t_creativevisionary):
        sim.add_trait(t_creativevisionary)

    if not sim.has_trait(t_dancemachine):
        sim.add_trait(t_dancemachine)

    if not sim.has_trait(t_dastardly):
        sim.add_trait(t_dastardly)

    if not sim.has_trait(t_dauntless):
        sim.add_trait(t_dauntless)

    if not sim.has_trait(t_doglover):
        sim.add_trait(t_doglover)

    if not sim.has_trait(t_ecoengineer):
        sim.add_trait(t_ecoengineer)

    if not sim.has_trait(t_ecomaster):
        sim.add_trait(t_ecomaster)

    if not sim.has_trait(t_entrepreneur):
        sim.add_trait(t_entrepreneur)

    if not sim.has_trait(t_entrepreneurial):
        sim.add_trait(t_entrepreneurial)

    if not sim.has_trait(t_epicpoet):
        sim.add_trait(t_epicpoet)

    if not sim.has_trait(t_essenceofflavor):
        sim.add_trait(t_essenceofflavor)

    if not sim.has_trait(t_eternalbond):
        sim.add_trait(t_eternalbond)

    if not sim.has_trait(t_evil):
        sim.add_trait(t_evil)

    if not sim.has_trait(t_expressionistic):
        sim.add_trait(t_expressionistic)

    if not sim.has_trait(t_fakegenius):
        sim.add_trait(t_fakegenius)

    if not sim.has_trait(t_familyoriented):
        sim.add_trait(t_familyoriented)

    if not sim.has_trait(t_familysim):
        sim.add_trait(t_familysim)

    if not sim.has_trait(t_fastfastidious):
        sim.add_trait(t_fastfastidious)

    if not sim.has_trait(t_fertile):
        sim.add_trait(t_fertile)

    if not sim.has_trait(t_filthdweller):
        sim.add_trait(t_filthdweller)

    if not sim.has_trait(t_fizzyhead):
        sim.add_trait(t_fizzyhead)

    if not sim.has_trait(t_foodie):
        sim.add_trait(t_foodie)

    if not sim.has_trait(t_foreverfresh):
        sim.add_trait(t_foreverfresh)

    if not sim.has_trait(t_foreverfull):
        sim.add_trait(t_foreverfull)

    if not sim.has_trait(t_freegan):
        sim.add_trait(t_freegan)

    if not sim.has_trait(t_freeservices):
        sim.add_trait(t_freeservices)

    if not sim.has_trait(t_freshchef):
        sim.add_trait(t_freshchef)

    if not sim.has_trait(t_friendofsea):
        sim.add_trait(t_friendofsea)

    if not sim.has_trait(t_frugal):
        sim.add_trait(t_frugal)

    if not sim.has_trait(t_geek):
        sim.add_trait(t_geek)

    if not sim.has_trait(t_genius):
        sim.add_trait(t_genius)

    if not sim.has_trait(t_gloomy):
        sim.add_trait(t_gloomy)

    if not sim.has_trait(t_glutton):
        sim.add_trait(t_glutton)

    if not sim.has_trait(t_good):
        sim.add_trait(t_good)

    if not sim.has_trait(t_goodstories):
        sim.add_trait(t_goodstories)

    if not sim.has_trait(t_goofball):
        sim.add_trait(t_goofball)

    if not sim.has_trait(t_gschoola):
        sim.add_trait(t_gschoola)

    if not sim.has_trait(t_gschoolb):
        sim.add_trait(t_gschoolb)

    if not sim.has_trait(t_gschoolc):
        sim.add_trait(t_gschoolc)

    if not sim.has_trait(t_gschoold):
        sim.add_trait(t_gschoold)

    if not sim.has_trait(t_gschoolf):
        sim.add_trait(t_gschoolf)

    if not sim.has_trait(t_greatkisser):
        sim.add_trait(t_greatkisser)

    if not sim.has_trait(t_greenfiend):
        sim.add_trait(t_greenfiend)

    if not sim.has_trait(t_gregarious):
        sim.add_trait(t_gregarious)

    if not sim.has_trait(t_gymrat):
        sim.add_trait(t_gymrat)

    if not sim.has_trait(t_happytoddler):
        sim.add_trait(t_happytoddler)

    if not sim.has_trait(t_hardlyhungry):
        sim.add_trait(t_hardlyhungry)

    if not sim.has_trait(t_hateschildren):
        sim.add_trait(t_hateschildren)

    if not sim.has_trait(t_heatproof):
        sim.add_trait(t_heatproof)

    if not sim.has_trait(t_heroicpresence):
        sim.add_trait(t_heroicpresence)

    if not sim.has_trait(t_heroofstrange):
        sim.add_trait(t_heroofstrange)

    if not sim.has_trait(t_highereducation):
        sim.add_trait(t_highereducation)

    if not sim.has_trait(t_highflier):
        sim.add_trait(t_highflier)

    if not sim.has_trait(t_highmaintenance):
        sim.add_trait(t_highmaintenance)

    if not sim.has_trait(t_highmetab):
        sim.add_trait(t_highmetab)

    if not sim.has_trait(t_hilarious):
        sim.add_trait(t_hilarious)

    if not sim.has_trait(t_hometurf):
        sim.add_trait(t_hometurf)

    if not sim.has_trait(t_hotheaded):
        sim.add_trait(t_hotheaded)

    if not sim.has_trait(t_hschoola):
        sim.add_trait(t_hschoola)

    if not sim.has_trait(t_hschoolb):
        sim.add_trait(t_hschoolb)

    if not sim.has_trait(t_hschoolc):
        sim.add_trait(t_hschoolc)

    if not sim.has_trait(t_hschoold):
        sim.add_trait(t_hschoold)

    if not sim.has_trait(t_hschoolf):
        sim.add_trait(t_hschoolf)

    if not sim.has_trait(t_hsexit_dropout):
        sim.add_trait(t_hsexit_dropout)

    if not sim.has_trait(t_hsexit_earnedged):
        sim.add_trait(t_hsexit_earnedged)

    if not sim.has_trait(t_hsexit_expel):
        sim.add_trait(t_hsexit_expel)

    if not sim.has_trait(t_hsexit_early):
        sim.add_trait(t_hsexit_early)

    if not sim.has_trait(t_hsexit_honors):
        sim.add_trait(t_hsexit_honors)

    if not sim.has_trait(t_hsexit_valedictorian):
        sim.add_trait(t_hsexit_valedictorian)

    if not sim.has_trait(t_hsteamrewardcheer):
        sim.add_trait(t_hsteamrewardcheer)

    if not sim.has_trait(t_hsteamrewardchess):
        sim.add_trait(t_hsteamrewardchess)

    if not sim.has_trait(t_hsteamrewardcomp):
        sim.add_trait(t_hsteamrewardcomp)

    if not sim.has_trait(t_hsteamrewardfootb):
        sim.add_trait(t_hsteamrewardfootb)

    if not sim.has_trait(t_iceproof):
        sim.add_trait(t_iceproof)

    if not sim.has_trait(t_iconic):
        sim.add_trait(t_iconic)

    if not sim.has_trait(t_incrediblyfriendly):
        sim.add_trait(t_incrediblyfriendly)

    if not sim.has_trait(t_independent):
        sim.add_trait(t_independent)

    if not sim.has_trait(t_influential):
        sim.add_trait(t_influential)

    if not sim.has_trait(t_insane):
        sim.add_trait(t_insane)

    if not sim.has_trait(t_insider):
        sim.add_trait(t_insider)

    if not sim.has_trait(t_inspiredexplorer):
        sim.add_trait(t_inspiredexplorer)

    if not sim.has_trait(t_intheknow):
        sim.add_trait(t_intheknow)

    if not sim.has_trait(t_invested):
        sim.add_trait(t_invested)

    if not sim.has_trait(t_jealous):
        sim.add_trait(t_jealous)

    if not sim.has_trait(t_kindnessambasador):
        sim.add_trait(t_kindnessambasador)

    if not sim.has_trait(t_klepto):
        sim.add_trait(t_klepto)

    if not sim.has_trait(t_lactoseintol):
        sim.add_trait(t_lactoseintol)

    if not sim.has_trait(t_lazy):
        sim.add_trait(t_lazy)

    if not sim.has_trait(t_legendary):
        sim.add_trait(t_legendary)

    if not sim.has_trait(t_legendarystamina):
        sim.add_trait(t_legendarystamina)

    if not sim.has_trait(t_livingvicariously):
        sim.add_trait(t_livingvicariously)

    if not sim.has_trait(t_loner):
        sim.add_trait(t_loner)

    if not sim.has_trait(t_longevity):
        sim.add_trait(t_longevity)

    if not sim.has_trait(t_lovesoutdoors):
        sim.add_trait(t_lovesoutdoors)

    if not sim.has_trait(t_lskill_argumentative):
        sim.add_trait(t_lskill_argumentative)

    if not sim.has_trait(t_lskill_badmanners):
        sim.add_trait(t_lskill_badmanners)

    if not sim.has_trait(t_lskill_compassionate):
        sim.add_trait(t_lskill_compassionate)

    if not sim.has_trait(t_lskill_emotionalcontrol):
        sim.add_trait(t_lskill_emotionalcontrol)

    if not sim.has_trait(t_lskill_goodmanners):
        sim.add_trait(t_lskill_goodmanners)

    if not sim.has_trait(t_lskill_irresponsible):
        sim.add_trait(t_lskill_irresponsible)

    if not sim.has_trait(t_lskill_mediator):
        sim.add_trait(t_lskill_mediator)

    if not sim.has_trait(t_lskill_responsible):
        sim.add_trait(t_lskill_responsible)

    if not sim.has_trait(t_lskill_uncontrolledemotion):
        sim.add_trait(t_lskill_uncontrolledemotion)

    if not sim.has_trait(t_lskill_unfeeling):
        sim.add_trait(t_lskill_unfeeling)

    if not sim.has_trait(t_maker):
        sim.add_trait(t_maker)

    if not sim.has_trait(t_marketable):
        sim.add_trait(t_marketable)

    if not sim.has_trait(t_mastermaker):
        sim.add_trait(t_mastermaker)

    if not sim.has_trait(t_mastermind):
        sim.add_trait(t_mastermind)

    if not sim.has_trait(t_mastermixer):
        sim.add_trait(t_mastermixer)

    if not sim.has_trait(t_materialistic):
        sim.add_trait(t_materialistic)

    if not sim.has_trait(t_mean):
        sim.add_trait(t_mean)

    if not sim.has_trait(t_meltmaster):
        sim.add_trait(t_meltmaster)

    if not sim.has_trait(t_memorable):
        sim.add_trait(t_memorable)

    if not sim.has_trait(t_mentallygifted):
        sim.add_trait(t_mentallygifted)

    if not sim.has_trait(t_mentor):
        sim.add_trait(t_mentor)

    if not sim.has_trait(t_morningperson):
        sim.add_trait(t_morningperson)

    if not sim.has_trait(t_mountaineer3):
        sim.add_trait(t_mountaineer3)

    if not sim.has_trait(t_muser):
        sim.add_trait(t_muser)

    if not sim.has_trait(t_museumpatron):
        sim.add_trait(t_museumpatron)

    if not sim.has_trait(t_musiclover):
        sim.add_trait(t_musiclover)

    if not sim.has_trait(t_naturalspeaker):
        sim.add_trait(t_naturalspeaker)

    if not sim.has_trait(t_neat):
        sim.add_trait(t_neat)

    if not sim.has_trait(t_needsnoone):
        sim.add_trait(t_needsnoone)

    if not sim.has_trait(t_neverweary):
        sim.add_trait(t_neverweary)

    if not sim.has_trait(t_nightowl):
        sim.add_trait(t_nightowl)

    if not sim.has_trait(t_observant):
        sim.add_trait(t_observant)

    if not sim.has_trait(t_onewithnature):
        sim.add_trait(t_onewithnature)

    if not sim.has_trait(t_outgoing):
        sim.add_trait(t_outgoing)

    if not sim.has_trait(t_overachiever):
        sim.add_trait(t_overachiever)

    if not sim.has_trait(t_overachievernew):
        sim.add_trait(t_overachievernew)

    if not sim.has_trait(t_pamatriarch):
        sim.add_trait(t_pamatriarch)

    if not sim.has_trait(t_paranoid):
        sim.add_trait(t_paranoid)

    if not sim.has_trait(t_paranormallicense):
        sim.add_trait(t_paranormallicense)

    if not sim.has_trait(t_partyanimal):
        sim.add_trait(t_partyanimal)

    if not sim.has_trait(t_perfecthost):
        sim.add_trait(t_perfecthost)

    if not sim.has_trait(t_perfectionist):
        sim.add_trait(t_perfectionist)

    if not sim.has_trait(t_physicallygifted):
        sim.add_trait(t_physicallygifted)

    if not sim.has_trait(t_piper):
        sim.add_trait(t_piper)

    if not sim.has_trait(t_player):
        sim.add_trait(t_player)

    if not sim.has_trait(t_potionmaster):
        sim.add_trait(t_potionmaster)

    if not sim.has_trait(t_prankster):
        sim.add_trait(t_prankster)

    if not sim.has_trait(t_preparedvoyager):
        sim.add_trait(t_preparedvoyager)

    if not sim.has_trait(t_professionalslacker):
        sim.add_trait(t_professionalslacker)

    if not sim.has_trait(t_proper):
        sim.add_trait(t_proper)

    if not sim.has_trait(t_quicklearner):
        sim.add_trait(t_quicklearner)

    if not sim.has_trait(t_recycledisciple):
        sim.add_trait(t_recycledisciple)

    if not sim.has_trait(t_regainedhumanity):
        sim.add_trait(t_regainedhumanity)

    if not sim.has_trait(t_relatable):
        sim.add_trait(t_relatable)

    if not sim.has_trait(t_reprankpristine):
        sim.add_trait(t_reprankpristine)

    if not sim.has_trait(t_rolemodel):
        sim.add_trait(t_rolemodel)

    if not sim.has_trait(t_romantic):
        sim.add_trait(t_romantic)

    if not sim.has_trait(t_sacredknitknowledge):
        sim.add_trait(t_sacredknitknowledge)

    if not sim.has_trait(t_savant):
        sim.add_trait(t_savant)

    if not sim.has_trait(t_scoutingaptitude):
        sim.add_trait(t_scoutingaptitude)

    if not sim.has_trait(t_seasonedgamer):
        sim.add_trait(t_seasonedgamer)

    if not sim.has_trait(t_seldomsleepy):
        sim.add_trait(t_seldomsleepy)

    if not sim.has_trait(t_selfabsorbed):
        sim.add_trait(t_selfabsorbed)

    if not sim.has_trait(t_selfassured):
        sim.add_trait(t_selfassured)

    if not sim.has_trait(t_shameless):
        sim.add_trait(t_shameless)

    if not sim.has_trait(t_sicknessimmunity):
        sim.add_trait(t_sicknessimmunity)

    if not sim.has_trait(t_sincere):
        sim.add_trait(t_sincere)

    if not sim.has_trait(t_slingerofspells):
        sim.add_trait(t_slingerofspells)

    if not sim.has_trait(t_slob):
        sim.add_trait(t_slob)

    if not sim.has_trait(t_snob):
        sim.add_trait(t_snob)

    if not sim.has_trait(t_snowhate):
        sim.add_trait(t_snowhate)

    if not sim.has_trait(t_snowlove):
        sim.add_trait(t_snowlove)

    if not sim.has_trait(t_sociallyawkward):
        sim.add_trait(t_sociallyawkward)

    if not sim.has_trait(t_sociallygifted):
        sim.add_trait(t_sociallygifted)

    if not sim.has_trait(t_speedcleaner):
        sim.add_trait(t_speedcleaner)

    if not sim.has_trait(t_speedreader):
        sim.add_trait(t_speedreader)

    if not sim.has_trait(t_spicehound):
        sim.add_trait(t_spicehound)

    if not sim.has_trait(t_squemish):
        sim.add_trait(t_squemish)

    if not sim.has_trait(t_steelbladder):
        sim.add_trait(t_steelbladder)

    if not sim.has_trait(t_stormchaser):
        sim.add_trait(t_stormchaser)

    if not sim.has_trait(t_stovesandgrillmaster):
        sim.add_trait(t_stovesandgrillmaster)

    if not sim.has_trait(t_supergreenthumb):
        sim.add_trait(t_supergreenthumb)

    if not sim.has_trait(t_supremeauthority):
        sim.add_trait(t_supremeauthority)

    if not sim.has_trait(t_survivalinstinct):
        sim.add_trait(t_survivalinstinct)

    if not sim.has_trait(t_survivalist):
        sim.add_trait(t_survivalist)

    if not sim.has_trait(t_theknack):
        sim.add_trait(t_theknack)

    if not sim.has_trait(t_theknowledge):
        sim.add_trait(t_theknowledge)

    if not sim.has_trait(t_themaster):
        sim.add_trait(t_themaster)

    if not sim.has_trait(t_toddler_angelic):
        sim.add_trait(t_toddler_angelic)

    if not sim.has_trait(t_toddler_charmer):
        sim.add_trait(t_toddler_charmer)

    if not sim.has_trait(t_toddler_clingy):
        sim.add_trait(t_toddler_clingy)

    if not sim.has_trait(t_toddler_fussy):
        sim.add_trait(t_toddler_fussy)

    if not sim.has_trait(t_toddler_independent):
        sim.add_trait(t_toddler_independent)

    if not sim.has_trait(t_toddler_inquisitive):
        sim.add_trait(t_toddler_inquisitive)

    if not sim.has_trait(t_toddler_silly):
        sim.add_trait(t_toddler_silly)

    if not sim.has_trait(t_toddler_topnotch):
        sim.add_trait(t_toddler_topnotch)

    if not sim.has_trait(t_toddler_wild):
        sim.add_trait(t_toddler_wild)

    if not sim.has_trait(t_treasurehunter):
        sim.add_trait(t_treasurehunter)

    if not sim.has_trait(t_treasurehunterbg):
        sim.add_trait(t_treasurehunterbg)

    if not sim.has_trait(t_truemaster):
        sim.add_trait(t_truemaster)

    if not sim.has_trait(t_unflirty):
        sim.add_trait(t_unflirty)

    if not sim.has_trait(t_overclock):
        sim.add_trait(t_overclock)

    if not sim.has_trait(t_unstoppablefame):
        sim.add_trait(t_unstoppablefame)

    if not sim.has_trait(t_untroubled):
        sim.add_trait(t_untroubled)

    if not sim.has_trait(t_valuedcustomer):
        sim.add_trait(t_valuedcustomer)

    if not sim.has_trait(t_vegetarian):
        sim.add_trait(t_vegetarian)

    if not sim.has_trait(t_waterproof):
        sim.add_trait(t_waterproof)

    if not sim.has_trait(t_webmaster):
        sim.add_trait(t_webmaster)

    if not sim.has_trait(t_worldlyknowledge):
        sim.add_trait(t_worldlyknowledge)

    if not sim.has_trait(t_renownedactor):
        sim.add_trait(t_renownedactor)

    if not sim.has_trait(t_calmingaura):
        sim.add_trait(t_calmingaura)

    if not sim.has_trait(t_clearperspective):
        sim.add_trait(t_clearperspective)

    if not sim.has_trait(t_momentofclarity):
        sim.add_trait(t_momentofclarity)

    if not sim.has_trait(t_selfcareexpert):
        sim.add_trait(t_selfcareexpert)

    if not sim.has_trait(t_spamember):
        sim.add_trait(t_spamember)


@sims4.commands.Command('pbs_wwtraits', command_type=sims4.commands.CommandType.Live)
def pbs_wwtraits(_connection=None):
    # Get the console output
    output = sims4.commands.CheatOutput(_connection)

    # Get the sim_info for the active sim
    sim = services.client_manager().get(_connection).active_sim.sim_info

    # Get the tuned trait instance from the tuning instance manager
    instance_manager = services.get_instance_manager(Types.TRAIT)
    t_teen = instance_manager.get(get_resource_key(T_TEEN, Types.TRAIT))
    t_female = instance_manager.get(get_resource_key(T_FEMALE, Types.TRAIT))
    T_cheater = instance_manager.get(get_resource_key(T_WW_ADULTERER, Types.TRAIT))
    T_cuck = instance_manager.get(get_resource_key(T_WW_CUCKOLD, Types.TRAIT))
    T_cumslut = instance_manager.get(get_resource_key(T_WW_CUMSLUT, Types.TRAIT))
    T_beardlove = instance_manager.get(get_resource_key(T_WW_LIKESBEARD, Types.TRAIT))
    T_poly = instance_manager.get(get_resource_key(T_WW_POLY, Types.TRAIT))
    T_absorbancy = instance_manager.get(get_resource_key(T_WW_EXTRAABSORB, Types.TRAIT))
    T_postpuberty = instance_manager.get(get_resource_key(T_WW_POSTPUBERTY, Types.TRAIT))

    if sim.has_trait(t_teen):
        sim.add_trait(T_postpuberty)

    if sim.has_trait(t_female):
        sim.add_trait(T_absorbancy)
        sim.add_trait(T_cumslut)
        sim.add_trait(T_beardlove)

    sim.add_trait(T_cheater)
    sim.add_trait(T_cuck)
    sim.add_trait(T_poly)



@sims4.commands.Command('pbs_maxskills', command_type=sims4.commands.CommandType.Live)
def pbs_maxskills(_connection=None):
    # Get the console output
    output = sims4.commands.CheatOutput(_connection)

    # Get the sim_info for the active sim
    sim = services.client_manager().get(_connection).active_sim.sim_info

    # Get the tuned trait instance from the tuning instance manager
    instance_manager = services.get_instance_manager(Types.TRAIT)
    t_toddler = instance_manager.get(get_resource_key(T_TODDLER, Types.TRAIT))
    t_child = instance_manager.get(get_resource_key(T_CHILD, Types.TRAIT))
    t_teen = instance_manager.get(get_resource_key(T_TEEN, Types.TRAIT))
    t_yadult = instance_manager.get(get_resource_key(T_YADULT, Types.TRAIT))
    t_adult = instance_manager.get(get_resource_key(T_ADULT, Types.TRAIT))
    t_elder = instance_manager.get(get_resource_key(T_ELDER, Types.TRAIT))

    stat_manager = services.get_instance_manager(Types.STATISTIC)
    s_communication = stat_manager.get(get_resource_key(S_COMMUNICATION, Types.STATISTIC))
    s_imagination = stat_manager.get(get_resource_key(S_IMMAGINATION, Types.STATISTIC))
    s_movement = stat_manager.get(get_resource_key(S_MOVEMENT, Types.STATISTIC))
    s_potty = stat_manager.get(get_resource_key(S_POTTY, Types.STATISTIC))
    s_thinking = stat_manager.get(get_resource_key(S_THINKING, Types.STATISTIC))
    s_creativity = stat_manager.get(get_resource_key(S_CREATIVITY, Types.STATISTIC))
    s_mental = stat_manager.get(get_resource_key(S_MENTAL, Types.STATISTIC))
    s_motor = stat_manager.get(get_resource_key(S_MOTOR, Types.STATISTIC))
    s_social = stat_manager.get(get_resource_key(S_SOCIAL, Types.STATISTIC))
    s_acting = stat_manager.get(get_resource_key(S_ACTING, Types.STATISTIC))
    s_archaeology = stat_manager.get(get_resource_key(S_ARCHAEOLOGY, Types.STATISTIC))
    s_baking = stat_manager.get(get_resource_key(S_BAKING, Types.STATISTIC))
    s_bartending = stat_manager.get(get_resource_key(S_BARTENDING, Types.STATISTIC))
    s_bowling = stat_manager.get(get_resource_key(S_BOWLING, Types.STATISTIC))
    s_charisma = stat_manager.get(get_resource_key(S_CHARISMA, Types.STATISTIC))
    s_chopsticks = stat_manager.get(get_resource_key(S_CHOPSTICKS, Types.STATISTIC))
    s_comedy = stat_manager.get(get_resource_key(S_COMEDY, Types.STATISTIC))
    s_cooking = stat_manager.get(get_resource_key(S_COOKING, Types.STATISTIC))
    s_crossstitch = stat_manager.get(get_resource_key(S_CROSSSTITCH, Types.STATISTIC))
    s_dancing = stat_manager.get(get_resource_key(S_DANCING, Types.STATISTIC))
    s_djmixing = stat_manager.get(get_resource_key(S_DJMIXING, Types.STATISTIC))
    s_dogtraining = stat_manager.get(get_resource_key(S_DOGTRAINING, Types.STATISTIC))
    s_entrepreneur = stat_manager.get(get_resource_key(S_ENTREPRENEUR, Types.STATISTIC))
    s_fabrication = stat_manager.get(get_resource_key(S_FABRICATION, Types.STATISTIC))
    s_fishing = stat_manager.get(get_resource_key(S_FISHING, Types.STATISTIC))
    s_flowerarranging = stat_manager.get(get_resource_key(S_FLOWERARRANGE, Types.STATISTIC))
    s_foosball = stat_manager.get(get_resource_key(S_FOOSBALL, Types.STATISTIC))
    s_gardening = stat_manager.get(get_resource_key(S_GARDENING, Types.STATISTIC))
    s_gourmetcooking = stat_manager.get(get_resource_key(S_GOURMETCOOKING, Types.STATISTIC))
    s_guitar = stat_manager.get(get_resource_key(S_GUITAR, Types.STATISTIC))
    s_handiness = stat_manager.get(get_resource_key(S_HANDINESS, Types.STATISTIC))
    s_herbalism = stat_manager.get(get_resource_key(S_HERBALISM, Types.STATISTIC))
    s_juicefizzing = stat_manager.get(get_resource_key(S_JUICEFIZZING, Types.STATISTIC))
    s_juicepong = stat_manager.get(get_resource_key(S_JUICEPONG, Types.STATISTIC))
    s_knitting = stat_manager.get(get_resource_key(S_KNITTING, Types.STATISTIC))
    s_localculture = stat_manager.get(get_resource_key(S_LOCALCULTURE, Types.STATISTIC))
    s_logic = stat_manager.get(get_resource_key(S_LOGIC, Types.STATISTIC))
    s_mediaproduction = stat_manager.get(get_resource_key(S_MEDIAPRODUCTION, Types.STATISTIC))
    s_medium = stat_manager.get(get_resource_key(S_MEDIUM, Types.STATISTIC))
    s_mischief = stat_manager.get(get_resource_key(S_MISCHIEF, Types.STATISTIC))
    s_painting = stat_manager.get(get_resource_key(S_PAINTING, Types.STATISTIC))
    s_parenting = stat_manager.get(get_resource_key(S_PARENTING, Types.STATISTIC))
    s_photography = stat_manager.get(get_resource_key(S_PHOTOGRAPHY, Types.STATISTIC))
    s_piano = stat_manager.get(get_resource_key(S_PIANO, Types.STATISTIC))
    s_pingpong = stat_manager.get(get_resource_key(S_PINGPONG, Types.STATISTIC))
    s_organ = stat_manager.get(get_resource_key(S_PIPEORGAN, Types.STATISTIC))
    s_programming = stat_manager.get(get_resource_key(S_PROGRAMMING, Types.STATISTIC))
    s_researchdebate = stat_manager.get(get_resource_key(S_RESEARCHDEBATE, Types.STATISTIC))
    s_retailmaintenance = stat_manager.get(get_resource_key(S_RETAILMAINTENANCE, Types.STATISTIC))
    s_retailsales = stat_manager.get(get_resource_key(S_RETAILSALES, Types.STATISTIC))
    s_retailethic = stat_manager.get(get_resource_key(S_RETAILWORKETHIC, Types.STATISTIC))
    s_robotics = stat_manager.get(get_resource_key(S_ROBOTICS, Types.STATISTIC))
    s_rockclimbing = stat_manager.get(get_resource_key(S_ROCKCLIMB, Types.STATISTIC))
    s_rocketscience = stat_manager.get(get_resource_key(S_ROCKETSCIENCE, Types.STATISTIC))
    s_singing = stat_manager.get(get_resource_key(S_SINGING, Types.STATISTIC))
    s_skating = stat_manager.get(get_resource_key(S_SKATING, Types.STATISTIC))
    s_skiing = stat_manager.get(get_resource_key(S_SKIING, Types.STATISTIC))
    s_snowboarding = stat_manager.get(get_resource_key(S_SNOWBOARDING, Types.STATISTIC))
    s_spicyfood = stat_manager.get(get_resource_key(S_SPICYFOOD, Types.STATISTIC))
    s_vampirelore = stat_manager.get(get_resource_key(S_VAMPIRELORE, Types.STATISTIC))
    s_veterinarian = stat_manager.get(get_resource_key(S_VETERINARIAN, Types.STATISTIC))
    s_videogaming = stat_manager.get(get_resource_key(S_VIDEOGAMING, Types.STATISTIC))
    s_violin = stat_manager.get(get_resource_key(S_VIOLIN, Types.STATISTIC))
    s_wellness = stat_manager.get(get_resource_key(S_WELLNESS, Types.STATISTIC))
    s_writing = stat_manager.get(get_resource_key(S_WRITING, Types.STATISTIC))

    s_ww_nudity = stat_manager.get(get_resource_key(S_WW_NUDITY, Types.STATISTIC))
    s_ww_sexpertise = stat_manager.get(get_resource_key(S_WW_SEXPERTISE, Types.STATISTIC))
    s_ww_naturism = stat_manager.get(get_resource_key(S_WW_NATURISM, Types.STATISTIC))
    s_ww_exhibit = stat_manager.get(get_resource_key(S_WW_EXHIBIT, Types.STATISTIC))
    s_ww_striptease = stat_manager.get(get_resource_key(S_WW_STRIPTEASE, Types.STATISTIC))

    #stats.set_all_skills_max

    #Skill levels
#    lvl0 = 0
#    lvl1 = 100
#    lvl2 = 1540
#    lvl3 = 3700
#    lvl4 = 7300
#    lvl5 = 12580
#    lvl6 = 19780
#    lvl7 = 29920
#    lvl8 = 43360
#    lvl9 = 60460
#    maxlevel = 81580

    #Set skill levels
    #Toddler
    #if sim.has_trait(t_toddler):
    #    s_communication.set_value(maxlevel)
    #    s_imagination.set_value(maxlevel)
    #    s_movement.set_value(maxlevel)
    #    s_potty.set_value(maxlevel)
    #    s_thinking.set_value(maxlevel)

#    if sim.has_trait(t_child):
#        s_creativity.set_value(maxlevel)
#        s_mental.set_value(maxlevel)
#        s_motor.set_value(maxlevel)
#        s_social.set_value(maxlevel)

#    if sim.has_trait(t_child) or sim.has_trait(t_teen) or sim.has_trait(t_yadult) or sim.has_trait(t_adult) or sim.has_trait(t_elder):
#        if not sim.has_trait(t_child):
#            s_ww_nudity.set_value(maxlevel)
#            s_ww_sexpertise.set_value(maxlevel)
#            s_ww_naturism.set_value(maxlevel)
#            s_ww_exhibit.set_value(maxlevel)
#            s_ww_striptease.set_value(maxlevel)

#        s_acting.set_value(maxlevel)
#        s_archaeology.set_value(maxlevel)
#        s_baking.set_value(maxlevel)
#        s_bartending.set_value(maxlevel)
#        s_bowling.set_value(maxlevel)
#        s_charisma.set_value(maxlevel)
#        s_chopsticks.set_value(maxlevel)
#        s_comedy.set_value(maxlevel)
#        s_cooking.set_value(maxlevel)
#        s_crossstitch.set_value(maxlevel)
#        s_dancing.set_value(maxlevel)
#        s_djmixing.set_value(maxlevel)
#        s_dogtraining.set_value(maxlevel)
#        s_entrepreneur.set_value(maxlevel)
#        s_fabrication.set_value(maxlevel)
#        s_fishing.set_value(maxlevel)
#        s_flowerarranging.set_value(maxlevel)
#        s_foosball.set_value(maxlevel)
#        s_gardening.set_value(maxlevel)
#        s_gourmetcooking.set_value(maxlevel)
#        s_guitar.set_value(maxlevel)
#        s_handiness.set_value(maxlevel)
#        s_herbalism.set_value(maxlevel)
#        s_juicefizzing.set_value(maxlevel)
#        s_juicepong.set_value(maxlevel)
#        s_knitting.set_value(maxlevel)
#        s_localculture.set_value(maxlevel)
#        s_logic.set_value(maxlevel)
#        s_mediaproduction.set_value(maxlevel)
#        s_medium.set_value(maxlevel)
#        s_mischief.set_value(maxlevel)
#        s_painting.set_value(maxlevel)
#        s_parenting.set_value(maxlevel)
#        s_photography.set_value(maxlevel)
#        s_piano.set_value(maxlevel)
#        s_pingpong.set_value(maxlevel)
#        s_organ.set_value(maxlevel)
#        s_programming.set_value(maxlevel)
#        s_researchdebate.set_value(maxlevel)
#        s_retailmaintenance.set_value(maxlevel)
#        s_retailsales.set_value(maxlevel)
#        s_retailethic.set_value(maxlevel)
#        s_robotics.set_value(maxlevel)
#        s_rocketscience.set_value(maxlevel)
#        s_rockclimbing.set_value(maxlevel)
#        s_singing.set_value(maxlevel)
#        s_skating.set_value(maxlevel)
#        s_skiing.set_value(maxlevel)
#        s_snowboarding.set_value(maxlevel)
#        s_spicyfood.set_value(maxlevel)
#        s_vampirelore.set_value(maxlevel)
#        s_veterinarian.set_value(maxlevel)
#        s_videogaming.set_value(maxlevel)
#        s_violin.set_value(maxlevel)
#        s_wellness.set_value(maxlevel)
#        s_writing.set_value(maxlevel)