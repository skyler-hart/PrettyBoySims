from sims4.resources import Types, get_resource_key
from pbs_t_ids import *
from pbs_s_ids import *
import os
import services, sims4.commands


@sims4.commands.Command('pbs_allsims', command_type=sims4.commands.CommandType.Live)
def pbs_allsims(_connection=None):
    # Get the console output
    output = sims4.commands.CheatOutput(_connection)

    # Get the sim_info for the active sim
    sim = services.client_manager().get(_connection).active_sim.sim_info

    # Get the tuned trait instance from the tuning instance manager
    instance_manager = services.get_instance_manager(Types.TRAIT)

    # Remove or add traits from all sims

    archaeologyskill_giveauthenticationmail_prohibit = instance_manager.get(get_resource_key(ARCHAEOLOGYSKILL_GIVEAUTHENTICATIONMAIL_PROHIBIT, Types.TRAIT))
    if not sim.has_trait(archaeologyskill_giveauthenticationmail_prohibit):
        sim.add_trait(archaeologyskill_giveauthenticationmail_prohibit)

    fametraits_celebritywalk_on = instance_manager.get(get_resource_key(FAMETRAITS_CELEBRITYWALK_ON, Types.TRAIT))
    if sim.has_trait(fametraits_celebritywalk_on):
        sim.remove_trait(fametraits_celebritywalk_on)

    fametraits_shine_off = instance_manager.get(get_resource_key(FAMETRAITS_SHINE_OFF, Types.TRAIT))
    if not sim.has_trait(fametraits_shine_off):
        sim.add_trait(fametraits_shine_off)

    fametraits_shine_on_rank4 = instance_manager.get(get_resource_key(FAMETRAITS_SHINE_ON_RANK4, Types.TRAIT))
    if sim.has_trait(fametraits_shine_on_rank4):
        sim.remove_trait(fametraits_shine_on_rank4)

    fametraits_shine_on_rank5 = instance_manager.get(get_resource_key(FAMETRAITS_SHINE_ON_RANK5, Types.TRAIT))
    if sim.has_trait(fametraits_shine_on_rank5):
        sim.remove_trait(fametraits_shine_on_rank5)

    trait_computerglasses_wearing = instance_manager.get(get_resource_key(TRAIT_COMPUTERGLASSES_WEARING, Types.TRAIT))
    if sim.has_trait(trait_computerglasses_wearing):
        sim.remove_trait(trait_computerglasses_wearing)

    trait_computerglasses_wearing_blue = instance_manager.get(get_resource_key(TRAIT_COMPUTERGLASSES_WEARING_BLUE, Types.TRAIT))
    if sim.has_trait(trait_computerglasses_wearing_blue):
        sim.remove_trait(trait_computerglasses_wearing_blue)

    trait_computerglasses_wearing_green = instance_manager.get(get_resource_key(TRAIT_COMPUTERGLASSES_WEARING_GREEN, Types.TRAIT))
    if sim.has_trait(trait_computerglasses_wearing_green):
        sim.remove_trait(trait_computerglasses_wearing_green)

    trait_computerglasses_wearing_orange = instance_manager.get(get_resource_key(TRAIT_COMPUTERGLASSES_WEARING_ORANGE, Types.TRAIT))
    if sim.has_trait(trait_computerglasses_wearing_orange):
        sim.remove_trait(trait_computerglasses_wearing_orange)

    trait_computerglasses_wearing_pink = instance_manager.get(get_resource_key(TRAIT_COMPUTERGLASSES_WEARING_PINK, Types.TRAIT))
    if sim.has_trait(trait_computerglasses_wearing_pink):
        sim.remove_trait(trait_computerglasses_wearing_pink)

    trait_computerglasses_wearing_red = instance_manager.get(get_resource_key(TRAIT_COMPUTERGLASSES_WEARING_RED, Types.TRAIT))
    if sim.has_trait(trait_computerglasses_wearing_red):
        sim.remove_trait(trait_computerglasses_wearing_red)

    trait_computerglasses_wearing_yellow = instance_manager.get(get_resource_key(TRAIT_COMPUTERGLASSES_WEARING_YELLOW, Types.TRAIT))
    if sim.has_trait(trait_computerglasses_wearing_yellow):
        sim.remove_trait(trait_computerglasses_wearing_yellow)

    trait_crystalhelmet_alabaster = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_ALABASTER, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_alabaster):
        sim.remove_trait(trait_crystalhelmet_alabaster)

    trait_crystalhelmet_alexandrite_ep = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_ALEXANDRITE_EP, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_alexandrite_ep):
        sim.remove_trait(trait_crystalhelmet_alexandrite_ep)

    trait_crystalhelmet_amazonite_ep = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_AMAZONITE_EP, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_amazonite_ep):
        sim.remove_trait(trait_crystalhelmet_amazonite_ep)

    trait_crystalhelmet_amethyst = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_AMETHYST, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_amethyst):
        sim.remove_trait(trait_crystalhelmet_amethyst)

    trait_crystalhelmet_citrine = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_CITRINE, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_citrine):
        sim.remove_trait(trait_crystalhelmet_citrine)

    trait_crystalhelmet_crandestine_ep = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_CRANDESTINE_EP, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_crandestine_ep):
        sim.remove_trait(trait_crystalhelmet_crandestine_ep)

    trait_crystalhelmet_diamond = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_DIAMOND, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_diamond):
        sim.remove_trait(trait_crystalhelmet_diamond)

    trait_crystalhelmet_emerald = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_EMERALD, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_emerald):
        sim.remove_trait(trait_crystalhelmet_emerald)

    trait_crystalhelmet_fireopal = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_FIREOPAL, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_fireopal):
        sim.remove_trait(trait_crystalhelmet_fireopal)

    trait_crystalhelmet_hematite = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_HEMATITE, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_hematite):
        sim.remove_trait(trait_crystalhelmet_hematite)

    trait_crystalhelmet_jet = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_JET, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_jet):
        sim.remove_trait(trait_crystalhelmet_jet)

    trait_crystalhelmet_jonquilyst = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_JONQUILYST, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_jonquilyst):
        sim.remove_trait(trait_crystalhelmet_jonquilyst)

    trait_crystalhelmet_nitelite_ep = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_NITELITE_EP, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_nitelite_ep):
        sim.remove_trait(trait_crystalhelmet_nitelite_ep)

    trait_crystalhelmet_orangetopaz = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_ORANGETOPAZ, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_orangetopaz):
        sim.remove_trait(trait_crystalhelmet_orangetopaz)

    trait_crystalhelmet_peach = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_PEACH, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_peach):
        sim.remove_trait(trait_crystalhelmet_peach)

    trait_crystalhelmet_plumbite = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_PLUMBITE, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_plumbite):
        sim.remove_trait(trait_crystalhelmet_plumbite)

    trait_crystalhelmet_quartz = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_QUARTZ, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_quartz):
        sim.remove_trait(trait_crystalhelmet_quartz)

    trait_crystalhelmet_rainborz = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_RAINBORZ, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_rainborz):
        sim.remove_trait(trait_crystalhelmet_rainborz)

    trait_crystalhelmet_rose = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_ROSE, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_rose):
        sim.remove_trait(trait_crystalhelmet_rose)

    trait_crystalhelmet_ruby = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_RUBY, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_ruby):
        sim.remove_trait(trait_crystalhelmet_ruby)

    trait_crystalhelmet_sapphire = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_SAPPHIRE, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_sapphire):
        sim.remove_trait(trait_crystalhelmet_sapphire)

    trait_crystalhelmet_shinalite = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_SHINALITE, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_shinalite):
        sim.remove_trait(trait_crystalhelmet_shinalite)

    trait_crystalhelmet_simanite = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_SIMANITE, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_simanite):
        sim.remove_trait(trait_crystalhelmet_simanite)

    trait_crystalhelmet_turquoise = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_TURQUOISE, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_turquoise):
        sim.remove_trait(trait_crystalhelmet_turquoise)

    trait_doctor_sicknessresistant = instance_manager.get(get_resource_key(TRAIT_DOCTOR_SICKNESSRESISTANT, Types.TRAIT))
    if not sim.has_trait(trait_doctor_sicknessresistant):
        sim.add_trait(trait_doctor_sicknessresistant)

    trait_essenceofflavor = instance_manager.get(get_resource_key(TRAIT_ESSENCEOFFLAVOR, Types.TRAIT))
    if not sim.has_trait(trait_essenceofflavor):
        sim.add_trait(trait_essenceofflavor)

    trait_fear_beingcheatedon = instance_manager.get(get_resource_key(TRAIT_FEAR_BEINGCHEATEDON, Types.TRAIT))
    if sim.has_trait(trait_fear_beingcheatedon):
        sim.remove_trait(trait_fear_beingcheatedon)

    trait_fear_beingjudged = instance_manager.get(get_resource_key(TRAIT_FEAR_BEINGJUDGED, Types.TRAIT))
    if sim.has_trait(trait_fear_beingjudged):
        sim.remove_trait(trait_fear_beingjudged)

    trait_fear_cowplant = instance_manager.get(get_resource_key(TRAIT_FEAR_COWPLANT, Types.TRAIT))
    if sim.has_trait(trait_fear_cowplant):
        sim.remove_trait(trait_fear_cowplant)

    trait_fear_crowdedplaces = instance_manager.get(get_resource_key(TRAIT_FEAR_CROWDEDPLACES, Types.TRAIT))
    if sim.has_trait(trait_fear_crowdedplaces):
        sim.remove_trait(trait_fear_crowdedplaces)

    trait_fear_dark = instance_manager.get(get_resource_key(TRAIT_FEAR_DARK, Types.TRAIT))
    if sim.has_trait(trait_fear_dark):
        sim.remove_trait(trait_fear_dark)

    trait_fear_deadendjob = instance_manager.get(get_resource_key(TRAIT_FEAR_DEADENDJOB, Types.TRAIT))
    if sim.has_trait(trait_fear_deadendjob):
        sim.remove_trait(trait_fear_deadendjob)

    trait_fear_death = instance_manager.get(get_resource_key(TRAIT_FEAR_DEATH, Types.TRAIT))
    if sim.has_trait(trait_fear_death):
        sim.remove_trait(trait_fear_death)

    trait_fear_disappointingparents = instance_manager.get(get_resource_key(TRAIT_FEAR_DISAPPOINTINGPARENTS, Types.TRAIT))
    if sim.has_trait(trait_fear_disappointingparents):
        sim.remove_trait(trait_fear_disappointingparents)

    trait_fear_disappointingparents_parentdeceasedflag = instance_manager.get(get_resource_key(TRAIT_FEAR_DISAPPOINTINGPARENTS_PARENTDECEASEDFLAG, Types.TRAIT))
    if sim.has_trait(trait_fear_disappointingparents_parentdeceasedflag):
        sim.remove_trait(trait_fear_disappointingparents_parentdeceasedflag)

    trait_fear_failing_afterschoolactivities = instance_manager.get(get_resource_key(TRAIT_FEAR_FAILING_AFTERSCHOOLACTIVITIES, Types.TRAIT))
    if sim.has_trait(trait_fear_failing_afterschoolactivities):
        sim.remove_trait(trait_fear_failing_afterschoolactivities)

    trait_fear_failing_class = instance_manager.get(get_resource_key(TRAIT_FEAR_FAILING_CLASS, Types.TRAIT))
    if sim.has_trait(trait_fear_failing_class):
        sim.remove_trait(trait_fear_failing_class)

    trait_fear_failing_tests = instance_manager.get(get_resource_key(TRAIT_FEAR_FAILING_TESTS, Types.TRAIT))
    if sim.has_trait(trait_fear_failing_tests):
        sim.remove_trait(trait_fear_failing_tests)

    trait_fear_failure = instance_manager.get(get_resource_key(TRAIT_FEAR_FAILURE, Types.TRAIT))
    if sim.has_trait(trait_fear_failure):
        sim.remove_trait(trait_fear_failure)

    trait_fear_fire = instance_manager.get(get_resource_key(TRAIT_FEAR_FIRE, Types.TRAIT))
    if sim.has_trait(trait_fear_fire):
        sim.remove_trait(trait_fear_fire)

    trait_fear_ghosts = instance_manager.get(get_resource_key(TRAIT_FEAR_GHOSTS, Types.TRAIT))
    if sim.has_trait(trait_fear_ghosts):
        sim.remove_trait(trait_fear_ghosts)

    trait_fear_homework = instance_manager.get(get_resource_key(TRAIT_FEAR_HOMEWORK, Types.TRAIT))
    if sim.has_trait(trait_fear_homework):
        sim.remove_trait(trait_fear_homework)

    trait_fear_swimming = instance_manager.get(get_resource_key(TRAIT_FEAR_SWIMMING, Types.TRAIT))
    if sim.has_trait(trait_fear_swimming):
        sim.remove_trait(trait_fear_swimming)

    trait_fear_unfulfilled = instance_manager.get(get_resource_key(TRAIT_FEAR_UNFULFILLED, Types.TRAIT))
    if sim.has_trait(trait_fear_unfulfilled):
        sim.remove_trait(trait_fear_unfulfilled)

    trait_filthdweller = instance_manager.get(get_resource_key(TRAIT_FILTHDWELLER, Types.TRAIT))
    if sim.has_trait(trait_filthdweller):
        sim.remove_trait(trait_filthdweller)

    trait_freeservices = instance_manager.get(get_resource_key(TRAIT_FREESERVICES, Types.TRAIT))
    if not sim.has_trait(trait_freeservices):
        sim.add_trait(trait_freeservices)

    trait_frugal = instance_manager.get(get_resource_key(TRAIT_FRUGAL, Types.TRAIT))
    if not sim.has_trait(trait_frugal):
        sim.add_trait(trait_frugal)

    trait_genderoptions_attractedto_notfemale = instance_manager.get(get_resource_key(TRAIT_GENDEROPTIONS_ATTRACTEDTO_NOTFEMALE, Types.TRAIT))
    if sim.has_trait(trait_genderoptions_attractedto_notfemale):
        sim.remove_trait(trait_genderoptions_attractedto_notfemale)

    trait_genderoptions_attractedto_notmale = instance_manager.get(get_resource_key(TRAIT_GENDEROPTIONS_ATTRACTEDTO_NOTMALE, Types.TRAIT))
    if sim.has_trait(trait_genderoptions_attractedto_notmale):
        sim.remove_trait(trait_genderoptions_attractedto_notmale)

    trait_genderoptions_sexuality_exploring = instance_manager.get(get_resource_key(TRAIT_GENDEROPTIONS_SEXUALITY_EXPLORING, Types.TRAIT))
    if not sim.has_trait(trait_genderoptions_sexuality_exploring):
        sim.add_trait(trait_genderoptions_sexuality_exploring)

    trait_genderoptions_sexuality_notexploring = instance_manager.get(get_resource_key(TRAIT_GENDEROPTIONS_SEXUALITY_NOTEXPLORING, Types.TRAIT))
    if sim.has_trait(trait_genderoptions_sexuality_notexploring):
        sim.remove_trait(trait_genderoptions_sexuality_notexploring)

    trait_glutton = instance_manager.get(get_resource_key(TRAIT_GLUTTON, Types.TRAIT))
    if sim.has_trait(trait_glutton):
        sim.remove_trait(trait_glutton)

    trait_gradeschool_a = instance_manager.get(get_resource_key(TRAIT_GRADESCHOOL_A, Types.TRAIT))
    if not sim.has_trait(trait_gradeschool_a):
        sim.add_trait(trait_gradeschool_a)

    trait_gradeschool_b = instance_manager.get(get_resource_key(TRAIT_GRADESCHOOL_B, Types.TRAIT))
    if sim.has_trait(trait_gradeschool_b):
        sim.remove_trait(trait_gradeschool_b)

    trait_gradeschool_c = instance_manager.get(get_resource_key(TRAIT_GRADESCHOOL_C, Types.TRAIT))
    if sim.has_trait(trait_gradeschool_c):
        sim.remove_trait(trait_gradeschool_c)

    trait_gradeschool_d = instance_manager.get(get_resource_key(TRAIT_GRADESCHOOL_D, Types.TRAIT))
    if sim.has_trait(trait_gradeschool_d):
        sim.remove_trait(trait_gradeschool_d)

    trait_gradeschool_f = instance_manager.get(get_resource_key(TRAIT_GRADESCHOOL_F, Types.TRAIT))
    if sim.has_trait(trait_gradeschool_f):
        sim.remove_trait(trait_gradeschool_f)

    trait_highschool_a = instance_manager.get(get_resource_key(TRAIT_HIGHSCHOOL_A, Types.TRAIT))
    if not sim.has_trait(trait_highschool_a):
        sim.add_trait(trait_highschool_a)

    trait_highschool_b = instance_manager.get(get_resource_key(TRAIT_HIGHSCHOOL_B, Types.TRAIT))
    if sim.has_trait(trait_highschool_b):
        sim.remove_trait(trait_highschool_b)

    trait_highschool_c = instance_manager.get(get_resource_key(TRAIT_HIGHSCHOOL_C, Types.TRAIT))
    if sim.has_trait(trait_highschool_c):
        sim.remove_trait(trait_highschool_c)

    trait_highschool_d = instance_manager.get(get_resource_key(TRAIT_HIGHSCHOOL_D, Types.TRAIT))
    if sim.has_trait(trait_highschool_d):
        sim.remove_trait(trait_highschool_d)

    trait_highschool_f = instance_manager.get(get_resource_key(TRAIT_HIGHSCHOOL_F, Types.TRAIT))
    if sim.has_trait(trait_highschool_f):
        sim.remove_trait(trait_highschool_f)

    trait_hotheaded = instance_manager.get(get_resource_key(TRAIT_HOTHEADED, Types.TRAIT))
    if sim.has_trait(trait_hotheaded):
        sim.remove_trait(trait_hotheaded)

    trait_hsexit_expelled = instance_manager.get(get_resource_key(TRAIT_HSEXIT_EXPELLED, Types.TRAIT))
    if sim.has_trait(trait_hsexit_expelled):
        sim.remove_trait(trait_hsexit_expelled)

    trait_insane = instance_manager.get(get_resource_key(TRAIT_INSANE, Types.TRAIT))
    if sim.has_trait(trait_insane):
        sim.remove_trait(trait_insane)

    trait_invested = instance_manager.get(get_resource_key(TRAIT_INVESTED, Types.TRAIT))
    if not sim.has_trait(trait_invested):
        sim.add_trait(trait_invested)

    trait_ispregnant = instance_manager.get(get_resource_key(TRAIT_ISPREGNANT, Types.TRAIT))
    if sim.has_trait(trait_ispregnant):
        sim.remove_trait(trait_ispregnant)

    trait_mechanicalsuit_hoverengaged = instance_manager.get(get_resource_key(TRAIT_MECHANICALSUIT_HOVERENGAGED, Types.TRAIT))
    if sim.has_trait(trait_mechanicalsuit_hoverengaged):
        sim.remove_trait(trait_mechanicalsuit_hoverengaged)

    trait_mechanicalsuit_wearing_body_beigewhite = instance_manager.get(get_resource_key(TRAIT_MECHANICALSUIT_WEARING_BODY_BEIGEWHITE, Types.TRAIT))
    if sim.has_trait(trait_mechanicalsuit_wearing_body_beigewhite):
        sim.remove_trait(trait_mechanicalsuit_wearing_body_beigewhite)

    trait_mechanicalsuit_wearing_body_blackblue = instance_manager.get(get_resource_key(TRAIT_MECHANICALSUIT_WEARING_BODY_BLACKBLUE, Types.TRAIT))
    if sim.has_trait(trait_mechanicalsuit_wearing_body_blackblue):
        sim.remove_trait(trait_mechanicalsuit_wearing_body_blackblue)

    trait_mechanicalsuit_wearing_body_bluered = instance_manager.get(get_resource_key(TRAIT_MECHANICALSUIT_WEARING_BODY_BLUERED, Types.TRAIT))
    if sim.has_trait(trait_mechanicalsuit_wearing_body_bluered):
        sim.remove_trait(trait_mechanicalsuit_wearing_body_bluered)

    trait_mechanicalsuit_wearing_body_graybrown = instance_manager.get(get_resource_key(TRAIT_MECHANICALSUIT_WEARING_BODY_GRAYBROWN, Types.TRAIT))
    if sim.has_trait(trait_mechanicalsuit_wearing_body_graybrown):
        sim.remove_trait(trait_mechanicalsuit_wearing_body_graybrown)

    trait_mechanicalsuit_wearing_body_greenbrown = instance_manager.get(get_resource_key(TRAIT_MECHANICALSUIT_WEARING_BODY_GREENBROWN, Types.TRAIT))
    if sim.has_trait(trait_mechanicalsuit_wearing_body_greenbrown):
        sim.remove_trait(trait_mechanicalsuit_wearing_body_greenbrown)

    trait_mechanicalsuit_wearing_body_redgreen = instance_manager.get(get_resource_key(TRAIT_MECHANICALSUIT_WEARING_BODY_REDGREEN, Types.TRAIT))
    if sim.has_trait(trait_mechanicalsuit_wearing_body_redgreen):
        sim.remove_trait(trait_mechanicalsuit_wearing_body_redgreen)

    trait_mechanicalsuit_wearing_body_whitecopper = instance_manager.get(get_resource_key(TRAIT_MECHANICALSUIT_WEARING_BODY_WHITECOPPER, Types.TRAIT))
    if sim.has_trait(trait_mechanicalsuit_wearing_body_whitecopper):
        sim.remove_trait(trait_mechanicalsuit_wearing_body_whitecopper)

    trait_mechanicalsuit_wearing_helmet_blackblue = instance_manager.get(get_resource_key(TRAIT_MECHANICALSUIT_WEARING_HELMET_BLACKBLUE, Types.TRAIT))
    if sim.has_trait(trait_mechanicalsuit_wearing_helmet_blackblue):
        sim.remove_trait(trait_mechanicalsuit_wearing_helmet_blackblue)

    trait_mechanicalsuit_wearing_helmet_blackcopper = instance_manager.get(get_resource_key(TRAIT_MECHANICALSUIT_WEARING_HELMET_BLACKCOPPER, Types.TRAIT))
    if sim.has_trait(trait_mechanicalsuit_wearing_helmet_blackcopper):
        sim.remove_trait(trait_mechanicalsuit_wearing_helmet_blackcopper)

    trait_mechanicalsuit_wearing_helmet_blackgold = instance_manager.get(get_resource_key(TRAIT_MECHANICALSUIT_WEARING_HELMET_BLACKGOLD, Types.TRAIT))
    if sim.has_trait(trait_mechanicalsuit_wearing_helmet_blackgold):
        sim.remove_trait(trait_mechanicalsuit_wearing_helmet_blackgold)

    trait_mechanicalsuit_wearing_helmet_blackgray = instance_manager.get(get_resource_key(TRAIT_MECHANICALSUIT_WEARING_HELMET_BLACKGRAY, Types.TRAIT))
    if sim.has_trait(trait_mechanicalsuit_wearing_helmet_blackgray):
        sim.remove_trait(trait_mechanicalsuit_wearing_helmet_blackgray)

    trait_mechanicalsuit_wearing_helmet_bluegray = instance_manager.get(get_resource_key(TRAIT_MECHANICALSUIT_WEARING_HELMET_BLUEGRAY, Types.TRAIT))
    if sim.has_trait(trait_mechanicalsuit_wearing_helmet_bluegray):
        sim.remove_trait(trait_mechanicalsuit_wearing_helmet_bluegray)

    trait_mechanicalsuit_wearing_helmet_grayblack = instance_manager.get(get_resource_key(TRAIT_MECHANICALSUIT_WEARING_HELMET_GRAYBLACK, Types.TRAIT))
    if sim.has_trait(trait_mechanicalsuit_wearing_helmet_grayblack):
        sim.remove_trait(trait_mechanicalsuit_wearing_helmet_grayblack)

    trait_mechanicalsuit_wearing_helmet_greenblack = instance_manager.get(get_resource_key(TRAIT_MECHANICALSUIT_WEARING_HELMET_GREENBLACK, Types.TRAIT))
    if sim.has_trait(trait_mechanicalsuit_wearing_helmet_greenblack):
        sim.remove_trait(trait_mechanicalsuit_wearing_helmet_greenblack)

    trait_nightowl_crystalhelmet = instance_manager.get(get_resource_key(TRAIT_NIGHTOWL_CRYSTALHELMET, Types.TRAIT))
    if sim.has_trait(trait_nightowl_crystalhelmet):
        sim.remove_trait(trait_nightowl_crystalhelmet)

    trait_roboticsarm_wearing_beigewhite = instance_manager.get(get_resource_key(TRAIT_ROBOTICSARM_WEARING_BEIGEWHITE, Types.TRAIT))
    if sim.has_trait(trait_roboticsarm_wearing_beigewhite):
        sim.remove_trait(trait_roboticsarm_wearing_beigewhite)

    trait_roboticsarm_wearing_blackblue = instance_manager.get(get_resource_key(TRAIT_ROBOTICSARM_WEARING_BLACKBLUE, Types.TRAIT))
    if sim.has_trait(trait_roboticsarm_wearing_blackblue):
        sim.remove_trait(trait_roboticsarm_wearing_blackblue)

    trait_roboticsarm_wearing_bluered = instance_manager.get(get_resource_key(TRAIT_ROBOTICSARM_WEARING_BLUERED, Types.TRAIT))
    if sim.has_trait(trait_roboticsarm_wearing_bluered):
        sim.remove_trait(trait_roboticsarm_wearing_bluered)

    trait_roboticsarm_wearing_graybrown = instance_manager.get(get_resource_key(TRAIT_ROBOTICSARM_WEARING_GRAYBROWN, Types.TRAIT))
    if sim.has_trait(trait_roboticsarm_wearing_graybrown):
        sim.remove_trait(trait_roboticsarm_wearing_graybrown)

    trait_roboticsarm_wearing_greenbrown = instance_manager.get(get_resource_key(TRAIT_ROBOTICSARM_WEARING_GREENBROWN, Types.TRAIT))
    if sim.has_trait(trait_roboticsarm_wearing_greenbrown):
        sim.remove_trait(trait_roboticsarm_wearing_greenbrown)

    trait_roboticsarm_wearing_redgreen = instance_manager.get(get_resource_key(TRAIT_ROBOTICSARM_WEARING_REDGREEN, Types.TRAIT))
    if sim.has_trait(trait_roboticsarm_wearing_redgreen):
        sim.remove_trait(trait_roboticsarm_wearing_redgreen)

    trait_roboticsarm_wearing_whitecopper = instance_manager.get(get_resource_key(TRAIT_ROBOTICSARM_WEARING_WHITECOPPER, Types.TRAIT))
    if sim.has_trait(trait_roboticsarm_wearing_whitecopper):
        sim.remove_trait(trait_roboticsarm_wearing_whitecopper)

    trait_selfassured = instance_manager.get(get_resource_key(TRAIT_SELFASSURED, Types.TRAIT))
    if not sim.has_trait(trait_selfassured):
        sim.add_trait(trait_selfassured)

    trait_sexualorientation_woohoointerests_female = instance_manager.get(get_resource_key(TRAIT_SEXUALORIENTATION_WOOHOOINTERESTS_FEMALE, Types.TRAIT))
    if not sim.has_trait(trait_sexualorientation_woohoointerests_female):
        sim.add_trait(trait_sexualorientation_woohoointerests_female)

    trait_sexualorientation_woohoointerests_male = instance_manager.get(get_resource_key(TRAIT_SEXUALORIENTATION_WOOHOOINTERESTS_MALE, Types.TRAIT))
    if not sim.has_trait(trait_sexualorientation_woohoointerests_male):
        sim.add_trait(trait_sexualorientation_woohoointerests_male)

    trait_sexualorientation_woohoointerests_notfemale = instance_manager.get(get_resource_key(TRAIT_SEXUALORIENTATION_WOOHOOINTERESTS_NOTFEMALE, Types.TRAIT))
    if sim.has_trait(trait_sexualorientation_woohoointerests_notfemale):
        sim.remove_trait(trait_sexualorientation_woohoointerests_notfemale)

    trait_simpreference_dislikes_activities_djmixing = instance_manager.get(get_resource_key(TRAIT_SIMPREFERENCE_DISLIKES_ACTIVITIES_DJMIXING, Types.TRAIT))
    if sim.has_trait(trait_simpreference_dislikes_activities_djmixing):
        sim.remove_trait(trait_simpreference_dislikes_activities_djmixing)

    trait_simpreference_dislikes_activities_fitness = instance_manager.get(get_resource_key(TRAIT_SIMPREFERENCE_DISLIKES_ACTIVITIES_FITNESS, Types.TRAIT))
    if sim.has_trait(trait_simpreference_dislikes_activities_fitness):
        sim.remove_trait(trait_simpreference_dislikes_activities_fitness)

    trait_simpreference_dislikes_activities_guitar = instance_manager.get(get_resource_key(TRAIT_SIMPREFERENCE_DISLIKES_ACTIVITIES_GUITAR, Types.TRAIT))
    if sim.has_trait(trait_simpreference_dislikes_activities_guitar):
        sim.remove_trait(trait_simpreference_dislikes_activities_guitar)

    trait_simpreference_dislikes_activities_piano = instance_manager.get(get_resource_key(TRAIT_SIMPREFERENCE_DISLIKES_ACTIVITIES_PIANO, Types.TRAIT))
    if sim.has_trait(trait_simpreference_dislikes_activities_piano):
        sim.remove_trait(trait_simpreference_dislikes_activities_piano)

    trait_simpreference_dislikes_activities_pipeorgan = instance_manager.get(get_resource_key(TRAIT_SIMPREFERENCE_DISLIKES_ACTIVITIES_PIPEORGAN, Types.TRAIT))
    if sim.has_trait(trait_simpreference_dislikes_activities_pipeorgan):
        sim.remove_trait(trait_simpreference_dislikes_activities_pipeorgan)

    trait_simpreference_dislikes_activities_programming = instance_manager.get(get_resource_key(TRAIT_SIMPREFERENCE_DISLIKES_ACTIVITIES_PROGRAMMING, Types.TRAIT))
    if sim.has_trait(trait_simpreference_dislikes_activities_programming):
        sim.remove_trait(trait_simpreference_dislikes_activities_programming)

    trait_simpreference_dislikes_activities_rockclimbing = instance_manager.get(get_resource_key(TRAIT_SIMPREFERENCE_DISLIKES_ACTIVITIES_ROCKCLIMBING, Types.TRAIT))
    if sim.has_trait(trait_simpreference_dislikes_activities_rockclimbing):
        sim.remove_trait(trait_simpreference_dislikes_activities_rockclimbing)

    trait_simpreference_dislikes_activities_singing = instance_manager.get(get_resource_key(TRAIT_SIMPREFERENCE_DISLIKES_ACTIVITIES_SINGING, Types.TRAIT))
    if sim.has_trait(trait_simpreference_dislikes_activities_singing):
        sim.remove_trait(trait_simpreference_dislikes_activities_singing)

    trait_simpreference_dislikes_activities_violin = instance_manager.get(get_resource_key(TRAIT_SIMPREFERENCE_DISLIKES_ACTIVITIES_VIOLIN, Types.TRAIT))
    if sim.has_trait(trait_simpreference_dislikes_activities_violin):
        sim.remove_trait(trait_simpreference_dislikes_activities_violin)

    trait_simpreference_dislikes_activities_wellness = instance_manager.get(get_resource_key(TRAIT_SIMPREFERENCE_DISLIKES_ACTIVITIES_WELLNESS, Types.TRAIT))
    if sim.has_trait(trait_simpreference_dislikes_activities_wellness):
        sim.remove_trait(trait_simpreference_dislikes_activities_wellness)

    trait_simpreference_dislikes_activities_writing = instance_manager.get(get_resource_key(TRAIT_SIMPREFERENCE_DISLIKES_ACTIVITIES_WRITING, Types.TRAIT))
    if sim.has_trait(trait_simpreference_dislikes_activities_writing):
        sim.remove_trait(trait_simpreference_dislikes_activities_writing)

    trait_simpreference_likes_activities_fitness = instance_manager.get(get_resource_key(TRAIT_SIMPREFERENCE_LIKES_ACTIVITIES_FITNESS, Types.TRAIT))
    if not sim.has_trait(trait_simpreference_likes_activities_fitness):
        sim.add_trait(trait_simpreference_likes_activities_fitness)

    trait_simpreference_likes_activities_wellness = instance_manager.get(get_resource_key(TRAIT_SIMPREFERENCE_LIKES_ACTIVITIES_WELLNESS, Types.TRAIT))
    if not sim.has_trait(trait_simpreference_likes_activities_wellness):
        sim.add_trait(trait_simpreference_likes_activities_wellness)

    trait_simpreference_noopinion_activities_fitness = instance_manager.get(get_resource_key(TRAIT_SIMPREFERENCE_NOOPINION_ACTIVITIES_FITNESS, Types.TRAIT))
    if sim.has_trait(trait_simpreference_noopinion_activities_fitness):
        sim.remove_trait(trait_simpreference_noopinion_activities_fitness)

    trait_simpreference_noopinion_activities_wellness = instance_manager.get(get_resource_key(TRAIT_SIMPREFERENCE_NOOPINION_ACTIVITIES_WELLNESS, Types.TRAIT))
    if sim.has_trait(trait_simpreference_noopinion_activities_wellness):
        sim.remove_trait(trait_simpreference_noopinion_activities_wellness)

    trait_slob = instance_manager.get(get_resource_key(TRAIT_SLOB, Types.TRAIT))
    if sim.has_trait(trait_slob):
        sim.remove_trait(trait_slob)

    trait_speedcleaner = instance_manager.get(get_resource_key(TRAIT_SPEEDCLEANER, Types.TRAIT))
    if not sim.has_trait(trait_speedcleaner):
        sim.add_trait(trait_speedcleaner)

    trait_speedreader = instance_manager.get(get_resource_key(TRAIT_SPEEDREADER, Types.TRAIT))
    if not sim.has_trait(trait_speedreader):
        sim.add_trait(trait_speedreader)

    trait_stormchaser = instance_manager.get(get_resource_key(TRAIT_STORMCHASER, Types.TRAIT))
    if not sim.has_trait(trait_stormchaser):
        sim.add_trait(trait_stormchaser)

    trait_temperature_burningman = instance_manager.get(get_resource_key(TRAIT_TEMPERATURE_BURNINGMAN, Types.TRAIT))
    if not sim.has_trait(trait_temperature_burningman):
        sim.add_trait(trait_temperature_burningman)

    trait_temperature_coldacclimation = instance_manager.get(get_resource_key(TRAIT_TEMPERATURE_COLDACCLIMATION, Types.TRAIT))
    if sim.has_trait(trait_temperature_coldacclimation):
        sim.remove_trait(trait_temperature_coldacclimation)

    trait_temperature_heatacclimation = instance_manager.get(get_resource_key(TRAIT_TEMPERATURE_HEATACCLIMATION, Types.TRAIT))
    if sim.has_trait(trait_temperature_heatacclimation):
        sim.remove_trait(trait_temperature_heatacclimation)

    trait_temperature_iceman = instance_manager.get(get_resource_key(TRAIT_TEMPERATURE_ICEMAN, Types.TRAIT))
    if not sim.has_trait(trait_temperature_iceman):
        sim.add_trait(trait_temperature_iceman)

    trait_theknack = instance_manager.get(get_resource_key(TRAIT_THEKNACK, Types.TRAIT))
    if not sim.has_trait(trait_theknack):
        sim.add_trait(trait_theknack)

    trait_university_arthistorydegreeba = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_ARTHISTORYDEGREEBA, Types.TRAIT))
    if sim.has_trait(trait_university_arthistorydegreeba):
        sim.remove_trait(trait_university_arthistorydegreeba)

    trait_university_arthistorydegreebs = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_ARTHISTORYDEGREEBS, Types.TRAIT))
    if sim.has_trait(trait_university_arthistorydegreebs):
        sim.remove_trait(trait_university_arthistorydegreebs)

    trait_university_biologydegreeba = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_BIOLOGYDEGREEBA, Types.TRAIT))
    if sim.has_trait(trait_university_biologydegreeba):
        sim.remove_trait(trait_university_biologydegreeba)

    trait_university_biologydegreebs = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_BIOLOGYDEGREEBS, Types.TRAIT))
    if sim.has_trait(trait_university_biologydegreebs):
        sim.remove_trait(trait_university_biologydegreebs)

    trait_university_communicationsdegreeba = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_COMMUNICATIONSDEGREEBA, Types.TRAIT))
    if sim.has_trait(trait_university_communicationsdegreeba):
        sim.remove_trait(trait_university_communicationsdegreeba)

    trait_university_communicationsdegreebs = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_COMMUNICATIONSDEGREEBS, Types.TRAIT))
    if sim.has_trait(trait_university_communicationsdegreebs):
        sim.remove_trait(trait_university_communicationsdegreebs)

    trait_university_computersciencedegreeba = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_COMPUTERSCIENCEDEGREEBA, Types.TRAIT))
    if sim.has_trait(trait_university_computersciencedegreeba):
        sim.remove_trait(trait_university_computersciencedegreeba)

    trait_university_computersciencedegreebs = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_COMPUTERSCIENCEDEGREEBS, Types.TRAIT))
    if sim.has_trait(trait_university_computersciencedegreebs):
        sim.remove_trait(trait_university_computersciencedegreebs)

    trait_university_culinaryartsdegreeba = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_CULINARYARTSDEGREEBA, Types.TRAIT))
    if sim.has_trait(trait_university_culinaryartsdegreeba):
        sim.remove_trait(trait_university_culinaryartsdegreeba)

    trait_university_culinaryartsdegreebs = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_CULINARYARTSDEGREEBS, Types.TRAIT))
    if sim.has_trait(trait_university_culinaryartsdegreebs):
        sim.remove_trait(trait_university_culinaryartsdegreebs)

    trait_university_dramadegreeba = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_DRAMADEGREEBA, Types.TRAIT))
    if sim.has_trait(trait_university_dramadegreeba):
        sim.remove_trait(trait_university_dramadegreeba)

    trait_university_dramadegreebs = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_DRAMADEGREEBS, Types.TRAIT))
    if sim.has_trait(trait_university_dramadegreebs):
        sim.remove_trait(trait_university_dramadegreebs)

    trait_university_economicsdegreeba = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_ECONOMICSDEGREEBA, Types.TRAIT))
    if sim.has_trait(trait_university_economicsdegreeba):
        sim.remove_trait(trait_university_economicsdegreeba)

    trait_university_economicsdegreebs = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_ECONOMICSDEGREEBS, Types.TRAIT))
    if sim.has_trait(trait_university_economicsdegreebs):
        sim.remove_trait(trait_university_economicsdegreebs)

    trait_university_fineartdegreeba = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_FINEARTDEGREEBA, Types.TRAIT))
    if sim.has_trait(trait_university_fineartdegreeba):
        sim.remove_trait(trait_university_fineartdegreeba)

    trait_university_fineartdegreebs = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_FINEARTDEGREEBS, Types.TRAIT))
    if sim.has_trait(trait_university_fineartdegreebs):
        sim.remove_trait(trait_university_fineartdegreebs)

    trait_university_historydegreeba = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_HISTORYDEGREEBA, Types.TRAIT))
    if sim.has_trait(trait_university_historydegreeba):
        sim.remove_trait(trait_university_historydegreeba)

    trait_university_historydegreebs = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_HISTORYDEGREEBS, Types.TRAIT))
    if sim.has_trait(trait_university_historydegreebs):
        sim.remove_trait(trait_university_historydegreebs)

    trait_university_languageandliteraturedegreeba = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_LANGUAGEANDLITERATUREDEGREEBA, Types.TRAIT))
    if sim.has_trait(trait_university_languageandliteraturedegreeba):
        sim.remove_trait(trait_university_languageandliteraturedegreeba)

    trait_university_languageandliteraturedegreebs = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_LANGUAGEANDLITERATUREDEGREEBS, Types.TRAIT))
    if sim.has_trait(trait_university_languageandliteraturedegreebs):
        sim.remove_trait(trait_university_languageandliteraturedegreebs)

    trait_university_physicsdegreeba = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_PHYSICSDEGREEBA, Types.TRAIT))
    if sim.has_trait(trait_university_physicsdegreeba):
        sim.remove_trait(trait_university_physicsdegreeba)

    trait_university_physicsdegreebs = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_PHYSICSDEGREEBS, Types.TRAIT))
    if sim.has_trait(trait_university_physicsdegreebs):
        sim.remove_trait(trait_university_physicsdegreebs)

    trait_university_psychologydegreeba = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_PSYCHOLOGYDEGREEBA, Types.TRAIT))
    if sim.has_trait(trait_university_psychologydegreeba):
        sim.remove_trait(trait_university_psychologydegreeba)

    trait_university_psychologydegreebs = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_PSYCHOLOGYDEGREEBS, Types.TRAIT))
    if sim.has_trait(trait_university_psychologydegreebs):
        sim.remove_trait(trait_university_psychologydegreebs)

    trait_university_villainydegreeba = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_VILLAINYDEGREEBA, Types.TRAIT))
    if sim.has_trait(trait_university_villainydegreeba):
        sim.remove_trait(trait_university_villainydegreeba)

    trait_university_villainydegreebs = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_VILLAINYDEGREEBS, Types.TRAIT))
    if sim.has_trait(trait_university_villainydegreebs):
        sim.remove_trait(trait_university_villainydegreebs)

    trait_walkstylecreepy = instance_manager.get(get_resource_key(TRAIT_WALKSTYLECREEPY, Types.TRAIT))
    if sim.has_trait(trait_walkstylecreepy):
        sim.remove_trait(trait_walkstylecreepy)

    trait_walkstyleenergetic = instance_manager.get(get_resource_key(TRAIT_WALKSTYLEENERGETIC, Types.TRAIT))
    if sim.has_trait(trait_walkstyleenergetic):
        sim.remove_trait(trait_walkstyleenergetic)

    trait_walkstyleenergetic = instance_manager.get(get_resource_key(TRAIT_WALKSTYLEENERGETIC, Types.TRAIT))
    if sim.has_trait(trait_walkstyleenergetic):
        sim.remove_trait(trait_walkstyleenergetic)

    trait_walkstylefeminine = instance_manager.get(get_resource_key(TRAIT_WALKSTYLEFEMININE, Types.TRAIT))
    if sim.has_trait(trait_walkstylefeminine):
        sim.remove_trait(trait_walkstylefeminine)

    trait_walkstylegoofy = instance_manager.get(get_resource_key(TRAIT_WALKSTYLEGOOFY, Types.TRAIT))
    if sim.has_trait(trait_walkstylegoofy):
        sim.remove_trait(trait_walkstylegoofy)

    trait_walkstyleperky = instance_manager.get(get_resource_key(TRAIT_WALKSTYLEPERKY, Types.TRAIT))
    if sim.has_trait(trait_walkstyleperky):
        sim.remove_trait(trait_walkstyleperky)

    trait_walkstylesleepy = instance_manager.get(get_resource_key(TRAIT_WALKSTYLESLEEPY, Types.TRAIT))
    if sim.has_trait(trait_walkstylesleepy):
        sim.remove_trait(trait_walkstylesleepy)

    trait_walkstylesnooty = instance_manager.get(get_resource_key(TRAIT_WALKSTYLESNOOTY, Types.TRAIT))
    if sim.has_trait(trait_walkstylesnooty):
        sim.remove_trait(trait_walkstylesnooty)

    trait_walkstyleswagger = instance_manager.get(get_resource_key(TRAIT_WALKSTYLESWAGGER, Types.TRAIT))
    if sim.has_trait(trait_walkstyleswagger):
        sim.remove_trait(trait_walkstyleswagger)

    trait_walkstyletough = instance_manager.get(get_resource_key(TRAIT_WALKSTYLETOUGH, Types.TRAIT))
    if sim.has_trait(trait_walkstyletough):
        sim.remove_trait(trait_walkstyletough)

    trait_waterproof = instance_manager.get(get_resource_key(TRAIT_WATERPROOF, Types.TRAIT))
    if not sim.has_trait(trait_waterproof):
        sim.add_trait(trait_waterproof)

    trait_webmaster = instance_manager.get(get_resource_key(TRAIT_WEBMASTER, Types.TRAIT))
    if not sim.has_trait(trait_webmaster):
        sim.add_trait(trait_webmaster)

    wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_breastslarge = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_BODYSHAPE_BREASTSLARGE, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_breastslarge):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_breastslarge)

    wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_breastssmall = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_BODYSHAPE_BREASTSSMALL, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_breastssmall):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_breastssmall)

    wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_buttlarge = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_BODYSHAPE_BUTTLARGE, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_buttlarge):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_buttlarge)

    wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_buttsmall = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_BODYSHAPE_BUTTSMALL, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_buttsmall):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_buttsmall)

    wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_heavy = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_BODYSHAPE_HEAVY, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_heavy):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_heavy)

    wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_high = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_BODYSHAPE_HIGH, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_high):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_high)

    wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_light = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_BODYSHAPE_LIGHT, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_light):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_light)

    wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_low = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_BODYSHAPE_LOW, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_low):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_low)

    wickedwhims_attractiveness_trait_simpreference_dislikes_detail_body_hair = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_DETAIL_BODY_HAIR, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_detail_body_hair):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_detail_body_hair)

    wickedwhims_attractiveness_trait_simpreference_dislikes_detail_freckles = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_DETAIL_FRECKLES, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_detail_freckles):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_detail_freckles)

    wickedwhims_attractiveness_trait_simpreference_dislikes_detail_glasses = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_DETAIL_GLASSES, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_detail_glasses):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_detail_glasses)

    wickedwhims_attractiveness_trait_simpreference_dislikes_detail_hats = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_DETAIL_HATS, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_detail_hats):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_detail_hats)

    wickedwhims_attractiveness_trait_simpreference_dislikes_detail_jewelery = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_DETAIL_JEWELERY, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_detail_jewelery):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_detail_jewelery)

    wickedwhims_attractiveness_trait_simpreference_dislikes_detail_makeup = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_DETAIL_MAKEUP, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_detail_makeup):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_detail_makeup)

    wickedwhims_attractiveness_trait_simpreference_dislikes_detail_piercing = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_DETAIL_PIERCING, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_detail_piercing):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_detail_piercing)

    wickedwhims_attractiveness_trait_simpreference_dislikes_detail_tattoos = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_DETAIL_TATTOOS, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_detail_tattoos):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_detail_tattoos)

    wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_blue = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_EYECOLOR_BLUE, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_blue):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_blue)

    wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_blue = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_EYECOLOR_BLUE, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_blue):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_blue)

    wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_brown = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_EYECOLOR_BROWN, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_brown):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_brown)

    wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_brown = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_EYECOLOR_BROWN, Types.TRAIT))
    if not sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_brown):
        sim.add_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_brown)

    wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_green = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_EYECOLOR_GREEN, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_green):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_green)

    wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_green = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_EYECOLOR_GREEN, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_green):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_green)

    wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_unnatural = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_EYECOLOR_UNNATURAL, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_unnatural):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_unnatural)

    wickedwhims_attractiveness_trait_simpreference_dislikes_facialhair_beard = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_FACIALHAIR_BEARD, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_facialhair_beard):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_facialhair_beard)

    wickedwhims_attractiveness_trait_simpreference_dislikes_facialhair_clean = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_FACIALHAIR_CLEAN, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_facialhair_clean):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_facialhair_clean)

    wickedwhims_attractiveness_trait_simpreference_dislikes_facialhair_goatee = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_FACIALHAIR_GOATEE, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_facialhair_goatee):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_facialhair_goatee)

    wickedwhims_attractiveness_trait_simpreference_dislikes_facialhair_mustache = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_FACIALHAIR_MUSTACHE, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_facialhair_mustache):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_facialhair_mustache)

    wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_black = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_HAIRCOLOR_BLACK, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_black):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_black)

    wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_blonde = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_HAIRCOLOR_BLONDE, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_blonde):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_blonde)

    wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_blonde = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_HAIRCOLOR_BLONDE, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_blonde):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_blonde)

    wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_blue = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_HAIRCOLOR_BLUE, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_blue):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_blue)

    wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_blue = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_HAIRCOLOR_BLUE, Types.TRAIT))
    if not sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_blue):
        sim.add_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_blue)

    wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_brown = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_HAIRCOLOR_BROWN, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_brown):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_brown)

    wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_brown = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_HAIRCOLOR_BROWN, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_brown):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_brown)

    wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_gray = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_HAIRCOLOR_GRAY, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_gray):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_gray)

    wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_green = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_HAIRCOLOR_GREEN, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_green):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_green)

    wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_green = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_HAIRCOLOR_GREEN, Types.TRAIT))
    if not sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_green):
        sim.add_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_green)

    wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_pink = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_HAIRCOLOR_PINK, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_pink):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_pink)

    wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_red = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_HAIRCOLOR_RED, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_red):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_red)

    wickedwhims_attractiveness_trait_simpreference_dislikes_hairlength_bald = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_HAIRLENGTH_BALD, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_hairlength_bald):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_hairlength_bald)

    wickedwhims_attractiveness_trait_simpreference_dislikes_hairlength_bald = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_HAIRLENGTH_BALD, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_hairlength_bald):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_hairlength_bald)

    wickedwhims_attractiveness_trait_simpreference_dislikes_hairlength_long = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_HAIRLENGTH_LONG, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_hairlength_long):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_hairlength_long)

    wickedwhims_attractiveness_trait_simpreference_dislikes_hairlength_medium = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_HAIRLENGTH_MEDIUM, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_hairlength_medium):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_hairlength_medium)

    wickedwhims_attractiveness_trait_simpreference_dislikes_hairlength_short = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_HAIRLENGTH_SHORT, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_hairlength_short):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_hairlength_short)

    wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_breastslarge = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_BODYSHAPE_BREASTSLARGE, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_breastslarge):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_breastslarge)

    wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_breastssmall = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_BODYSHAPE_BREASTSSMALL, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_breastssmall):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_breastssmall)

    wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_breastssmall = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_BODYSHAPE_BREASTSSMALL, Types.TRAIT))
    if not sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_breastssmall):
        sim.add_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_breastssmall)

    wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_buttlarge = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_BODYSHAPE_BUTTLARGE, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_buttlarge):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_buttlarge)

    wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_buttlarge = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_BODYSHAPE_BUTTLARGE, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_buttlarge):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_buttlarge)

    wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_buttsmall = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_BODYSHAPE_BUTTSMALL, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_buttsmall):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_buttsmall)

    wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_buttsmall = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_BODYSHAPE_BUTTSMALL, Types.TRAIT))
    if not sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_buttsmall):
        sim.add_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_buttsmall)

    wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_heavy = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_BODYSHAPE_HEAVY, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_heavy):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_heavy)

    wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_high = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_BODYSHAPE_HIGH, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_high):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_high)

    wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_light = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_BODYSHAPE_LIGHT, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_light):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_light)

    wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_low = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_BODYSHAPE_LOW, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_low):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_low)

    wickedwhims_attractiveness_trait_simpreference_likes_detail_body_hair = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_DETAIL_BODY_HAIR, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_body_hair):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_body_hair)

    wickedwhims_attractiveness_trait_simpreference_likes_detail_freckles = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_DETAIL_FRECKLES, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_freckles):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_freckles)

    wickedwhims_attractiveness_trait_simpreference_likes_detail_glasses = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_DETAIL_GLASSES, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_glasses):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_glasses)

    wickedwhims_attractiveness_trait_simpreference_likes_detail_glasses = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_DETAIL_GLASSES, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_glasses):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_glasses)

    wickedwhims_attractiveness_trait_simpreference_likes_detail_hats = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_DETAIL_HATS, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_hats):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_hats)

    wickedwhims_attractiveness_trait_simpreference_likes_detail_hats = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_DETAIL_HATS, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_hats):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_hats)

    wickedwhims_attractiveness_trait_simpreference_likes_detail_jewelery = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_DETAIL_JEWELERY, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_jewelery):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_jewelery)

    wickedwhims_attractiveness_trait_simpreference_likes_detail_makeup = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_DETAIL_MAKEUP, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_makeup):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_makeup)

    wickedwhims_attractiveness_trait_simpreference_likes_detail_piercing = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_DETAIL_PIERCING, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_piercing):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_piercing)

    wickedwhims_attractiveness_trait_simpreference_likes_detail_tattoos = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_DETAIL_TATTOOS, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_tattoos):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_tattoos)

    wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_blue = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_EYECOLOR_BLUE, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_blue):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_blue)

    wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_blue = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_EYECOLOR_BLUE, Types.TRAIT))
    if not sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_blue):
        sim.add_trait(wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_blue)

    wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_brown = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_EYECOLOR_BROWN, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_brown):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_brown)

    wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_brown = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_EYECOLOR_BROWN, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_brown):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_brown)

    wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_green = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_EYECOLOR_GREEN, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_green):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_green)

    wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_green = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_EYECOLOR_GREEN, Types.TRAIT))
    if not sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_green):
        sim.add_trait(wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_green)

    wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_unnatural = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_EYECOLOR_UNNATURAL, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_unnatural):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_unnatural)

    wickedwhims_attractiveness_trait_simpreference_likes_facialhair_beard = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_FACIALHAIR_BEARD, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_facialhair_beard):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_facialhair_beard)

    wickedwhims_attractiveness_trait_simpreference_likes_facialhair_clean = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_FACIALHAIR_CLEAN, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_facialhair_clean):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_facialhair_clean)

    wickedwhims_attractiveness_trait_simpreference_likes_facialhair_goatee = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_FACIALHAIR_GOATEE, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_facialhair_goatee):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_facialhair_goatee)

    wickedwhims_attractiveness_trait_simpreference_likes_facialhair_mustache = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_FACIALHAIR_MUSTACHE, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_facialhair_mustache):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_facialhair_mustache)

    wickedwhims_attractiveness_trait_simpreference_likes_haircolor_black = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_HAIRCOLOR_BLACK, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_black):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_black)

    wickedwhims_attractiveness_trait_simpreference_likes_haircolor_blonde = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_HAIRCOLOR_BLONDE, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_blonde):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_blonde)

    wickedwhims_attractiveness_trait_simpreference_likes_haircolor_blonde = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_HAIRCOLOR_BLONDE, Types.TRAIT))
    if not sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_blonde):
        sim.add_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_blonde)

    wickedwhims_attractiveness_trait_simpreference_likes_haircolor_blue = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_HAIRCOLOR_BLUE, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_blue):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_blue)

    wickedwhims_attractiveness_trait_simpreference_likes_haircolor_brown = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_HAIRCOLOR_BROWN, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_brown):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_brown)

    wickedwhims_attractiveness_trait_simpreference_likes_haircolor_brown = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_HAIRCOLOR_BROWN, Types.TRAIT))
    if not sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_brown):
        sim.add_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_brown)

    wickedwhims_attractiveness_trait_simpreference_likes_haircolor_gray = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_HAIRCOLOR_GRAY, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_gray):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_gray)

    wickedwhims_attractiveness_trait_simpreference_likes_haircolor_green = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_HAIRCOLOR_GREEN, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_green):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_green)

    wickedwhims_attractiveness_trait_simpreference_likes_haircolor_pink = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_HAIRCOLOR_PINK, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_pink):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_pink)

    wickedwhims_attractiveness_trait_simpreference_likes_haircolor_red = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_HAIRCOLOR_RED, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_red):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_red)

    wickedwhims_attractiveness_trait_simpreference_likes_hairlength_bald = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_HAIRLENGTH_BALD, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_hairlength_bald):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_hairlength_bald)

    wickedwhims_attractiveness_trait_simpreference_likes_hairlength_long = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_HAIRLENGTH_LONG, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_hairlength_long):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_hairlength_long)

    wickedwhims_attractiveness_trait_simpreference_likes_hairlength_medium = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_HAIRLENGTH_MEDIUM, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_hairlength_medium):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_hairlength_medium)

    wickedwhims_attractiveness_trait_simpreference_likes_hairlength_short = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_HAIRLENGTH_SHORT, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_hairlength_short):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_hairlength_short)

    wickedwhims_trait_attractivenessblacklist = instance_manager.get(get_resource_key(WICKEDWHIMS_TRAIT_ATTRACTIVENESSBLACKLIST, Types.TRAIT))
    if sim.has_trait(wickedwhims_trait_attractivenessblacklist):
        sim.remove_trait(wickedwhims_trait_attractivenessblacklist)

    wickedwhims_trait_bodyhair_pubichair_isdisabled = instance_manager.get(get_resource_key(WICKEDWHIMS_TRAIT_BODYHAIR_PUBICHAIR_ISDISABLED, Types.TRAIT))
    if not sim.has_trait(wickedwhims_trait_bodyhair_pubichair_isdisabled):
        sim.add_trait(wickedwhims_trait_bodyhair_pubichair_isdisabled)

    wickedwhims_trait_bodyhair_pubichair_isgrowthdisabled = instance_manager.get(get_resource_key(WICKEDWHIMS_TRAIT_BODYHAIR_PUBICHAIR_ISGROWTHDISABLED, Types.TRAIT))
    if not sim.has_trait(wickedwhims_trait_bodyhair_pubichair_isgrowthdisabled):
        sim.add_trait(wickedwhims_trait_bodyhair_pubichair_isgrowthdisabled)

    wickedwhims_trait_cumslut = instance_manager.get(get_resource_key(WICKEDWHIMS_TRAIT_CUMSLUT, Types.TRAIT))
    if not sim.has_trait(wickedwhims_trait_cumslut):
        sim.add_trait(wickedwhims_trait_cumslut)

    wickedwhims_trait_improved_absorbency = instance_manager.get(get_resource_key(WICKEDWHIMS_TRAIT_IMPROVED_ABSORBENCY, Types.TRAIT))
    if not sim.has_trait(wickedwhims_trait_improved_absorbency):
        sim.add_trait(wickedwhims_trait_improved_absorbency)

    wickedwhims_trait_postpubertyteen = instance_manager.get(get_resource_key(WICKEDWHIMS_TRAIT_POSTPUBERTYTEEN, Types.TRAIT))
    if not sim.has_trait(wickedwhims_trait_postpubertyteen):
        sim.add_trait(wickedwhims_trait_postpubertyteen)

    wickedwhims_trait_sex_attribute_badatsex = instance_manager.get(get_resource_key(WICKEDWHIMS_TRAIT_SEX_ATTRIBUTE_BADATSEX, Types.TRAIT))
    if sim.has_trait(wickedwhims_trait_sex_attribute_badatsex):
        sim.remove_trait(wickedwhims_trait_sex_attribute_badatsex)

    wickedwhims_trait_sex_sexuallyabstinent = instance_manager.get(get_resource_key(WICKEDWHIMS_TRAIT_SEX_SEXUALLYABSTINENT, Types.TRAIT))
    if sim.has_trait(wickedwhims_trait_sex_sexuallyabstinent):
        sim.remove_trait(wickedwhims_trait_sex_sexuallyabstinent)


@sims4.commands.Command('pbs_maid', command_type=sims4.commands.CommandType.Live)
def pbs_maid(_connection=None):
    # Get the console output
    output = sims4.commands.CheatOutput(_connection)

    # Get the sim_info for the active sim
    sim = services.client_manager().get(_connection).active_sim.sim_info

    # Get the tuned trait instance from the tuning instance manager
    instance_manager = services.get_instance_manager(Types.TRAIT)

    # Remove or add traits from all sims
    archaeologyskill_giveauthenticationmail_prohibit = instance_manager.get(get_resource_key(ARCHAEOLOGYSKILL_GIVEAUTHENTICATIONMAIL_PROHIBIT, Types.TRAIT))
    if not sim.has_trait(archaeologyskill_giveauthenticationmail_prohibit):
        sim.add_trait(archaeologyskill_giveauthenticationmail_prohibit)

    fametraits_celebritywalk_on = instance_manager.get(get_resource_key(FAMETRAITS_CELEBRITYWALK_ON, Types.TRAIT))
    if sim.has_trait(fametraits_celebritywalk_on):
        sim.remove_trait(fametraits_celebritywalk_on)

    fametraits_shine_off = instance_manager.get(get_resource_key(FAMETRAITS_SHINE_OFF, Types.TRAIT))
    if not sim.has_trait(fametraits_shine_off):
        sim.add_trait(fametraits_shine_off)

    fametraits_shine_on_rank4 = instance_manager.get(get_resource_key(FAMETRAITS_SHINE_ON_RANK4, Types.TRAIT))
    if sim.has_trait(fametraits_shine_on_rank4):
        sim.remove_trait(fametraits_shine_on_rank4)

    fametraits_shine_on_rank5 = instance_manager.get(get_resource_key(FAMETRAITS_SHINE_ON_RANK5, Types.TRAIT))
    if sim.has_trait(fametraits_shine_on_rank5):
        sim.remove_trait(fametraits_shine_on_rank5)

    trait_computerglasses_wearing = instance_manager.get(get_resource_key(TRAIT_COMPUTERGLASSES_WEARING, Types.TRAIT))
    if sim.has_trait(trait_computerglasses_wearing):
        sim.remove_trait(trait_computerglasses_wearing)

    trait_computerglasses_wearing_blue = instance_manager.get(get_resource_key(TRAIT_COMPUTERGLASSES_WEARING_BLUE, Types.TRAIT))
    if sim.has_trait(trait_computerglasses_wearing_blue):
        sim.remove_trait(trait_computerglasses_wearing_blue)

    trait_computerglasses_wearing_green = instance_manager.get(get_resource_key(TRAIT_COMPUTERGLASSES_WEARING_GREEN, Types.TRAIT))
    if sim.has_trait(trait_computerglasses_wearing_green):
        sim.remove_trait(trait_computerglasses_wearing_green)

    trait_computerglasses_wearing_orange = instance_manager.get(get_resource_key(TRAIT_COMPUTERGLASSES_WEARING_ORANGE, Types.TRAIT))
    if sim.has_trait(trait_computerglasses_wearing_orange):
        sim.remove_trait(trait_computerglasses_wearing_orange)

    trait_computerglasses_wearing_pink = instance_manager.get(get_resource_key(TRAIT_COMPUTERGLASSES_WEARING_PINK, Types.TRAIT))
    if sim.has_trait(trait_computerglasses_wearing_pink):
        sim.remove_trait(trait_computerglasses_wearing_pink)

    trait_computerglasses_wearing_red = instance_manager.get(get_resource_key(TRAIT_COMPUTERGLASSES_WEARING_RED, Types.TRAIT))
    if sim.has_trait(trait_computerglasses_wearing_red):
        sim.remove_trait(trait_computerglasses_wearing_red)

    trait_computerglasses_wearing_yellow = instance_manager.get(get_resource_key(TRAIT_COMPUTERGLASSES_WEARING_YELLOW, Types.TRAIT))
    if sim.has_trait(trait_computerglasses_wearing_yellow):
        sim.remove_trait(trait_computerglasses_wearing_yellow)

    trait_crystalhelmet_alabaster = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_ALABASTER, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_alabaster):
        sim.remove_trait(trait_crystalhelmet_alabaster)

    trait_crystalhelmet_alexandrite_ep = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_ALEXANDRITE_EP, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_alexandrite_ep):
        sim.remove_trait(trait_crystalhelmet_alexandrite_ep)

    trait_crystalhelmet_amazonite_ep = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_AMAZONITE_EP, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_amazonite_ep):
        sim.remove_trait(trait_crystalhelmet_amazonite_ep)

    trait_crystalhelmet_amethyst = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_AMETHYST, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_amethyst):
        sim.remove_trait(trait_crystalhelmet_amethyst)

    trait_crystalhelmet_citrine = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_CITRINE, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_citrine):
        sim.remove_trait(trait_crystalhelmet_citrine)

    trait_crystalhelmet_crandestine_ep = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_CRANDESTINE_EP, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_crandestine_ep):
        sim.remove_trait(trait_crystalhelmet_crandestine_ep)

    trait_crystalhelmet_diamond = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_DIAMOND, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_diamond):
        sim.remove_trait(trait_crystalhelmet_diamond)

    trait_crystalhelmet_emerald = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_EMERALD, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_emerald):
        sim.remove_trait(trait_crystalhelmet_emerald)

    trait_crystalhelmet_fireopal = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_FIREOPAL, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_fireopal):
        sim.remove_trait(trait_crystalhelmet_fireopal)

    trait_crystalhelmet_hematite = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_HEMATITE, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_hematite):
        sim.remove_trait(trait_crystalhelmet_hematite)

    trait_crystalhelmet_jet = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_JET, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_jet):
        sim.remove_trait(trait_crystalhelmet_jet)

    trait_crystalhelmet_jonquilyst = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_JONQUILYST, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_jonquilyst):
        sim.remove_trait(trait_crystalhelmet_jonquilyst)

    trait_crystalhelmet_nitelite_ep = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_NITELITE_EP, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_nitelite_ep):
        sim.remove_trait(trait_crystalhelmet_nitelite_ep)

    trait_crystalhelmet_orangetopaz = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_ORANGETOPAZ, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_orangetopaz):
        sim.remove_trait(trait_crystalhelmet_orangetopaz)

    trait_crystalhelmet_peach = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_PEACH, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_peach):
        sim.remove_trait(trait_crystalhelmet_peach)

    trait_crystalhelmet_plumbite = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_PLUMBITE, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_plumbite):
        sim.remove_trait(trait_crystalhelmet_plumbite)

    trait_crystalhelmet_quartz = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_QUARTZ, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_quartz):
        sim.remove_trait(trait_crystalhelmet_quartz)

    trait_crystalhelmet_rainborz = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_RAINBORZ, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_rainborz):
        sim.remove_trait(trait_crystalhelmet_rainborz)

    trait_crystalhelmet_rose = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_ROSE, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_rose):
        sim.remove_trait(trait_crystalhelmet_rose)

    trait_crystalhelmet_ruby = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_RUBY, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_ruby):
        sim.remove_trait(trait_crystalhelmet_ruby)

    trait_crystalhelmet_sapphire = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_SAPPHIRE, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_sapphire):
        sim.remove_trait(trait_crystalhelmet_sapphire)

    trait_crystalhelmet_shinalite = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_SHINALITE, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_shinalite):
        sim.remove_trait(trait_crystalhelmet_shinalite)

    trait_crystalhelmet_simanite = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_SIMANITE, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_simanite):
        sim.remove_trait(trait_crystalhelmet_simanite)

    trait_crystalhelmet_turquoise = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_TURQUOISE, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_turquoise):
        sim.remove_trait(trait_crystalhelmet_turquoise)

    trait_doctor_sicknessresistant = instance_manager.get(get_resource_key(TRAIT_DOCTOR_SICKNESSRESISTANT, Types.TRAIT))
    if not sim.has_trait(trait_doctor_sicknessresistant):
        sim.add_trait(trait_doctor_sicknessresistant)

    trait_essenceofflavor = instance_manager.get(get_resource_key(TRAIT_ESSENCEOFFLAVOR, Types.TRAIT))
    if not sim.has_trait(trait_essenceofflavor):
        sim.add_trait(trait_essenceofflavor)

    trait_fear_beingcheatedon = instance_manager.get(get_resource_key(TRAIT_FEAR_BEINGCHEATEDON, Types.TRAIT))
    if sim.has_trait(trait_fear_beingcheatedon):
        sim.remove_trait(trait_fear_beingcheatedon)

    trait_fear_beingjudged = instance_manager.get(get_resource_key(TRAIT_FEAR_BEINGJUDGED, Types.TRAIT))
    if sim.has_trait(trait_fear_beingjudged):
        sim.remove_trait(trait_fear_beingjudged)

    trait_fear_cowplant = instance_manager.get(get_resource_key(TRAIT_FEAR_COWPLANT, Types.TRAIT))
    if sim.has_trait(trait_fear_cowplant):
        sim.remove_trait(trait_fear_cowplant)

    trait_fear_crowdedplaces = instance_manager.get(get_resource_key(TRAIT_FEAR_CROWDEDPLACES, Types.TRAIT))
    if sim.has_trait(trait_fear_crowdedplaces):
        sim.remove_trait(trait_fear_crowdedplaces)

    trait_fear_dark = instance_manager.get(get_resource_key(TRAIT_FEAR_DARK, Types.TRAIT))
    if sim.has_trait(trait_fear_dark):
        sim.remove_trait(trait_fear_dark)

    trait_fear_deadendjob = instance_manager.get(get_resource_key(TRAIT_FEAR_DEADENDJOB, Types.TRAIT))
    if sim.has_trait(trait_fear_deadendjob):
        sim.remove_trait(trait_fear_deadendjob)

    trait_fear_death = instance_manager.get(get_resource_key(TRAIT_FEAR_DEATH, Types.TRAIT))
    if sim.has_trait(trait_fear_death):
        sim.remove_trait(trait_fear_death)

    trait_fear_disappointingparents = instance_manager.get(get_resource_key(TRAIT_FEAR_DISAPPOINTINGPARENTS, Types.TRAIT))
    if sim.has_trait(trait_fear_disappointingparents):
        sim.remove_trait(trait_fear_disappointingparents)

    trait_fear_disappointingparents_parentdeceasedflag = instance_manager.get(get_resource_key(TRAIT_FEAR_DISAPPOINTINGPARENTS_PARENTDECEASEDFLAG, Types.TRAIT))
    if sim.has_trait(trait_fear_disappointingparents_parentdeceasedflag):
        sim.remove_trait(trait_fear_disappointingparents_parentdeceasedflag)

    trait_fear_failing_afterschoolactivities = instance_manager.get(get_resource_key(TRAIT_FEAR_FAILING_AFTERSCHOOLACTIVITIES, Types.TRAIT))
    if sim.has_trait(trait_fear_failing_afterschoolactivities):
        sim.remove_trait(trait_fear_failing_afterschoolactivities)

    trait_fear_failing_class = instance_manager.get(get_resource_key(TRAIT_FEAR_FAILING_CLASS, Types.TRAIT))
    if sim.has_trait(trait_fear_failing_class):
        sim.remove_trait(trait_fear_failing_class)

    trait_fear_failing_tests = instance_manager.get(get_resource_key(TRAIT_FEAR_FAILING_TESTS, Types.TRAIT))
    if sim.has_trait(trait_fear_failing_tests):
        sim.remove_trait(trait_fear_failing_tests)

    trait_fear_failure = instance_manager.get(get_resource_key(TRAIT_FEAR_FAILURE, Types.TRAIT))
    if sim.has_trait(trait_fear_failure):
        sim.remove_trait(trait_fear_failure)

    trait_fear_fire = instance_manager.get(get_resource_key(TRAIT_FEAR_FIRE, Types.TRAIT))
    if sim.has_trait(trait_fear_fire):
        sim.remove_trait(trait_fear_fire)

    trait_fear_ghosts = instance_manager.get(get_resource_key(TRAIT_FEAR_GHOSTS, Types.TRAIT))
    if sim.has_trait(trait_fear_ghosts):
        sim.remove_trait(trait_fear_ghosts)

    trait_fear_homework = instance_manager.get(get_resource_key(TRAIT_FEAR_HOMEWORK, Types.TRAIT))
    if sim.has_trait(trait_fear_homework):
        sim.remove_trait(trait_fear_homework)

    trait_fear_swimming = instance_manager.get(get_resource_key(TRAIT_FEAR_SWIMMING, Types.TRAIT))
    if sim.has_trait(trait_fear_swimming):
        sim.remove_trait(trait_fear_swimming)

    trait_fear_unfulfilled = instance_manager.get(get_resource_key(TRAIT_FEAR_UNFULFILLED, Types.TRAIT))
    if sim.has_trait(trait_fear_unfulfilled):
        sim.remove_trait(trait_fear_unfulfilled)

    trait_filthdweller = instance_manager.get(get_resource_key(TRAIT_FILTHDWELLER, Types.TRAIT))
    if sim.has_trait(trait_filthdweller):
        sim.remove_trait(trait_filthdweller)

    trait_freeservices = instance_manager.get(get_resource_key(TRAIT_FREESERVICES, Types.TRAIT))
    if not sim.has_trait(trait_freeservices):
        sim.add_trait(trait_freeservices)

    trait_frugal = instance_manager.get(get_resource_key(TRAIT_FRUGAL, Types.TRAIT))
    if not sim.has_trait(trait_frugal):
        sim.add_trait(trait_frugal)

    trait_genderoptions_attractedto_notfemale = instance_manager.get(get_resource_key(TRAIT_GENDEROPTIONS_ATTRACTEDTO_NOTFEMALE, Types.TRAIT))
    if sim.has_trait(trait_genderoptions_attractedto_notfemale):
        sim.remove_trait(trait_genderoptions_attractedto_notfemale)

    trait_genderoptions_attractedto_notmale = instance_manager.get(get_resource_key(TRAIT_GENDEROPTIONS_ATTRACTEDTO_NOTMALE, Types.TRAIT))
    if sim.has_trait(trait_genderoptions_attractedto_notmale):
        sim.remove_trait(trait_genderoptions_attractedto_notmale)

    trait_genderoptions_sexuality_exploring = instance_manager.get(get_resource_key(TRAIT_GENDEROPTIONS_SEXUALITY_EXPLORING, Types.TRAIT))
    if not sim.has_trait(trait_genderoptions_sexuality_exploring):
        sim.add_trait(trait_genderoptions_sexuality_exploring)

    trait_genderoptions_sexuality_notexploring = instance_manager.get(get_resource_key(TRAIT_GENDEROPTIONS_SEXUALITY_NOTEXPLORING, Types.TRAIT))
    if sim.has_trait(trait_genderoptions_sexuality_notexploring):
        sim.remove_trait(trait_genderoptions_sexuality_notexploring)

    trait_glutton = instance_manager.get(get_resource_key(TRAIT_GLUTTON, Types.TRAIT))
    if sim.has_trait(trait_glutton):
        sim.remove_trait(trait_glutton)

    trait_gradeschool_a = instance_manager.get(get_resource_key(TRAIT_GRADESCHOOL_A, Types.TRAIT))
    if not sim.has_trait(trait_gradeschool_a):
        sim.add_trait(trait_gradeschool_a)

    trait_gradeschool_b = instance_manager.get(get_resource_key(TRAIT_GRADESCHOOL_B, Types.TRAIT))
    if sim.has_trait(trait_gradeschool_b):
        sim.remove_trait(trait_gradeschool_b)

    trait_gradeschool_c = instance_manager.get(get_resource_key(TRAIT_GRADESCHOOL_C, Types.TRAIT))
    if sim.has_trait(trait_gradeschool_c):
        sim.remove_trait(trait_gradeschool_c)

    trait_gradeschool_d = instance_manager.get(get_resource_key(TRAIT_GRADESCHOOL_D, Types.TRAIT))
    if sim.has_trait(trait_gradeschool_d):
        sim.remove_trait(trait_gradeschool_d)

    trait_gradeschool_f = instance_manager.get(get_resource_key(TRAIT_GRADESCHOOL_F, Types.TRAIT))
    if sim.has_trait(trait_gradeschool_f):
        sim.remove_trait(trait_gradeschool_f)

    trait_highschool_a = instance_manager.get(get_resource_key(TRAIT_HIGHSCHOOL_A, Types.TRAIT))
    if not sim.has_trait(trait_highschool_a):
        sim.add_trait(trait_highschool_a)

    trait_highschool_b = instance_manager.get(get_resource_key(TRAIT_HIGHSCHOOL_B, Types.TRAIT))
    if sim.has_trait(trait_highschool_b):
        sim.remove_trait(trait_highschool_b)

    trait_highschool_c = instance_manager.get(get_resource_key(TRAIT_HIGHSCHOOL_C, Types.TRAIT))
    if sim.has_trait(trait_highschool_c):
        sim.remove_trait(trait_highschool_c)

    trait_highschool_d = instance_manager.get(get_resource_key(TRAIT_HIGHSCHOOL_D, Types.TRAIT))
    if sim.has_trait(trait_highschool_d):
        sim.remove_trait(trait_highschool_d)

    trait_highschool_f = instance_manager.get(get_resource_key(TRAIT_HIGHSCHOOL_F, Types.TRAIT))
    if sim.has_trait(trait_highschool_f):
        sim.remove_trait(trait_highschool_f)

    trait_hotheaded = instance_manager.get(get_resource_key(TRAIT_HOTHEADED, Types.TRAIT))
    if sim.has_trait(trait_hotheaded):
        sim.remove_trait(trait_hotheaded)

    trait_hsexit_expelled = instance_manager.get(get_resource_key(TRAIT_HSEXIT_EXPELLED, Types.TRAIT))
    if sim.has_trait(trait_hsexit_expelled):
        sim.remove_trait(trait_hsexit_expelled)

    trait_insane = instance_manager.get(get_resource_key(TRAIT_INSANE, Types.TRAIT))
    if sim.has_trait(trait_insane):
        sim.remove_trait(trait_insane)

    trait_invested = instance_manager.get(get_resource_key(TRAIT_INVESTED, Types.TRAIT))
    if not sim.has_trait(trait_invested):
        sim.add_trait(trait_invested)

    trait_ispregnant = instance_manager.get(get_resource_key(TRAIT_ISPREGNANT, Types.TRAIT))
    if sim.has_trait(trait_ispregnant):
        sim.remove_trait(trait_ispregnant)

    trait_mechanicalsuit_hoverengaged = instance_manager.get(get_resource_key(TRAIT_MECHANICALSUIT_HOVERENGAGED, Types.TRAIT))
    if sim.has_trait(trait_mechanicalsuit_hoverengaged):
        sim.remove_trait(trait_mechanicalsuit_hoverengaged)

    trait_mechanicalsuit_wearing_body_beigewhite = instance_manager.get(get_resource_key(TRAIT_MECHANICALSUIT_WEARING_BODY_BEIGEWHITE, Types.TRAIT))
    if sim.has_trait(trait_mechanicalsuit_wearing_body_beigewhite):
        sim.remove_trait(trait_mechanicalsuit_wearing_body_beigewhite)

    trait_mechanicalsuit_wearing_body_blackblue = instance_manager.get(get_resource_key(TRAIT_MECHANICALSUIT_WEARING_BODY_BLACKBLUE, Types.TRAIT))
    if sim.has_trait(trait_mechanicalsuit_wearing_body_blackblue):
        sim.remove_trait(trait_mechanicalsuit_wearing_body_blackblue)

    trait_mechanicalsuit_wearing_body_bluered = instance_manager.get(get_resource_key(TRAIT_MECHANICALSUIT_WEARING_BODY_BLUERED, Types.TRAIT))
    if sim.has_trait(trait_mechanicalsuit_wearing_body_bluered):
        sim.remove_trait(trait_mechanicalsuit_wearing_body_bluered)

    trait_mechanicalsuit_wearing_body_graybrown = instance_manager.get(get_resource_key(TRAIT_MECHANICALSUIT_WEARING_BODY_GRAYBROWN, Types.TRAIT))
    if sim.has_trait(trait_mechanicalsuit_wearing_body_graybrown):
        sim.remove_trait(trait_mechanicalsuit_wearing_body_graybrown)

    trait_mechanicalsuit_wearing_body_greenbrown = instance_manager.get(get_resource_key(TRAIT_MECHANICALSUIT_WEARING_BODY_GREENBROWN, Types.TRAIT))
    if sim.has_trait(trait_mechanicalsuit_wearing_body_greenbrown):
        sim.remove_trait(trait_mechanicalsuit_wearing_body_greenbrown)

    trait_mechanicalsuit_wearing_body_redgreen = instance_manager.get(get_resource_key(TRAIT_MECHANICALSUIT_WEARING_BODY_REDGREEN, Types.TRAIT))
    if sim.has_trait(trait_mechanicalsuit_wearing_body_redgreen):
        sim.remove_trait(trait_mechanicalsuit_wearing_body_redgreen)

    trait_mechanicalsuit_wearing_body_whitecopper = instance_manager.get(get_resource_key(TRAIT_MECHANICALSUIT_WEARING_BODY_WHITECOPPER, Types.TRAIT))
    if sim.has_trait(trait_mechanicalsuit_wearing_body_whitecopper):
        sim.remove_trait(trait_mechanicalsuit_wearing_body_whitecopper)

    trait_mechanicalsuit_wearing_helmet_blackblue = instance_manager.get(get_resource_key(TRAIT_MECHANICALSUIT_WEARING_HELMET_BLACKBLUE, Types.TRAIT))
    if sim.has_trait(trait_mechanicalsuit_wearing_helmet_blackblue):
        sim.remove_trait(trait_mechanicalsuit_wearing_helmet_blackblue)

    trait_mechanicalsuit_wearing_helmet_blackcopper = instance_manager.get(get_resource_key(TRAIT_MECHANICALSUIT_WEARING_HELMET_BLACKCOPPER, Types.TRAIT))
    if sim.has_trait(trait_mechanicalsuit_wearing_helmet_blackcopper):
        sim.remove_trait(trait_mechanicalsuit_wearing_helmet_blackcopper)

    trait_mechanicalsuit_wearing_helmet_blackgold = instance_manager.get(get_resource_key(TRAIT_MECHANICALSUIT_WEARING_HELMET_BLACKGOLD, Types.TRAIT))
    if sim.has_trait(trait_mechanicalsuit_wearing_helmet_blackgold):
        sim.remove_trait(trait_mechanicalsuit_wearing_helmet_blackgold)

    trait_mechanicalsuit_wearing_helmet_blackgray = instance_manager.get(get_resource_key(TRAIT_MECHANICALSUIT_WEARING_HELMET_BLACKGRAY, Types.TRAIT))
    if sim.has_trait(trait_mechanicalsuit_wearing_helmet_blackgray):
        sim.remove_trait(trait_mechanicalsuit_wearing_helmet_blackgray)

    trait_mechanicalsuit_wearing_helmet_bluegray = instance_manager.get(get_resource_key(TRAIT_MECHANICALSUIT_WEARING_HELMET_BLUEGRAY, Types.TRAIT))
    if sim.has_trait(trait_mechanicalsuit_wearing_helmet_bluegray):
        sim.remove_trait(trait_mechanicalsuit_wearing_helmet_bluegray)

    trait_mechanicalsuit_wearing_helmet_grayblack = instance_manager.get(get_resource_key(TRAIT_MECHANICALSUIT_WEARING_HELMET_GRAYBLACK, Types.TRAIT))
    if sim.has_trait(trait_mechanicalsuit_wearing_helmet_grayblack):
        sim.remove_trait(trait_mechanicalsuit_wearing_helmet_grayblack)

    trait_mechanicalsuit_wearing_helmet_greenblack = instance_manager.get(get_resource_key(TRAIT_MECHANICALSUIT_WEARING_HELMET_GREENBLACK, Types.TRAIT))
    if sim.has_trait(trait_mechanicalsuit_wearing_helmet_greenblack):
        sim.remove_trait(trait_mechanicalsuit_wearing_helmet_greenblack)

    trait_nightowl_crystalhelmet = instance_manager.get(get_resource_key(TRAIT_NIGHTOWL_CRYSTALHELMET, Types.TRAIT))
    if sim.has_trait(trait_nightowl_crystalhelmet):
        sim.remove_trait(trait_nightowl_crystalhelmet)

    trait_roboticsarm_wearing_beigewhite = instance_manager.get(get_resource_key(TRAIT_ROBOTICSARM_WEARING_BEIGEWHITE, Types.TRAIT))
    if sim.has_trait(trait_roboticsarm_wearing_beigewhite):
        sim.remove_trait(trait_roboticsarm_wearing_beigewhite)

    trait_roboticsarm_wearing_blackblue = instance_manager.get(get_resource_key(TRAIT_ROBOTICSARM_WEARING_BLACKBLUE, Types.TRAIT))
    if sim.has_trait(trait_roboticsarm_wearing_blackblue):
        sim.remove_trait(trait_roboticsarm_wearing_blackblue)

    trait_roboticsarm_wearing_bluered = instance_manager.get(get_resource_key(TRAIT_ROBOTICSARM_WEARING_BLUERED, Types.TRAIT))
    if sim.has_trait(trait_roboticsarm_wearing_bluered):
        sim.remove_trait(trait_roboticsarm_wearing_bluered)

    trait_roboticsarm_wearing_graybrown = instance_manager.get(get_resource_key(TRAIT_ROBOTICSARM_WEARING_GRAYBROWN, Types.TRAIT))
    if sim.has_trait(trait_roboticsarm_wearing_graybrown):
        sim.remove_trait(trait_roboticsarm_wearing_graybrown)

    trait_roboticsarm_wearing_greenbrown = instance_manager.get(get_resource_key(TRAIT_ROBOTICSARM_WEARING_GREENBROWN, Types.TRAIT))
    if sim.has_trait(trait_roboticsarm_wearing_greenbrown):
        sim.remove_trait(trait_roboticsarm_wearing_greenbrown)

    trait_roboticsarm_wearing_redgreen = instance_manager.get(get_resource_key(TRAIT_ROBOTICSARM_WEARING_REDGREEN, Types.TRAIT))
    if sim.has_trait(trait_roboticsarm_wearing_redgreen):
        sim.remove_trait(trait_roboticsarm_wearing_redgreen)

    trait_roboticsarm_wearing_whitecopper = instance_manager.get(get_resource_key(TRAIT_ROBOTICSARM_WEARING_WHITECOPPER, Types.TRAIT))
    if sim.has_trait(trait_roboticsarm_wearing_whitecopper):
        sim.remove_trait(trait_roboticsarm_wearing_whitecopper)

    trait_selfassured = instance_manager.get(get_resource_key(TRAIT_SELFASSURED, Types.TRAIT))
    if not sim.has_trait(trait_selfassured):
        sim.add_trait(trait_selfassured)

    trait_sexualorientation_woohoointerests_female = instance_manager.get(get_resource_key(TRAIT_SEXUALORIENTATION_WOOHOOINTERESTS_FEMALE, Types.TRAIT))
    if not sim.has_trait(trait_sexualorientation_woohoointerests_female):
        sim.add_trait(trait_sexualorientation_woohoointerests_female)

    trait_sexualorientation_woohoointerests_male = instance_manager.get(get_resource_key(TRAIT_SEXUALORIENTATION_WOOHOOINTERESTS_MALE, Types.TRAIT))
    if not sim.has_trait(trait_sexualorientation_woohoointerests_male):
        sim.add_trait(trait_sexualorientation_woohoointerests_male)

    trait_sexualorientation_woohoointerests_notfemale = instance_manager.get(get_resource_key(TRAIT_SEXUALORIENTATION_WOOHOOINTERESTS_NOTFEMALE, Types.TRAIT))
    if sim.has_trait(trait_sexualorientation_woohoointerests_notfemale):
        sim.remove_trait(trait_sexualorientation_woohoointerests_notfemale)

    trait_simpreference_dislikes_activities_djmixing = instance_manager.get(get_resource_key(TRAIT_SIMPREFERENCE_DISLIKES_ACTIVITIES_DJMIXING, Types.TRAIT))
    if sim.has_trait(trait_simpreference_dislikes_activities_djmixing):
        sim.remove_trait(trait_simpreference_dislikes_activities_djmixing)

    trait_simpreference_dislikes_activities_fitness = instance_manager.get(get_resource_key(TRAIT_SIMPREFERENCE_DISLIKES_ACTIVITIES_FITNESS, Types.TRAIT))
    if sim.has_trait(trait_simpreference_dislikes_activities_fitness):
        sim.remove_trait(trait_simpreference_dislikes_activities_fitness)

    trait_simpreference_dislikes_activities_guitar = instance_manager.get(get_resource_key(TRAIT_SIMPREFERENCE_DISLIKES_ACTIVITIES_GUITAR, Types.TRAIT))
    if sim.has_trait(trait_simpreference_dislikes_activities_guitar):
        sim.remove_trait(trait_simpreference_dislikes_activities_guitar)

    trait_simpreference_dislikes_activities_piano = instance_manager.get(get_resource_key(TRAIT_SIMPREFERENCE_DISLIKES_ACTIVITIES_PIANO, Types.TRAIT))
    if sim.has_trait(trait_simpreference_dislikes_activities_piano):
        sim.remove_trait(trait_simpreference_dislikes_activities_piano)

    trait_simpreference_dislikes_activities_pipeorgan = instance_manager.get(get_resource_key(TRAIT_SIMPREFERENCE_DISLIKES_ACTIVITIES_PIPEORGAN, Types.TRAIT))
    if sim.has_trait(trait_simpreference_dislikes_activities_pipeorgan):
        sim.remove_trait(trait_simpreference_dislikes_activities_pipeorgan)

    trait_simpreference_dislikes_activities_programming = instance_manager.get(get_resource_key(TRAIT_SIMPREFERENCE_DISLIKES_ACTIVITIES_PROGRAMMING, Types.TRAIT))
    if sim.has_trait(trait_simpreference_dislikes_activities_programming):
        sim.remove_trait(trait_simpreference_dislikes_activities_programming)

    trait_simpreference_dislikes_activities_rockclimbing = instance_manager.get(get_resource_key(TRAIT_SIMPREFERENCE_DISLIKES_ACTIVITIES_ROCKCLIMBING, Types.TRAIT))
    if sim.has_trait(trait_simpreference_dislikes_activities_rockclimbing):
        sim.remove_trait(trait_simpreference_dislikes_activities_rockclimbing)

    trait_simpreference_dislikes_activities_singing = instance_manager.get(get_resource_key(TRAIT_SIMPREFERENCE_DISLIKES_ACTIVITIES_SINGING, Types.TRAIT))
    if sim.has_trait(trait_simpreference_dislikes_activities_singing):
        sim.remove_trait(trait_simpreference_dislikes_activities_singing)

    trait_simpreference_dislikes_activities_violin = instance_manager.get(get_resource_key(TRAIT_SIMPREFERENCE_DISLIKES_ACTIVITIES_VIOLIN, Types.TRAIT))
    if sim.has_trait(trait_simpreference_dislikes_activities_violin):
        sim.remove_trait(trait_simpreference_dislikes_activities_violin)

    trait_simpreference_dislikes_activities_wellness = instance_manager.get(get_resource_key(TRAIT_SIMPREFERENCE_DISLIKES_ACTIVITIES_WELLNESS, Types.TRAIT))
    if sim.has_trait(trait_simpreference_dislikes_activities_wellness):
        sim.remove_trait(trait_simpreference_dislikes_activities_wellness)

    trait_simpreference_dislikes_activities_writing = instance_manager.get(get_resource_key(TRAIT_SIMPREFERENCE_DISLIKES_ACTIVITIES_WRITING, Types.TRAIT))
    if sim.has_trait(trait_simpreference_dislikes_activities_writing):
        sim.remove_trait(trait_simpreference_dislikes_activities_writing)

    trait_simpreference_likes_activities_fitness = instance_manager.get(get_resource_key(TRAIT_SIMPREFERENCE_LIKES_ACTIVITIES_FITNESS, Types.TRAIT))
    if not sim.has_trait(trait_simpreference_likes_activities_fitness):
        sim.add_trait(trait_simpreference_likes_activities_fitness)

    trait_simpreference_likes_activities_wellness = instance_manager.get(get_resource_key(TRAIT_SIMPREFERENCE_LIKES_ACTIVITIES_WELLNESS, Types.TRAIT))
    if not sim.has_trait(trait_simpreference_likes_activities_wellness):
        sim.add_trait(trait_simpreference_likes_activities_wellness)

    trait_simpreference_noopinion_activities_fitness = instance_manager.get(get_resource_key(TRAIT_SIMPREFERENCE_NOOPINION_ACTIVITIES_FITNESS, Types.TRAIT))
    if sim.has_trait(trait_simpreference_noopinion_activities_fitness):
        sim.remove_trait(trait_simpreference_noopinion_activities_fitness)

    trait_simpreference_noopinion_activities_wellness = instance_manager.get(get_resource_key(TRAIT_SIMPREFERENCE_NOOPINION_ACTIVITIES_WELLNESS, Types.TRAIT))
    if sim.has_trait(trait_simpreference_noopinion_activities_wellness):
        sim.remove_trait(trait_simpreference_noopinion_activities_wellness)

    trait_slob = instance_manager.get(get_resource_key(TRAIT_SLOB, Types.TRAIT))
    if sim.has_trait(trait_slob):
        sim.remove_trait(trait_slob)

    trait_speedcleaner = instance_manager.get(get_resource_key(TRAIT_SPEEDCLEANER, Types.TRAIT))
    if not sim.has_trait(trait_speedcleaner):
        sim.add_trait(trait_speedcleaner)

    trait_speedreader = instance_manager.get(get_resource_key(TRAIT_SPEEDREADER, Types.TRAIT))
    if not sim.has_trait(trait_speedreader):
        sim.add_trait(trait_speedreader)

    trait_stormchaser = instance_manager.get(get_resource_key(TRAIT_STORMCHASER, Types.TRAIT))
    if not sim.has_trait(trait_stormchaser):
        sim.add_trait(trait_stormchaser)

    trait_temperature_burningman = instance_manager.get(get_resource_key(TRAIT_TEMPERATURE_BURNINGMAN, Types.TRAIT))
    if not sim.has_trait(trait_temperature_burningman):
        sim.add_trait(trait_temperature_burningman)

    trait_temperature_coldacclimation = instance_manager.get(get_resource_key(TRAIT_TEMPERATURE_COLDACCLIMATION, Types.TRAIT))
    if sim.has_trait(trait_temperature_coldacclimation):
        sim.remove_trait(trait_temperature_coldacclimation)

    trait_temperature_heatacclimation = instance_manager.get(get_resource_key(TRAIT_TEMPERATURE_HEATACCLIMATION, Types.TRAIT))
    if sim.has_trait(trait_temperature_heatacclimation):
        sim.remove_trait(trait_temperature_heatacclimation)

    trait_temperature_iceman = instance_manager.get(get_resource_key(TRAIT_TEMPERATURE_ICEMAN, Types.TRAIT))
    if not sim.has_trait(trait_temperature_iceman):
        sim.add_trait(trait_temperature_iceman)

    trait_theknack = instance_manager.get(get_resource_key(TRAIT_THEKNACK, Types.TRAIT))
    if not sim.has_trait(trait_theknack):
        sim.add_trait(trait_theknack)

    trait_university_arthistorydegreeba = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_ARTHISTORYDEGREEBA, Types.TRAIT))
    if sim.has_trait(trait_university_arthistorydegreeba):
        sim.remove_trait(trait_university_arthistorydegreeba)

    trait_university_arthistorydegreebs = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_ARTHISTORYDEGREEBS, Types.TRAIT))
    if sim.has_trait(trait_university_arthistorydegreebs):
        sim.remove_trait(trait_university_arthistorydegreebs)

    trait_university_biologydegreeba = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_BIOLOGYDEGREEBA, Types.TRAIT))
    if sim.has_trait(trait_university_biologydegreeba):
        sim.remove_trait(trait_university_biologydegreeba)

    trait_university_biologydegreebs = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_BIOLOGYDEGREEBS, Types.TRAIT))
    if sim.has_trait(trait_university_biologydegreebs):
        sim.remove_trait(trait_university_biologydegreebs)

    trait_university_communicationsdegreeba = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_COMMUNICATIONSDEGREEBA, Types.TRAIT))
    if sim.has_trait(trait_university_communicationsdegreeba):
        sim.remove_trait(trait_university_communicationsdegreeba)

    trait_university_communicationsdegreebs = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_COMMUNICATIONSDEGREEBS, Types.TRAIT))
    if sim.has_trait(trait_university_communicationsdegreebs):
        sim.remove_trait(trait_university_communicationsdegreebs)

    trait_university_computersciencedegreeba = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_COMPUTERSCIENCEDEGREEBA, Types.TRAIT))
    if sim.has_trait(trait_university_computersciencedegreeba):
        sim.remove_trait(trait_university_computersciencedegreeba)

    trait_university_computersciencedegreebs = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_COMPUTERSCIENCEDEGREEBS, Types.TRAIT))
    if sim.has_trait(trait_university_computersciencedegreebs):
        sim.remove_trait(trait_university_computersciencedegreebs)

    trait_university_culinaryartsdegreeba = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_CULINARYARTSDEGREEBA, Types.TRAIT))
    if sim.has_trait(trait_university_culinaryartsdegreeba):
        sim.remove_trait(trait_university_culinaryartsdegreeba)

    trait_university_culinaryartsdegreebs = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_CULINARYARTSDEGREEBS, Types.TRAIT))
    if sim.has_trait(trait_university_culinaryartsdegreebs):
        sim.remove_trait(trait_university_culinaryartsdegreebs)

    trait_university_dramadegreeba = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_DRAMADEGREEBA, Types.TRAIT))
    if sim.has_trait(trait_university_dramadegreeba):
        sim.remove_trait(trait_university_dramadegreeba)

    trait_university_dramadegreebs = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_DRAMADEGREEBS, Types.TRAIT))
    if sim.has_trait(trait_university_dramadegreebs):
        sim.remove_trait(trait_university_dramadegreebs)

    trait_university_economicsdegreeba = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_ECONOMICSDEGREEBA, Types.TRAIT))
    if sim.has_trait(trait_university_economicsdegreeba):
        sim.remove_trait(trait_university_economicsdegreeba)

    trait_university_economicsdegreebs = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_ECONOMICSDEGREEBS, Types.TRAIT))
    if sim.has_trait(trait_university_economicsdegreebs):
        sim.remove_trait(trait_university_economicsdegreebs)

    trait_university_fineartdegreeba = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_FINEARTDEGREEBA, Types.TRAIT))
    if sim.has_trait(trait_university_fineartdegreeba):
        sim.remove_trait(trait_university_fineartdegreeba)

    trait_university_fineartdegreebs = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_FINEARTDEGREEBS, Types.TRAIT))
    if sim.has_trait(trait_university_fineartdegreebs):
        sim.remove_trait(trait_university_fineartdegreebs)

    trait_university_historydegreeba = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_HISTORYDEGREEBA, Types.TRAIT))
    if sim.has_trait(trait_university_historydegreeba):
        sim.remove_trait(trait_university_historydegreeba)

    trait_university_historydegreebs = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_HISTORYDEGREEBS, Types.TRAIT))
    if sim.has_trait(trait_university_historydegreebs):
        sim.remove_trait(trait_university_historydegreebs)

    trait_university_languageandliteraturedegreeba = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_LANGUAGEANDLITERATUREDEGREEBA, Types.TRAIT))
    if sim.has_trait(trait_university_languageandliteraturedegreeba):
        sim.remove_trait(trait_university_languageandliteraturedegreeba)

    trait_university_languageandliteraturedegreebs = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_LANGUAGEANDLITERATUREDEGREEBS, Types.TRAIT))
    if sim.has_trait(trait_university_languageandliteraturedegreebs):
        sim.remove_trait(trait_university_languageandliteraturedegreebs)

    trait_university_physicsdegreeba = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_PHYSICSDEGREEBA, Types.TRAIT))
    if sim.has_trait(trait_university_physicsdegreeba):
        sim.remove_trait(trait_university_physicsdegreeba)

    trait_university_physicsdegreebs = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_PHYSICSDEGREEBS, Types.TRAIT))
    if sim.has_trait(trait_university_physicsdegreebs):
        sim.remove_trait(trait_university_physicsdegreebs)

    trait_university_psychologydegreeba = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_PSYCHOLOGYDEGREEBA, Types.TRAIT))
    if sim.has_trait(trait_university_psychologydegreeba):
        sim.remove_trait(trait_university_psychologydegreeba)

    trait_university_psychologydegreebs = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_PSYCHOLOGYDEGREEBS, Types.TRAIT))
    if sim.has_trait(trait_university_psychologydegreebs):
        sim.remove_trait(trait_university_psychologydegreebs)

    trait_university_villainydegreeba = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_VILLAINYDEGREEBA, Types.TRAIT))
    if sim.has_trait(trait_university_villainydegreeba):
        sim.remove_trait(trait_university_villainydegreeba)

    trait_university_villainydegreebs = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_VILLAINYDEGREEBS, Types.TRAIT))
    if sim.has_trait(trait_university_villainydegreebs):
        sim.remove_trait(trait_university_villainydegreebs)

    trait_walkstylecreepy = instance_manager.get(get_resource_key(TRAIT_WALKSTYLECREEPY, Types.TRAIT))
    if sim.has_trait(trait_walkstylecreepy):
        sim.remove_trait(trait_walkstylecreepy)

    trait_walkstyleenergetic = instance_manager.get(get_resource_key(TRAIT_WALKSTYLEENERGETIC, Types.TRAIT))
    if sim.has_trait(trait_walkstyleenergetic):
        sim.remove_trait(trait_walkstyleenergetic)

    trait_walkstyleenergetic = instance_manager.get(get_resource_key(TRAIT_WALKSTYLEENERGETIC, Types.TRAIT))
    if sim.has_trait(trait_walkstyleenergetic):
        sim.remove_trait(trait_walkstyleenergetic)

    trait_walkstylefeminine = instance_manager.get(get_resource_key(TRAIT_WALKSTYLEFEMININE, Types.TRAIT))
    if sim.has_trait(trait_walkstylefeminine):
        sim.remove_trait(trait_walkstylefeminine)

    trait_walkstylegoofy = instance_manager.get(get_resource_key(TRAIT_WALKSTYLEGOOFY, Types.TRAIT))
    if sim.has_trait(trait_walkstylegoofy):
        sim.remove_trait(trait_walkstylegoofy)

    trait_walkstyleperky = instance_manager.get(get_resource_key(TRAIT_WALKSTYLEPERKY, Types.TRAIT))
    if sim.has_trait(trait_walkstyleperky):
        sim.remove_trait(trait_walkstyleperky)

    trait_walkstylesleepy = instance_manager.get(get_resource_key(TRAIT_WALKSTYLESLEEPY, Types.TRAIT))
    if sim.has_trait(trait_walkstylesleepy):
        sim.remove_trait(trait_walkstylesleepy)

    trait_walkstylesnooty = instance_manager.get(get_resource_key(TRAIT_WALKSTYLESNOOTY, Types.TRAIT))
    if sim.has_trait(trait_walkstylesnooty):
        sim.remove_trait(trait_walkstylesnooty)

    trait_walkstyleswagger = instance_manager.get(get_resource_key(TRAIT_WALKSTYLESWAGGER, Types.TRAIT))
    if sim.has_trait(trait_walkstyleswagger):
        sim.remove_trait(trait_walkstyleswagger)

    trait_walkstyletough = instance_manager.get(get_resource_key(TRAIT_WALKSTYLETOUGH, Types.TRAIT))
    if sim.has_trait(trait_walkstyletough):
        sim.remove_trait(trait_walkstyletough)

    trait_waterproof = instance_manager.get(get_resource_key(TRAIT_WATERPROOF, Types.TRAIT))
    if not sim.has_trait(trait_waterproof):
        sim.add_trait(trait_waterproof)

    trait_webmaster = instance_manager.get(get_resource_key(TRAIT_WEBMASTER, Types.TRAIT))
    if not sim.has_trait(trait_webmaster):
        sim.add_trait(trait_webmaster)

    wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_breastslarge = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_BODYSHAPE_BREASTSLARGE, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_breastslarge):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_breastslarge)

    wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_breastssmall = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_BODYSHAPE_BREASTSSMALL, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_breastssmall):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_breastssmall)

    wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_buttlarge = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_BODYSHAPE_BUTTLARGE, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_buttlarge):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_buttlarge)

    wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_buttsmall = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_BODYSHAPE_BUTTSMALL, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_buttsmall):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_buttsmall)

    wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_heavy = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_BODYSHAPE_HEAVY, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_heavy):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_heavy)

    wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_high = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_BODYSHAPE_HIGH, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_high):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_high)

    wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_light = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_BODYSHAPE_LIGHT, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_light):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_light)

    wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_low = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_BODYSHAPE_LOW, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_low):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_low)

    wickedwhims_attractiveness_trait_simpreference_dislikes_detail_body_hair = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_DETAIL_BODY_HAIR, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_detail_body_hair):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_detail_body_hair)

    wickedwhims_attractiveness_trait_simpreference_dislikes_detail_freckles = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_DETAIL_FRECKLES, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_detail_freckles):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_detail_freckles)

    wickedwhims_attractiveness_trait_simpreference_dislikes_detail_glasses = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_DETAIL_GLASSES, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_detail_glasses):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_detail_glasses)

    wickedwhims_attractiveness_trait_simpreference_dislikes_detail_hats = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_DETAIL_HATS, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_detail_hats):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_detail_hats)

    wickedwhims_attractiveness_trait_simpreference_dislikes_detail_jewelery = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_DETAIL_JEWELERY, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_detail_jewelery):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_detail_jewelery)

    wickedwhims_attractiveness_trait_simpreference_dislikes_detail_makeup = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_DETAIL_MAKEUP, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_detail_makeup):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_detail_makeup)

    wickedwhims_attractiveness_trait_simpreference_dislikes_detail_piercing = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_DETAIL_PIERCING, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_detail_piercing):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_detail_piercing)

    wickedwhims_attractiveness_trait_simpreference_dislikes_detail_tattoos = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_DETAIL_TATTOOS, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_detail_tattoos):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_detail_tattoos)

    wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_blue = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_EYECOLOR_BLUE, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_blue):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_blue)

    wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_blue = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_EYECOLOR_BLUE, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_blue):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_blue)

    wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_brown = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_EYECOLOR_BROWN, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_brown):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_brown)

    wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_brown = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_EYECOLOR_BROWN, Types.TRAIT))
    if not sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_brown):
        sim.add_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_brown)

    wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_green = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_EYECOLOR_GREEN, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_green):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_green)

    wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_green = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_EYECOLOR_GREEN, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_green):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_green)

    wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_unnatural = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_EYECOLOR_UNNATURAL, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_unnatural):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_unnatural)

    wickedwhims_attractiveness_trait_simpreference_dislikes_facialhair_beard = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_FACIALHAIR_BEARD, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_facialhair_beard):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_facialhair_beard)

    wickedwhims_attractiveness_trait_simpreference_dislikes_facialhair_clean = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_FACIALHAIR_CLEAN, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_facialhair_clean):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_facialhair_clean)

    wickedwhims_attractiveness_trait_simpreference_dislikes_facialhair_goatee = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_FACIALHAIR_GOATEE, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_facialhair_goatee):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_facialhair_goatee)

    wickedwhims_attractiveness_trait_simpreference_dislikes_facialhair_mustache = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_FACIALHAIR_MUSTACHE, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_facialhair_mustache):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_facialhair_mustache)

    wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_black = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_HAIRCOLOR_BLACK, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_black):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_black)

    wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_blonde = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_HAIRCOLOR_BLONDE, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_blonde):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_blonde)

    wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_blonde = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_HAIRCOLOR_BLONDE, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_blonde):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_blonde)

    wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_blue = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_HAIRCOLOR_BLUE, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_blue):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_blue)

    wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_blue = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_HAIRCOLOR_BLUE, Types.TRAIT))
    if not sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_blue):
        sim.add_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_blue)

    wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_brown = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_HAIRCOLOR_BROWN, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_brown):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_brown)

    wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_brown = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_HAIRCOLOR_BROWN, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_brown):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_brown)

    wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_gray = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_HAIRCOLOR_GRAY, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_gray):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_gray)

    wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_green = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_HAIRCOLOR_GREEN, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_green):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_green)

    wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_green = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_HAIRCOLOR_GREEN, Types.TRAIT))
    if not sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_green):
        sim.add_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_green)

    wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_pink = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_HAIRCOLOR_PINK, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_pink):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_pink)

    wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_red = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_HAIRCOLOR_RED, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_red):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_red)

    wickedwhims_attractiveness_trait_simpreference_dislikes_hairlength_bald = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_HAIRLENGTH_BALD, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_hairlength_bald):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_hairlength_bald)

    wickedwhims_attractiveness_trait_simpreference_dislikes_hairlength_bald = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_HAIRLENGTH_BALD, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_hairlength_bald):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_hairlength_bald)

    wickedwhims_attractiveness_trait_simpreference_dislikes_hairlength_long = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_HAIRLENGTH_LONG, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_hairlength_long):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_hairlength_long)

    wickedwhims_attractiveness_trait_simpreference_dislikes_hairlength_medium = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_HAIRLENGTH_MEDIUM, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_hairlength_medium):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_hairlength_medium)

    wickedwhims_attractiveness_trait_simpreference_dislikes_hairlength_short = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_HAIRLENGTH_SHORT, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_hairlength_short):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_hairlength_short)

    wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_breastslarge = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_BODYSHAPE_BREASTSLARGE, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_breastslarge):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_breastslarge)

    wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_breastssmall = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_BODYSHAPE_BREASTSSMALL, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_breastssmall):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_breastssmall)

    wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_breastssmall = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_BODYSHAPE_BREASTSSMALL, Types.TRAIT))
    if not sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_breastssmall):
        sim.add_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_breastssmall)

    wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_buttlarge = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_BODYSHAPE_BUTTLARGE, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_buttlarge):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_buttlarge)

    wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_buttlarge = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_BODYSHAPE_BUTTLARGE, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_buttlarge):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_buttlarge)

    wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_buttsmall = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_BODYSHAPE_BUTTSMALL, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_buttsmall):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_buttsmall)

    wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_buttsmall = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_BODYSHAPE_BUTTSMALL, Types.TRAIT))
    if not sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_buttsmall):
        sim.add_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_buttsmall)

    wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_heavy = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_BODYSHAPE_HEAVY, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_heavy):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_heavy)

    wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_high = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_BODYSHAPE_HIGH, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_high):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_high)

    wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_light = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_BODYSHAPE_LIGHT, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_light):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_light)

    wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_low = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_BODYSHAPE_LOW, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_low):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_low)

    wickedwhims_attractiveness_trait_simpreference_likes_detail_body_hair = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_DETAIL_BODY_HAIR, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_body_hair):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_body_hair)

    wickedwhims_attractiveness_trait_simpreference_likes_detail_freckles = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_DETAIL_FRECKLES, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_freckles):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_freckles)

    wickedwhims_attractiveness_trait_simpreference_likes_detail_glasses = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_DETAIL_GLASSES, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_glasses):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_glasses)

    wickedwhims_attractiveness_trait_simpreference_likes_detail_glasses = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_DETAIL_GLASSES, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_glasses):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_glasses)

    wickedwhims_attractiveness_trait_simpreference_likes_detail_hats = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_DETAIL_HATS, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_hats):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_hats)

    wickedwhims_attractiveness_trait_simpreference_likes_detail_hats = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_DETAIL_HATS, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_hats):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_hats)

    wickedwhims_attractiveness_trait_simpreference_likes_detail_jewelery = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_DETAIL_JEWELERY, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_jewelery):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_jewelery)

    wickedwhims_attractiveness_trait_simpreference_likes_detail_makeup = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_DETAIL_MAKEUP, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_makeup):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_makeup)

    wickedwhims_attractiveness_trait_simpreference_likes_detail_piercing = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_DETAIL_PIERCING, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_piercing):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_piercing)

    wickedwhims_attractiveness_trait_simpreference_likes_detail_tattoos = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_DETAIL_TATTOOS, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_tattoos):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_tattoos)

    wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_blue = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_EYECOLOR_BLUE, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_blue):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_blue)

    wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_blue = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_EYECOLOR_BLUE, Types.TRAIT))
    if not sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_blue):
        sim.add_trait(wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_blue)

    wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_brown = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_EYECOLOR_BROWN, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_brown):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_brown)

    wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_brown = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_EYECOLOR_BROWN, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_brown):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_brown)

    wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_green = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_EYECOLOR_GREEN, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_green):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_green)

    wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_green = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_EYECOLOR_GREEN, Types.TRAIT))
    if not sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_green):
        sim.add_trait(wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_green)

    wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_unnatural = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_EYECOLOR_UNNATURAL, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_unnatural):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_unnatural)

    wickedwhims_attractiveness_trait_simpreference_likes_facialhair_beard = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_FACIALHAIR_BEARD, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_facialhair_beard):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_facialhair_beard)

    wickedwhims_attractiveness_trait_simpreference_likes_facialhair_clean = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_FACIALHAIR_CLEAN, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_facialhair_clean):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_facialhair_clean)

    wickedwhims_attractiveness_trait_simpreference_likes_facialhair_goatee = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_FACIALHAIR_GOATEE, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_facialhair_goatee):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_facialhair_goatee)

    wickedwhims_attractiveness_trait_simpreference_likes_facialhair_mustache = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_FACIALHAIR_MUSTACHE, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_facialhair_mustache):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_facialhair_mustache)

    wickedwhims_attractiveness_trait_simpreference_likes_haircolor_black = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_HAIRCOLOR_BLACK, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_black):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_black)

    wickedwhims_attractiveness_trait_simpreference_likes_haircolor_blonde = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_HAIRCOLOR_BLONDE, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_blonde):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_blonde)

    wickedwhims_attractiveness_trait_simpreference_likes_haircolor_blonde = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_HAIRCOLOR_BLONDE, Types.TRAIT))
    if not sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_blonde):
        sim.add_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_blonde)

    wickedwhims_attractiveness_trait_simpreference_likes_haircolor_blue = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_HAIRCOLOR_BLUE, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_blue):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_blue)

    wickedwhims_attractiveness_trait_simpreference_likes_haircolor_brown = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_HAIRCOLOR_BROWN, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_brown):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_brown)

    wickedwhims_attractiveness_trait_simpreference_likes_haircolor_brown = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_HAIRCOLOR_BROWN, Types.TRAIT))
    if not sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_brown):
        sim.add_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_brown)

    wickedwhims_attractiveness_trait_simpreference_likes_haircolor_gray = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_HAIRCOLOR_GRAY, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_gray):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_gray)

    wickedwhims_attractiveness_trait_simpreference_likes_haircolor_green = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_HAIRCOLOR_GREEN, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_green):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_green)

    wickedwhims_attractiveness_trait_simpreference_likes_haircolor_pink = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_HAIRCOLOR_PINK, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_pink):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_pink)

    wickedwhims_attractiveness_trait_simpreference_likes_haircolor_red = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_HAIRCOLOR_RED, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_red):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_red)

    wickedwhims_attractiveness_trait_simpreference_likes_hairlength_bald = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_HAIRLENGTH_BALD, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_hairlength_bald):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_hairlength_bald)

    wickedwhims_attractiveness_trait_simpreference_likes_hairlength_long = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_HAIRLENGTH_LONG, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_hairlength_long):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_hairlength_long)

    wickedwhims_attractiveness_trait_simpreference_likes_hairlength_medium = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_HAIRLENGTH_MEDIUM, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_hairlength_medium):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_hairlength_medium)

    wickedwhims_attractiveness_trait_simpreference_likes_hairlength_short = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_HAIRLENGTH_SHORT, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_hairlength_short):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_hairlength_short)

    wickedwhims_trait_attractivenessblacklist = instance_manager.get(get_resource_key(WICKEDWHIMS_TRAIT_ATTRACTIVENESSBLACKLIST, Types.TRAIT))
    if sim.has_trait(wickedwhims_trait_attractivenessblacklist):
        sim.remove_trait(wickedwhims_trait_attractivenessblacklist)

    wickedwhims_trait_bodyhair_pubichair_isdisabled = instance_manager.get(get_resource_key(WICKEDWHIMS_TRAIT_BODYHAIR_PUBICHAIR_ISDISABLED, Types.TRAIT))
    if not sim.has_trait(wickedwhims_trait_bodyhair_pubichair_isdisabled):
        sim.add_trait(wickedwhims_trait_bodyhair_pubichair_isdisabled)

    wickedwhims_trait_bodyhair_pubichair_isgrowthdisabled = instance_manager.get(get_resource_key(WICKEDWHIMS_TRAIT_BODYHAIR_PUBICHAIR_ISGROWTHDISABLED, Types.TRAIT))
    if not sim.has_trait(wickedwhims_trait_bodyhair_pubichair_isgrowthdisabled):
        sim.add_trait(wickedwhims_trait_bodyhair_pubichair_isgrowthdisabled)

    wickedwhims_trait_cumslut = instance_manager.get(get_resource_key(WICKEDWHIMS_TRAIT_CUMSLUT, Types.TRAIT))
    if not sim.has_trait(wickedwhims_trait_cumslut):
        sim.add_trait(wickedwhims_trait_cumslut)

    wickedwhims_trait_improved_absorbency = instance_manager.get(get_resource_key(WICKEDWHIMS_TRAIT_IMPROVED_ABSORBENCY, Types.TRAIT))
    if not sim.has_trait(wickedwhims_trait_improved_absorbency):
        sim.add_trait(wickedwhims_trait_improved_absorbency)

    wickedwhims_trait_postpubertyteen = instance_manager.get(get_resource_key(WICKEDWHIMS_TRAIT_POSTPUBERTYTEEN, Types.TRAIT))
    if not sim.has_trait(wickedwhims_trait_postpubertyteen):
        sim.add_trait(wickedwhims_trait_postpubertyteen)

    wickedwhims_trait_sex_attribute_badatsex = instance_manager.get(get_resource_key(WICKEDWHIMS_TRAIT_SEX_ATTRIBUTE_BADATSEX, Types.TRAIT))
    if sim.has_trait(wickedwhims_trait_sex_attribute_badatsex):
        sim.remove_trait(wickedwhims_trait_sex_attribute_badatsex)

    wickedwhims_trait_sex_sexuallyabstinent = instance_manager.get(get_resource_key(WICKEDWHIMS_TRAIT_SEX_SEXUALLYABSTINENT, Types.TRAIT))
    if sim.has_trait(wickedwhims_trait_sex_sexuallyabstinent):
        sim.remove_trait(wickedwhims_trait_sex_sexuallyabstinent)


    # Remove or add traits from maid sims
    trait_alluring = instance_manager.get(get_resource_key(TRAIT_ALLURING, Types.TRAIT))
    if not sim.has_trait(trait_alluring):
        sim.add_trait(trait_alluring)

    trait_dastardly = instance_manager.get(get_resource_key(TRAIT_DASTARDLY, Types.TRAIT))
    if sim.has_trait(trait_dastardly):
        sim.remove_trait(trait_dastardly)

    trait_evil = instance_manager.get(get_resource_key(TRAIT_EVIL, Types.TRAIT))
    if sim.has_trait(trait_evil):
        sim.remove_trait(trait_evil)

    trait_freshchef = instance_manager.get(get_resource_key(TRAIT_FRESHCHEF, Types.TRAIT))
    if not sim.has_trait(trait_freshchef):
        sim.add_trait(trait_freshchef)

    trait_genderoptions_attractedto_female = instance_manager.get(get_resource_key(TRAIT_GENDEROPTIONS_ATTRACTEDTO_FEMALE, Types.TRAIT))
    if not sim.has_trait(trait_genderoptions_attractedto_female):
        sim.add_trait(trait_genderoptions_attractedto_female)

    trait_genderoptions_attractedto_male = instance_manager.get(get_resource_key(TRAIT_GENDEROPTIONS_ATTRACTEDTO_MALE, Types.TRAIT))
    if not sim.has_trait(trait_genderoptions_attractedto_male):
        sim.add_trait(trait_genderoptions_attractedto_male)

    trait_genderoptions_clothing_womenswear = instance_manager.get(get_resource_key(TRAIT_GENDEROPTIONS_CLOTHING_WOMENSWEAR, Types.TRAIT))
    if not sim.has_trait(trait_genderoptions_clothing_womenswear):
        sim.add_trait(trait_genderoptions_clothing_womenswear)

    trait_genderoptions_frame_feminine = instance_manager.get(get_resource_key(TRAIT_GENDEROPTIONS_FRAME_FEMININE, Types.TRAIT))
    if not sim.has_trait(trait_genderoptions_frame_feminine):
        sim.add_trait(trait_genderoptions_frame_feminine)

    trait_genderoptions_frame_masculine = instance_manager.get(get_resource_key(TRAIT_GENDEROPTIONS_FRAME_MASCULINE, Types.TRAIT))
    if sim.has_trait(trait_genderoptions_frame_masculine):
        sim.remove_trait(trait_genderoptions_frame_masculine)

    trait_genderoptions_pregnancy_canbeimpregnated = instance_manager.get(get_resource_key(TRAIT_GENDEROPTIONS_PREGNANCY_CANBEIMPREGNATED, Types.TRAIT))
    if not sim.has_trait(trait_genderoptions_pregnancy_canbeimpregnated):
        sim.add_trait(trait_genderoptions_pregnancy_canbeimpregnated)

    trait_genderoptions_pregnancy_cannotimpregnate = instance_manager.get(get_resource_key(TRAIT_GENDEROPTIONS_PREGNANCY_CANNOTIMPREGNATE, Types.TRAIT))
    if not sim.has_trait(trait_genderoptions_pregnancy_cannotimpregnate):
        sim.add_trait(trait_genderoptions_pregnancy_cannotimpregnate)

    trait_gloomy = instance_manager.get(get_resource_key(TRAIT_GLOOMY, Types.TRAIT))
    if sim.has_trait(trait_gloomy):
        sim.remove_trait(trait_gloomy)

    trait_greatkisser = instance_manager.get(get_resource_key(TRAIT_GREATKISSER, Types.TRAIT))
    if not sim.has_trait(trait_greatkisser):
        sim.add_trait(trait_greatkisser)

    trait_hsexit_earnedged = instance_manager.get(get_resource_key(TRAIT_HSEXIT_EARNEDGED, Types.TRAIT))
    if not sim.has_trait(trait_hsexit_earnedged):
        sim.add_trait(trait_hsexit_earnedged)

    trait_ismaid = instance_manager.get(get_resource_key(TRAIT_ISMAID, Types.TRAIT))
    if not sim.has_trait(trait_ismaid):
        sim.add_trait(trait_ismaid)

    trait_jealous = instance_manager.get(get_resource_key(TRAIT_JEALOUS, Types.TRAIT))
    if sim.has_trait(trait_jealous):
        sim.remove_trait(trait_jealous)

    trait_kleptomaniac = instance_manager.get(get_resource_key(TRAIT_KLEPTOMANIAC, Types.TRAIT))
    if sim.has_trait(trait_kleptomaniac):
        sim.remove_trait(trait_kleptomaniac)

    trait_neat = instance_manager.get(get_resource_key(TRAIT_NEAT, Types.TRAIT))
    if not sim.has_trait(trait_neat):
        sim.add_trait(trait_neat)

    trait_player = instance_manager.get(get_resource_key(TRAIT_PLAYER, Types.TRAIT))
    if not sim.has_trait(trait_player):
        sim.add_trait(trait_player)

    trait_proper = instance_manager.get(get_resource_key(TRAIT_PROPER, Types.TRAIT))
    if not sim.has_trait(trait_proper):
        sim.add_trait(trait_proper)

    trait_shameless = instance_manager.get(get_resource_key(TRAIT_SHAMELESS, Types.TRAIT))
    if not sim.has_trait(trait_shameless):
        sim.add_trait(trait_shameless)

    trait_sicknessimmunity = instance_manager.get(get_resource_key(TRAIT_SICKNESSIMMUNITY, Types.TRAIT))
    if not sim.has_trait(trait_sicknessimmunity):
        sim.add_trait(trait_sicknessimmunity)

    trait_walkstylefeminine = instance_manager.get(get_resource_key(TRAIT_WALKSTYLEFEMININE, Types.TRAIT))
    if not sim.has_trait(trait_walkstylefeminine):
        sim.add_trait(trait_walkstylefeminine)

    wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_breastslarge = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_BODYSHAPE_BREASTSLARGE, Types.TRAIT))
    if not sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_breastslarge):
        sim.add_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_breastslarge)

    wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_buttlarge = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_BODYSHAPE_BUTTLARGE, Types.TRAIT))
    if not sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_buttlarge):
        sim.add_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_buttlarge)

    wickedwhims_attractiveness_trait_simpreference_dislikes_facialhair_beard = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_FACIALHAIR_BEARD, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_facialhair_beard):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_facialhair_beard)

    wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_black = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_HAIRCOLOR_BLACK, Types.TRAIT))
    if not sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_black):
        sim.add_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_black)

    wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_heavy = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_BODYSHAPE_HEAVY, Types.TRAIT))
    if not sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_heavy):
        sim.add_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_heavy)

    wickedwhims_attractiveness_trait_simpreference_likes_detail_body_hair = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_DETAIL_BODY_HAIR, Types.TRAIT))
    if not sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_body_hair):
        sim.add_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_body_hair)

    wickedwhims_attractiveness_trait_simpreference_likes_facialhair_beard = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_FACIALHAIR_BEARD, Types.TRAIT))
    if not sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_facialhair_beard):
        sim.add_trait(wickedwhims_attractiveness_trait_simpreference_likes_facialhair_beard)

    wickedwhims_trait_relationships_poly = instance_manager.get(get_resource_key(WICKEDWHIMS_TRAIT_RELATIONSHIPS_POLY, Types.TRAIT))
    if not sim.has_trait(wickedwhims_trait_relationships_poly):
        sim.add_trait(wickedwhims_trait_relationships_poly)

    wickedwhims_trait_relationships_sexcheater = instance_manager.get(get_resource_key(WICKEDWHIMS_TRAIT_RELATIONSHIPS_SEXCHEATER, Types.TRAIT))
    if not sim.has_trait(wickedwhims_trait_relationships_sexcheater):
        sim.add_trait(wickedwhims_trait_relationships_sexcheater)

    wickedwhims_trait_sex_attribute_generouslover = instance_manager.get(get_resource_key(WICKEDWHIMS_TRAIT_SEX_ATTRIBUTE_GENEROUSLOVER, Types.TRAIT))
    if not sim.has_trait(wickedwhims_trait_sex_attribute_generouslover):
        sim.add_trait(wickedwhims_trait_sex_attribute_generouslover)

    wickedwhims_trait_sex_cuckold = instance_manager.get(get_resource_key(WICKEDWHIMS_TRAIT_SEX_CUCKOLD, Types.TRAIT))
    if not sim.has_trait(wickedwhims_trait_sex_cuckold):
        sim.add_trait(wickedwhims_trait_sex_cuckold)

    wickedwhims_trait_sex_sexuallyalluring = instance_manager.get(get_resource_key(WICKEDWHIMS_TRAIT_SEX_SEXUALLYALLURING, Types.TRAIT))
    if not sim.has_trait(wickedwhims_trait_sex_sexuallyalluring):
        sim.add_trait(wickedwhims_trait_sex_sexuallyalluring)


@sims4.commands.Command('pbs_mysim', command_type=sims4.commands.CommandType.Live)
def pbs_mysim(_connection=None):
    # Get the console output
    output = sims4.commands.CheatOutput(_connection)

    # Get the sim_info for the active sim
    sim = services.client_manager().get(_connection).active_sim.sim_info

    # Get the tuned trait instance from the tuning instance manager
    instance_manager = services.get_instance_manager(Types.TRAIT)

    # Remove or add traits from all sims

    archaeologyskill_giveauthenticationmail_prohibit = instance_manager.get(get_resource_key(ARCHAEOLOGYSKILL_GIVEAUTHENTICATIONMAIL_PROHIBIT, Types.TRAIT))
    if not sim.has_trait(archaeologyskill_giveauthenticationmail_prohibit):
        sim.add_trait(archaeologyskill_giveauthenticationmail_prohibit)

    fametraits_celebritywalk_on = instance_manager.get(get_resource_key(FAMETRAITS_CELEBRITYWALK_ON, Types.TRAIT))
    if sim.has_trait(fametraits_celebritywalk_on):
        sim.remove_trait(fametraits_celebritywalk_on)

    fametraits_shine_off = instance_manager.get(get_resource_key(FAMETRAITS_SHINE_OFF, Types.TRAIT))
    if not sim.has_trait(fametraits_shine_off):
        sim.add_trait(fametraits_shine_off)

    fametraits_shine_on_rank4 = instance_manager.get(get_resource_key(FAMETRAITS_SHINE_ON_RANK4, Types.TRAIT))
    if sim.has_trait(fametraits_shine_on_rank4):
        sim.remove_trait(fametraits_shine_on_rank4)

    fametraits_shine_on_rank5 = instance_manager.get(get_resource_key(FAMETRAITS_SHINE_ON_RANK5, Types.TRAIT))
    if sim.has_trait(fametraits_shine_on_rank5):
        sim.remove_trait(fametraits_shine_on_rank5)

    trait_computerglasses_wearing = instance_manager.get(get_resource_key(TRAIT_COMPUTERGLASSES_WEARING, Types.TRAIT))
    if sim.has_trait(trait_computerglasses_wearing):
        sim.remove_trait(trait_computerglasses_wearing)

    trait_computerglasses_wearing_blue = instance_manager.get(get_resource_key(TRAIT_COMPUTERGLASSES_WEARING_BLUE, Types.TRAIT))
    if sim.has_trait(trait_computerglasses_wearing_blue):
        sim.remove_trait(trait_computerglasses_wearing_blue)

    trait_computerglasses_wearing_green = instance_manager.get(get_resource_key(TRAIT_COMPUTERGLASSES_WEARING_GREEN, Types.TRAIT))
    if sim.has_trait(trait_computerglasses_wearing_green):
        sim.remove_trait(trait_computerglasses_wearing_green)

    trait_computerglasses_wearing_orange = instance_manager.get(get_resource_key(TRAIT_COMPUTERGLASSES_WEARING_ORANGE, Types.TRAIT))
    if sim.has_trait(trait_computerglasses_wearing_orange):
        sim.remove_trait(trait_computerglasses_wearing_orange)

    trait_computerglasses_wearing_pink = instance_manager.get(get_resource_key(TRAIT_COMPUTERGLASSES_WEARING_PINK, Types.TRAIT))
    if sim.has_trait(trait_computerglasses_wearing_pink):
        sim.remove_trait(trait_computerglasses_wearing_pink)

    trait_computerglasses_wearing_red = instance_manager.get(get_resource_key(TRAIT_COMPUTERGLASSES_WEARING_RED, Types.TRAIT))
    if sim.has_trait(trait_computerglasses_wearing_red):
        sim.remove_trait(trait_computerglasses_wearing_red)

    trait_computerglasses_wearing_yellow = instance_manager.get(get_resource_key(TRAIT_COMPUTERGLASSES_WEARING_YELLOW, Types.TRAIT))
    if sim.has_trait(trait_computerglasses_wearing_yellow):
        sim.remove_trait(trait_computerglasses_wearing_yellow)

    trait_crystalhelmet_alabaster = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_ALABASTER, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_alabaster):
        sim.remove_trait(trait_crystalhelmet_alabaster)

    trait_crystalhelmet_alexandrite_ep = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_ALEXANDRITE_EP, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_alexandrite_ep):
        sim.remove_trait(trait_crystalhelmet_alexandrite_ep)

    trait_crystalhelmet_amazonite_ep = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_AMAZONITE_EP, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_amazonite_ep):
        sim.remove_trait(trait_crystalhelmet_amazonite_ep)

    trait_crystalhelmet_amethyst = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_AMETHYST, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_amethyst):
        sim.remove_trait(trait_crystalhelmet_amethyst)

    trait_crystalhelmet_citrine = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_CITRINE, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_citrine):
        sim.remove_trait(trait_crystalhelmet_citrine)

    trait_crystalhelmet_crandestine_ep = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_CRANDESTINE_EP, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_crandestine_ep):
        sim.remove_trait(trait_crystalhelmet_crandestine_ep)

    trait_crystalhelmet_diamond = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_DIAMOND, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_diamond):
        sim.remove_trait(trait_crystalhelmet_diamond)

    trait_crystalhelmet_emerald = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_EMERALD, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_emerald):
        sim.remove_trait(trait_crystalhelmet_emerald)

    trait_crystalhelmet_fireopal = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_FIREOPAL, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_fireopal):
        sim.remove_trait(trait_crystalhelmet_fireopal)

    trait_crystalhelmet_hematite = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_HEMATITE, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_hematite):
        sim.remove_trait(trait_crystalhelmet_hematite)

    trait_crystalhelmet_jet = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_JET, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_jet):
        sim.remove_trait(trait_crystalhelmet_jet)

    trait_crystalhelmet_jonquilyst = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_JONQUILYST, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_jonquilyst):
        sim.remove_trait(trait_crystalhelmet_jonquilyst)

    trait_crystalhelmet_nitelite_ep = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_NITELITE_EP, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_nitelite_ep):
        sim.remove_trait(trait_crystalhelmet_nitelite_ep)

    trait_crystalhelmet_orangetopaz = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_ORANGETOPAZ, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_orangetopaz):
        sim.remove_trait(trait_crystalhelmet_orangetopaz)

    trait_crystalhelmet_peach = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_PEACH, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_peach):
        sim.remove_trait(trait_crystalhelmet_peach)

    trait_crystalhelmet_plumbite = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_PLUMBITE, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_plumbite):
        sim.remove_trait(trait_crystalhelmet_plumbite)

    trait_crystalhelmet_quartz = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_QUARTZ, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_quartz):
        sim.remove_trait(trait_crystalhelmet_quartz)

    trait_crystalhelmet_rainborz = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_RAINBORZ, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_rainborz):
        sim.remove_trait(trait_crystalhelmet_rainborz)

    trait_crystalhelmet_rose = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_ROSE, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_rose):
        sim.remove_trait(trait_crystalhelmet_rose)

    trait_crystalhelmet_ruby = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_RUBY, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_ruby):
        sim.remove_trait(trait_crystalhelmet_ruby)

    trait_crystalhelmet_sapphire = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_SAPPHIRE, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_sapphire):
        sim.remove_trait(trait_crystalhelmet_sapphire)

    trait_crystalhelmet_shinalite = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_SHINALITE, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_shinalite):
        sim.remove_trait(trait_crystalhelmet_shinalite)

    trait_crystalhelmet_simanite = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_SIMANITE, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_simanite):
        sim.remove_trait(trait_crystalhelmet_simanite)

    trait_crystalhelmet_turquoise = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_TURQUOISE, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_turquoise):
        sim.remove_trait(trait_crystalhelmet_turquoise)

    trait_doctor_sicknessresistant = instance_manager.get(get_resource_key(TRAIT_DOCTOR_SICKNESSRESISTANT, Types.TRAIT))
    if not sim.has_trait(trait_doctor_sicknessresistant):
        sim.add_trait(trait_doctor_sicknessresistant)

    trait_essenceofflavor = instance_manager.get(get_resource_key(TRAIT_ESSENCEOFFLAVOR, Types.TRAIT))
    if not sim.has_trait(trait_essenceofflavor):
        sim.add_trait(trait_essenceofflavor)

    trait_fear_beingcheatedon = instance_manager.get(get_resource_key(TRAIT_FEAR_BEINGCHEATEDON, Types.TRAIT))
    if sim.has_trait(trait_fear_beingcheatedon):
        sim.remove_trait(trait_fear_beingcheatedon)

    trait_fear_beingjudged = instance_manager.get(get_resource_key(TRAIT_FEAR_BEINGJUDGED, Types.TRAIT))
    if sim.has_trait(trait_fear_beingjudged):
        sim.remove_trait(trait_fear_beingjudged)

    trait_fear_cowplant = instance_manager.get(get_resource_key(TRAIT_FEAR_COWPLANT, Types.TRAIT))
    if sim.has_trait(trait_fear_cowplant):
        sim.remove_trait(trait_fear_cowplant)

    trait_fear_crowdedplaces = instance_manager.get(get_resource_key(TRAIT_FEAR_CROWDEDPLACES, Types.TRAIT))
    if sim.has_trait(trait_fear_crowdedplaces):
        sim.remove_trait(trait_fear_crowdedplaces)

    trait_fear_dark = instance_manager.get(get_resource_key(TRAIT_FEAR_DARK, Types.TRAIT))
    if sim.has_trait(trait_fear_dark):
        sim.remove_trait(trait_fear_dark)

    trait_fear_deadendjob = instance_manager.get(get_resource_key(TRAIT_FEAR_DEADENDJOB, Types.TRAIT))
    if sim.has_trait(trait_fear_deadendjob):
        sim.remove_trait(trait_fear_deadendjob)

    trait_fear_death = instance_manager.get(get_resource_key(TRAIT_FEAR_DEATH, Types.TRAIT))
    if sim.has_trait(trait_fear_death):
        sim.remove_trait(trait_fear_death)

    trait_fear_disappointingparents = instance_manager.get(get_resource_key(TRAIT_FEAR_DISAPPOINTINGPARENTS, Types.TRAIT))
    if sim.has_trait(trait_fear_disappointingparents):
        sim.remove_trait(trait_fear_disappointingparents)

    trait_fear_disappointingparents_parentdeceasedflag = instance_manager.get(get_resource_key(TRAIT_FEAR_DISAPPOINTINGPARENTS_PARENTDECEASEDFLAG, Types.TRAIT))
    if sim.has_trait(trait_fear_disappointingparents_parentdeceasedflag):
        sim.remove_trait(trait_fear_disappointingparents_parentdeceasedflag)

    trait_fear_failing_afterschoolactivities = instance_manager.get(get_resource_key(TRAIT_FEAR_FAILING_AFTERSCHOOLACTIVITIES, Types.TRAIT))
    if sim.has_trait(trait_fear_failing_afterschoolactivities):
        sim.remove_trait(trait_fear_failing_afterschoolactivities)

    trait_fear_failing_class = instance_manager.get(get_resource_key(TRAIT_FEAR_FAILING_CLASS, Types.TRAIT))
    if sim.has_trait(trait_fear_failing_class):
        sim.remove_trait(trait_fear_failing_class)

    trait_fear_failing_tests = instance_manager.get(get_resource_key(TRAIT_FEAR_FAILING_TESTS, Types.TRAIT))
    if sim.has_trait(trait_fear_failing_tests):
        sim.remove_trait(trait_fear_failing_tests)

    trait_fear_failure = instance_manager.get(get_resource_key(TRAIT_FEAR_FAILURE, Types.TRAIT))
    if sim.has_trait(trait_fear_failure):
        sim.remove_trait(trait_fear_failure)

    trait_fear_fire = instance_manager.get(get_resource_key(TRAIT_FEAR_FIRE, Types.TRAIT))
    if sim.has_trait(trait_fear_fire):
        sim.remove_trait(trait_fear_fire)

    trait_fear_ghosts = instance_manager.get(get_resource_key(TRAIT_FEAR_GHOSTS, Types.TRAIT))
    if sim.has_trait(trait_fear_ghosts):
        sim.remove_trait(trait_fear_ghosts)

    trait_fear_homework = instance_manager.get(get_resource_key(TRAIT_FEAR_HOMEWORK, Types.TRAIT))
    if sim.has_trait(trait_fear_homework):
        sim.remove_trait(trait_fear_homework)

    trait_fear_swimming = instance_manager.get(get_resource_key(TRAIT_FEAR_SWIMMING, Types.TRAIT))
    if sim.has_trait(trait_fear_swimming):
        sim.remove_trait(trait_fear_swimming)

    trait_fear_unfulfilled = instance_manager.get(get_resource_key(TRAIT_FEAR_UNFULFILLED, Types.TRAIT))
    if sim.has_trait(trait_fear_unfulfilled):
        sim.remove_trait(trait_fear_unfulfilled)

    trait_filthdweller = instance_manager.get(get_resource_key(TRAIT_FILTHDWELLER, Types.TRAIT))
    if sim.has_trait(trait_filthdweller):
        sim.remove_trait(trait_filthdweller)

    trait_freeservices = instance_manager.get(get_resource_key(TRAIT_FREESERVICES, Types.TRAIT))
    if not sim.has_trait(trait_freeservices):
        sim.add_trait(trait_freeservices)

    trait_frugal = instance_manager.get(get_resource_key(TRAIT_FRUGAL, Types.TRAIT))
    if not sim.has_trait(trait_frugal):
        sim.add_trait(trait_frugal)

    trait_genderoptions_attractedto_notfemale = instance_manager.get(get_resource_key(TRAIT_GENDEROPTIONS_ATTRACTEDTO_NOTFEMALE, Types.TRAIT))
    if sim.has_trait(trait_genderoptions_attractedto_notfemale):
        sim.remove_trait(trait_genderoptions_attractedto_notfemale)

    trait_genderoptions_attractedto_notmale = instance_manager.get(get_resource_key(TRAIT_GENDEROPTIONS_ATTRACTEDTO_NOTMALE, Types.TRAIT))
    if sim.has_trait(trait_genderoptions_attractedto_notmale):
        sim.remove_trait(trait_genderoptions_attractedto_notmale)

    trait_genderoptions_sexuality_exploring = instance_manager.get(get_resource_key(TRAIT_GENDEROPTIONS_SEXUALITY_EXPLORING, Types.TRAIT))
    if not sim.has_trait(trait_genderoptions_sexuality_exploring):
        sim.add_trait(trait_genderoptions_sexuality_exploring)

    trait_genderoptions_sexuality_notexploring = instance_manager.get(get_resource_key(TRAIT_GENDEROPTIONS_SEXUALITY_NOTEXPLORING, Types.TRAIT))
    if sim.has_trait(trait_genderoptions_sexuality_notexploring):
        sim.remove_trait(trait_genderoptions_sexuality_notexploring)

    trait_glutton = instance_manager.get(get_resource_key(TRAIT_GLUTTON, Types.TRAIT))
    if sim.has_trait(trait_glutton):
        sim.remove_trait(trait_glutton)

    trait_gradeschool_a = instance_manager.get(get_resource_key(TRAIT_GRADESCHOOL_A, Types.TRAIT))
    if not sim.has_trait(trait_gradeschool_a):
        sim.add_trait(trait_gradeschool_a)

    trait_gradeschool_b = instance_manager.get(get_resource_key(TRAIT_GRADESCHOOL_B, Types.TRAIT))
    if sim.has_trait(trait_gradeschool_b):
        sim.remove_trait(trait_gradeschool_b)

    trait_gradeschool_c = instance_manager.get(get_resource_key(TRAIT_GRADESCHOOL_C, Types.TRAIT))
    if sim.has_trait(trait_gradeschool_c):
        sim.remove_trait(trait_gradeschool_c)

    trait_gradeschool_d = instance_manager.get(get_resource_key(TRAIT_GRADESCHOOL_D, Types.TRAIT))
    if sim.has_trait(trait_gradeschool_d):
        sim.remove_trait(trait_gradeschool_d)

    trait_gradeschool_f = instance_manager.get(get_resource_key(TRAIT_GRADESCHOOL_F, Types.TRAIT))
    if sim.has_trait(trait_gradeschool_f):
        sim.remove_trait(trait_gradeschool_f)

    trait_highschool_a = instance_manager.get(get_resource_key(TRAIT_HIGHSCHOOL_A, Types.TRAIT))
    if not sim.has_trait(trait_highschool_a):
        sim.add_trait(trait_highschool_a)

    trait_highschool_b = instance_manager.get(get_resource_key(TRAIT_HIGHSCHOOL_B, Types.TRAIT))
    if sim.has_trait(trait_highschool_b):
        sim.remove_trait(trait_highschool_b)

    trait_highschool_c = instance_manager.get(get_resource_key(TRAIT_HIGHSCHOOL_C, Types.TRAIT))
    if sim.has_trait(trait_highschool_c):
        sim.remove_trait(trait_highschool_c)

    trait_highschool_d = instance_manager.get(get_resource_key(TRAIT_HIGHSCHOOL_D, Types.TRAIT))
    if sim.has_trait(trait_highschool_d):
        sim.remove_trait(trait_highschool_d)

    trait_highschool_f = instance_manager.get(get_resource_key(TRAIT_HIGHSCHOOL_F, Types.TRAIT))
    if sim.has_trait(trait_highschool_f):
        sim.remove_trait(trait_highschool_f)

    trait_hotheaded = instance_manager.get(get_resource_key(TRAIT_HOTHEADED, Types.TRAIT))
    if sim.has_trait(trait_hotheaded):
        sim.remove_trait(trait_hotheaded)

    trait_hsexit_expelled = instance_manager.get(get_resource_key(TRAIT_HSEXIT_EXPELLED, Types.TRAIT))
    if sim.has_trait(trait_hsexit_expelled):
        sim.remove_trait(trait_hsexit_expelled)

    trait_insane = instance_manager.get(get_resource_key(TRAIT_INSANE, Types.TRAIT))
    if sim.has_trait(trait_insane):
        sim.remove_trait(trait_insane)

    trait_invested = instance_manager.get(get_resource_key(TRAIT_INVESTED, Types.TRAIT))
    if not sim.has_trait(trait_invested):
        sim.add_trait(trait_invested)

    trait_ispregnant = instance_manager.get(get_resource_key(TRAIT_ISPREGNANT, Types.TRAIT))
    if sim.has_trait(trait_ispregnant):
        sim.remove_trait(trait_ispregnant)

    trait_mechanicalsuit_hoverengaged = instance_manager.get(get_resource_key(TRAIT_MECHANICALSUIT_HOVERENGAGED, Types.TRAIT))
    if sim.has_trait(trait_mechanicalsuit_hoverengaged):
        sim.remove_trait(trait_mechanicalsuit_hoverengaged)

    trait_mechanicalsuit_wearing_body_beigewhite = instance_manager.get(get_resource_key(TRAIT_MECHANICALSUIT_WEARING_BODY_BEIGEWHITE, Types.TRAIT))
    if sim.has_trait(trait_mechanicalsuit_wearing_body_beigewhite):
        sim.remove_trait(trait_mechanicalsuit_wearing_body_beigewhite)

    trait_mechanicalsuit_wearing_body_blackblue = instance_manager.get(get_resource_key(TRAIT_MECHANICALSUIT_WEARING_BODY_BLACKBLUE, Types.TRAIT))
    if sim.has_trait(trait_mechanicalsuit_wearing_body_blackblue):
        sim.remove_trait(trait_mechanicalsuit_wearing_body_blackblue)

    trait_mechanicalsuit_wearing_body_bluered = instance_manager.get(get_resource_key(TRAIT_MECHANICALSUIT_WEARING_BODY_BLUERED, Types.TRAIT))
    if sim.has_trait(trait_mechanicalsuit_wearing_body_bluered):
        sim.remove_trait(trait_mechanicalsuit_wearing_body_bluered)

    trait_mechanicalsuit_wearing_body_graybrown = instance_manager.get(get_resource_key(TRAIT_MECHANICALSUIT_WEARING_BODY_GRAYBROWN, Types.TRAIT))
    if sim.has_trait(trait_mechanicalsuit_wearing_body_graybrown):
        sim.remove_trait(trait_mechanicalsuit_wearing_body_graybrown)

    trait_mechanicalsuit_wearing_body_greenbrown = instance_manager.get(get_resource_key(TRAIT_MECHANICALSUIT_WEARING_BODY_GREENBROWN, Types.TRAIT))
    if sim.has_trait(trait_mechanicalsuit_wearing_body_greenbrown):
        sim.remove_trait(trait_mechanicalsuit_wearing_body_greenbrown)

    trait_mechanicalsuit_wearing_body_redgreen = instance_manager.get(get_resource_key(TRAIT_MECHANICALSUIT_WEARING_BODY_REDGREEN, Types.TRAIT))
    if sim.has_trait(trait_mechanicalsuit_wearing_body_redgreen):
        sim.remove_trait(trait_mechanicalsuit_wearing_body_redgreen)

    trait_mechanicalsuit_wearing_body_whitecopper = instance_manager.get(get_resource_key(TRAIT_MECHANICALSUIT_WEARING_BODY_WHITECOPPER, Types.TRAIT))
    if sim.has_trait(trait_mechanicalsuit_wearing_body_whitecopper):
        sim.remove_trait(trait_mechanicalsuit_wearing_body_whitecopper)

    trait_mechanicalsuit_wearing_helmet_blackblue = instance_manager.get(get_resource_key(TRAIT_MECHANICALSUIT_WEARING_HELMET_BLACKBLUE, Types.TRAIT))
    if sim.has_trait(trait_mechanicalsuit_wearing_helmet_blackblue):
        sim.remove_trait(trait_mechanicalsuit_wearing_helmet_blackblue)

    trait_mechanicalsuit_wearing_helmet_blackcopper = instance_manager.get(get_resource_key(TRAIT_MECHANICALSUIT_WEARING_HELMET_BLACKCOPPER, Types.TRAIT))
    if sim.has_trait(trait_mechanicalsuit_wearing_helmet_blackcopper):
        sim.remove_trait(trait_mechanicalsuit_wearing_helmet_blackcopper)

    trait_mechanicalsuit_wearing_helmet_blackgold = instance_manager.get(get_resource_key(TRAIT_MECHANICALSUIT_WEARING_HELMET_BLACKGOLD, Types.TRAIT))
    if sim.has_trait(trait_mechanicalsuit_wearing_helmet_blackgold):
        sim.remove_trait(trait_mechanicalsuit_wearing_helmet_blackgold)

    trait_mechanicalsuit_wearing_helmet_blackgray = instance_manager.get(get_resource_key(TRAIT_MECHANICALSUIT_WEARING_HELMET_BLACKGRAY, Types.TRAIT))
    if sim.has_trait(trait_mechanicalsuit_wearing_helmet_blackgray):
        sim.remove_trait(trait_mechanicalsuit_wearing_helmet_blackgray)

    trait_mechanicalsuit_wearing_helmet_bluegray = instance_manager.get(get_resource_key(TRAIT_MECHANICALSUIT_WEARING_HELMET_BLUEGRAY, Types.TRAIT))
    if sim.has_trait(trait_mechanicalsuit_wearing_helmet_bluegray):
        sim.remove_trait(trait_mechanicalsuit_wearing_helmet_bluegray)

    trait_mechanicalsuit_wearing_helmet_grayblack = instance_manager.get(get_resource_key(TRAIT_MECHANICALSUIT_WEARING_HELMET_GRAYBLACK, Types.TRAIT))
    if sim.has_trait(trait_mechanicalsuit_wearing_helmet_grayblack):
        sim.remove_trait(trait_mechanicalsuit_wearing_helmet_grayblack)

    trait_mechanicalsuit_wearing_helmet_greenblack = instance_manager.get(get_resource_key(TRAIT_MECHANICALSUIT_WEARING_HELMET_GREENBLACK, Types.TRAIT))
    if sim.has_trait(trait_mechanicalsuit_wearing_helmet_greenblack):
        sim.remove_trait(trait_mechanicalsuit_wearing_helmet_greenblack)

    trait_nightowl_crystalhelmet = instance_manager.get(get_resource_key(TRAIT_NIGHTOWL_CRYSTALHELMET, Types.TRAIT))
    if sim.has_trait(trait_nightowl_crystalhelmet):
        sim.remove_trait(trait_nightowl_crystalhelmet)

    trait_roboticsarm_wearing_beigewhite = instance_manager.get(get_resource_key(TRAIT_ROBOTICSARM_WEARING_BEIGEWHITE, Types.TRAIT))
    if sim.has_trait(trait_roboticsarm_wearing_beigewhite):
        sim.remove_trait(trait_roboticsarm_wearing_beigewhite)

    trait_roboticsarm_wearing_blackblue = instance_manager.get(get_resource_key(TRAIT_ROBOTICSARM_WEARING_BLACKBLUE, Types.TRAIT))
    if sim.has_trait(trait_roboticsarm_wearing_blackblue):
        sim.remove_trait(trait_roboticsarm_wearing_blackblue)

    trait_roboticsarm_wearing_bluered = instance_manager.get(get_resource_key(TRAIT_ROBOTICSARM_WEARING_BLUERED, Types.TRAIT))
    if sim.has_trait(trait_roboticsarm_wearing_bluered):
        sim.remove_trait(trait_roboticsarm_wearing_bluered)

    trait_roboticsarm_wearing_graybrown = instance_manager.get(get_resource_key(TRAIT_ROBOTICSARM_WEARING_GRAYBROWN, Types.TRAIT))
    if sim.has_trait(trait_roboticsarm_wearing_graybrown):
        sim.remove_trait(trait_roboticsarm_wearing_graybrown)

    trait_roboticsarm_wearing_greenbrown = instance_manager.get(get_resource_key(TRAIT_ROBOTICSARM_WEARING_GREENBROWN, Types.TRAIT))
    if sim.has_trait(trait_roboticsarm_wearing_greenbrown):
        sim.remove_trait(trait_roboticsarm_wearing_greenbrown)

    trait_roboticsarm_wearing_redgreen = instance_manager.get(get_resource_key(TRAIT_ROBOTICSARM_WEARING_REDGREEN, Types.TRAIT))
    if sim.has_trait(trait_roboticsarm_wearing_redgreen):
        sim.remove_trait(trait_roboticsarm_wearing_redgreen)

    trait_roboticsarm_wearing_whitecopper = instance_manager.get(get_resource_key(TRAIT_ROBOTICSARM_WEARING_WHITECOPPER, Types.TRAIT))
    if sim.has_trait(trait_roboticsarm_wearing_whitecopper):
        sim.remove_trait(trait_roboticsarm_wearing_whitecopper)

    trait_selfassured = instance_manager.get(get_resource_key(TRAIT_SELFASSURED, Types.TRAIT))
    if not sim.has_trait(trait_selfassured):
        sim.add_trait(trait_selfassured)

    trait_sexualorientation_woohoointerests_female = instance_manager.get(get_resource_key(TRAIT_SEXUALORIENTATION_WOOHOOINTERESTS_FEMALE, Types.TRAIT))
    if not sim.has_trait(trait_sexualorientation_woohoointerests_female):
        sim.add_trait(trait_sexualorientation_woohoointerests_female)

    trait_sexualorientation_woohoointerests_male = instance_manager.get(get_resource_key(TRAIT_SEXUALORIENTATION_WOOHOOINTERESTS_MALE, Types.TRAIT))
    if not sim.has_trait(trait_sexualorientation_woohoointerests_male):
        sim.add_trait(trait_sexualorientation_woohoointerests_male)

    trait_sexualorientation_woohoointerests_notfemale = instance_manager.get(get_resource_key(TRAIT_SEXUALORIENTATION_WOOHOOINTERESTS_NOTFEMALE, Types.TRAIT))
    if sim.has_trait(trait_sexualorientation_woohoointerests_notfemale):
        sim.remove_trait(trait_sexualorientation_woohoointerests_notfemale)

    trait_simpreference_dislikes_activities_djmixing = instance_manager.get(get_resource_key(TRAIT_SIMPREFERENCE_DISLIKES_ACTIVITIES_DJMIXING, Types.TRAIT))
    if sim.has_trait(trait_simpreference_dislikes_activities_djmixing):
        sim.remove_trait(trait_simpreference_dislikes_activities_djmixing)

    trait_simpreference_dislikes_activities_fitness = instance_manager.get(get_resource_key(TRAIT_SIMPREFERENCE_DISLIKES_ACTIVITIES_FITNESS, Types.TRAIT))
    if sim.has_trait(trait_simpreference_dislikes_activities_fitness):
        sim.remove_trait(trait_simpreference_dislikes_activities_fitness)

    trait_simpreference_dislikes_activities_guitar = instance_manager.get(get_resource_key(TRAIT_SIMPREFERENCE_DISLIKES_ACTIVITIES_GUITAR, Types.TRAIT))
    if sim.has_trait(trait_simpreference_dislikes_activities_guitar):
        sim.remove_trait(trait_simpreference_dislikes_activities_guitar)

    trait_simpreference_dislikes_activities_piano = instance_manager.get(get_resource_key(TRAIT_SIMPREFERENCE_DISLIKES_ACTIVITIES_PIANO, Types.TRAIT))
    if sim.has_trait(trait_simpreference_dislikes_activities_piano):
        sim.remove_trait(trait_simpreference_dislikes_activities_piano)

    trait_simpreference_dislikes_activities_pipeorgan = instance_manager.get(get_resource_key(TRAIT_SIMPREFERENCE_DISLIKES_ACTIVITIES_PIPEORGAN, Types.TRAIT))
    if sim.has_trait(trait_simpreference_dislikes_activities_pipeorgan):
        sim.remove_trait(trait_simpreference_dislikes_activities_pipeorgan)

    trait_simpreference_dislikes_activities_programming = instance_manager.get(get_resource_key(TRAIT_SIMPREFERENCE_DISLIKES_ACTIVITIES_PROGRAMMING, Types.TRAIT))
    if sim.has_trait(trait_simpreference_dislikes_activities_programming):
        sim.remove_trait(trait_simpreference_dislikes_activities_programming)

    trait_simpreference_dislikes_activities_rockclimbing = instance_manager.get(get_resource_key(TRAIT_SIMPREFERENCE_DISLIKES_ACTIVITIES_ROCKCLIMBING, Types.TRAIT))
    if sim.has_trait(trait_simpreference_dislikes_activities_rockclimbing):
        sim.remove_trait(trait_simpreference_dislikes_activities_rockclimbing)

    trait_simpreference_dislikes_activities_singing = instance_manager.get(get_resource_key(TRAIT_SIMPREFERENCE_DISLIKES_ACTIVITIES_SINGING, Types.TRAIT))
    if sim.has_trait(trait_simpreference_dislikes_activities_singing):
        sim.remove_trait(trait_simpreference_dislikes_activities_singing)

    trait_simpreference_dislikes_activities_violin = instance_manager.get(get_resource_key(TRAIT_SIMPREFERENCE_DISLIKES_ACTIVITIES_VIOLIN, Types.TRAIT))
    if sim.has_trait(trait_simpreference_dislikes_activities_violin):
        sim.remove_trait(trait_simpreference_dislikes_activities_violin)

    trait_simpreference_dislikes_activities_wellness = instance_manager.get(get_resource_key(TRAIT_SIMPREFERENCE_DISLIKES_ACTIVITIES_WELLNESS, Types.TRAIT))
    if sim.has_trait(trait_simpreference_dislikes_activities_wellness):
        sim.remove_trait(trait_simpreference_dislikes_activities_wellness)

    trait_simpreference_dislikes_activities_writing = instance_manager.get(get_resource_key(TRAIT_SIMPREFERENCE_DISLIKES_ACTIVITIES_WRITING, Types.TRAIT))
    if sim.has_trait(trait_simpreference_dislikes_activities_writing):
        sim.remove_trait(trait_simpreference_dislikes_activities_writing)

    trait_simpreference_likes_activities_fitness = instance_manager.get(get_resource_key(TRAIT_SIMPREFERENCE_LIKES_ACTIVITIES_FITNESS, Types.TRAIT))
    if not sim.has_trait(trait_simpreference_likes_activities_fitness):
        sim.add_trait(trait_simpreference_likes_activities_fitness)

    trait_simpreference_likes_activities_wellness = instance_manager.get(get_resource_key(TRAIT_SIMPREFERENCE_LIKES_ACTIVITIES_WELLNESS, Types.TRAIT))
    if not sim.has_trait(trait_simpreference_likes_activities_wellness):
        sim.add_trait(trait_simpreference_likes_activities_wellness)

    trait_simpreference_noopinion_activities_fitness = instance_manager.get(get_resource_key(TRAIT_SIMPREFERENCE_NOOPINION_ACTIVITIES_FITNESS, Types.TRAIT))
    if sim.has_trait(trait_simpreference_noopinion_activities_fitness):
        sim.remove_trait(trait_simpreference_noopinion_activities_fitness)

    trait_simpreference_noopinion_activities_wellness = instance_manager.get(get_resource_key(TRAIT_SIMPREFERENCE_NOOPINION_ACTIVITIES_WELLNESS, Types.TRAIT))
    if sim.has_trait(trait_simpreference_noopinion_activities_wellness):
        sim.remove_trait(trait_simpreference_noopinion_activities_wellness)

    trait_slob = instance_manager.get(get_resource_key(TRAIT_SLOB, Types.TRAIT))
    if sim.has_trait(trait_slob):
        sim.remove_trait(trait_slob)

    trait_speedcleaner = instance_manager.get(get_resource_key(TRAIT_SPEEDCLEANER, Types.TRAIT))
    if not sim.has_trait(trait_speedcleaner):
        sim.add_trait(trait_speedcleaner)

    trait_speedreader = instance_manager.get(get_resource_key(TRAIT_SPEEDREADER, Types.TRAIT))
    if not sim.has_trait(trait_speedreader):
        sim.add_trait(trait_speedreader)

    trait_stormchaser = instance_manager.get(get_resource_key(TRAIT_STORMCHASER, Types.TRAIT))
    if not sim.has_trait(trait_stormchaser):
        sim.add_trait(trait_stormchaser)

    trait_temperature_burningman = instance_manager.get(get_resource_key(TRAIT_TEMPERATURE_BURNINGMAN, Types.TRAIT))
    if not sim.has_trait(trait_temperature_burningman):
        sim.add_trait(trait_temperature_burningman)

    trait_temperature_coldacclimation = instance_manager.get(get_resource_key(TRAIT_TEMPERATURE_COLDACCLIMATION, Types.TRAIT))
    if sim.has_trait(trait_temperature_coldacclimation):
        sim.remove_trait(trait_temperature_coldacclimation)

    trait_temperature_heatacclimation = instance_manager.get(get_resource_key(TRAIT_TEMPERATURE_HEATACCLIMATION, Types.TRAIT))
    if sim.has_trait(trait_temperature_heatacclimation):
        sim.remove_trait(trait_temperature_heatacclimation)

    trait_temperature_iceman = instance_manager.get(get_resource_key(TRAIT_TEMPERATURE_ICEMAN, Types.TRAIT))
    if not sim.has_trait(trait_temperature_iceman):
        sim.add_trait(trait_temperature_iceman)

    trait_theknack = instance_manager.get(get_resource_key(TRAIT_THEKNACK, Types.TRAIT))
    if not sim.has_trait(trait_theknack):
        sim.add_trait(trait_theknack)

    trait_university_arthistorydegreeba = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_ARTHISTORYDEGREEBA, Types.TRAIT))
    if sim.has_trait(trait_university_arthistorydegreeba):
        sim.remove_trait(trait_university_arthistorydegreeba)

    trait_university_arthistorydegreebs = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_ARTHISTORYDEGREEBS, Types.TRAIT))
    if sim.has_trait(trait_university_arthistorydegreebs):
        sim.remove_trait(trait_university_arthistorydegreebs)

    trait_university_biologydegreeba = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_BIOLOGYDEGREEBA, Types.TRAIT))
    if sim.has_trait(trait_university_biologydegreeba):
        sim.remove_trait(trait_university_biologydegreeba)

    trait_university_biologydegreebs = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_BIOLOGYDEGREEBS, Types.TRAIT))
    if sim.has_trait(trait_university_biologydegreebs):
        sim.remove_trait(trait_university_biologydegreebs)

    trait_university_communicationsdegreeba = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_COMMUNICATIONSDEGREEBA, Types.TRAIT))
    if sim.has_trait(trait_university_communicationsdegreeba):
        sim.remove_trait(trait_university_communicationsdegreeba)

    trait_university_communicationsdegreebs = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_COMMUNICATIONSDEGREEBS, Types.TRAIT))
    if sim.has_trait(trait_university_communicationsdegreebs):
        sim.remove_trait(trait_university_communicationsdegreebs)

    trait_university_computersciencedegreeba = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_COMPUTERSCIENCEDEGREEBA, Types.TRAIT))
    if sim.has_trait(trait_university_computersciencedegreeba):
        sim.remove_trait(trait_university_computersciencedegreeba)

    trait_university_computersciencedegreebs = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_COMPUTERSCIENCEDEGREEBS, Types.TRAIT))
    if sim.has_trait(trait_university_computersciencedegreebs):
        sim.remove_trait(trait_university_computersciencedegreebs)

    trait_university_culinaryartsdegreeba = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_CULINARYARTSDEGREEBA, Types.TRAIT))
    if sim.has_trait(trait_university_culinaryartsdegreeba):
        sim.remove_trait(trait_university_culinaryartsdegreeba)

    trait_university_culinaryartsdegreebs = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_CULINARYARTSDEGREEBS, Types.TRAIT))
    if sim.has_trait(trait_university_culinaryartsdegreebs):
        sim.remove_trait(trait_university_culinaryartsdegreebs)

    trait_university_dramadegreeba = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_DRAMADEGREEBA, Types.TRAIT))
    if sim.has_trait(trait_university_dramadegreeba):
        sim.remove_trait(trait_university_dramadegreeba)

    trait_university_dramadegreebs = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_DRAMADEGREEBS, Types.TRAIT))
    if sim.has_trait(trait_university_dramadegreebs):
        sim.remove_trait(trait_university_dramadegreebs)

    trait_university_economicsdegreeba = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_ECONOMICSDEGREEBA, Types.TRAIT))
    if sim.has_trait(trait_university_economicsdegreeba):
        sim.remove_trait(trait_university_economicsdegreeba)

    trait_university_economicsdegreebs = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_ECONOMICSDEGREEBS, Types.TRAIT))
    if sim.has_trait(trait_university_economicsdegreebs):
        sim.remove_trait(trait_university_economicsdegreebs)

    trait_university_fineartdegreeba = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_FINEARTDEGREEBA, Types.TRAIT))
    if sim.has_trait(trait_university_fineartdegreeba):
        sim.remove_trait(trait_university_fineartdegreeba)

    trait_university_fineartdegreebs = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_FINEARTDEGREEBS, Types.TRAIT))
    if sim.has_trait(trait_university_fineartdegreebs):
        sim.remove_trait(trait_university_fineartdegreebs)

    trait_university_historydegreeba = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_HISTORYDEGREEBA, Types.TRAIT))
    if sim.has_trait(trait_university_historydegreeba):
        sim.remove_trait(trait_university_historydegreeba)

    trait_university_historydegreebs = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_HISTORYDEGREEBS, Types.TRAIT))
    if sim.has_trait(trait_university_historydegreebs):
        sim.remove_trait(trait_university_historydegreebs)

    trait_university_languageandliteraturedegreeba = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_LANGUAGEANDLITERATUREDEGREEBA, Types.TRAIT))
    if sim.has_trait(trait_university_languageandliteraturedegreeba):
        sim.remove_trait(trait_university_languageandliteraturedegreeba)

    trait_university_languageandliteraturedegreebs = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_LANGUAGEANDLITERATUREDEGREEBS, Types.TRAIT))
    if sim.has_trait(trait_university_languageandliteraturedegreebs):
        sim.remove_trait(trait_university_languageandliteraturedegreebs)

    trait_university_physicsdegreeba = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_PHYSICSDEGREEBA, Types.TRAIT))
    if sim.has_trait(trait_university_physicsdegreeba):
        sim.remove_trait(trait_university_physicsdegreeba)

    trait_university_physicsdegreebs = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_PHYSICSDEGREEBS, Types.TRAIT))
    if sim.has_trait(trait_university_physicsdegreebs):
        sim.remove_trait(trait_university_physicsdegreebs)

    trait_university_psychologydegreeba = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_PSYCHOLOGYDEGREEBA, Types.TRAIT))
    if sim.has_trait(trait_university_psychologydegreeba):
        sim.remove_trait(trait_university_psychologydegreeba)

    trait_university_psychologydegreebs = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_PSYCHOLOGYDEGREEBS, Types.TRAIT))
    if sim.has_trait(trait_university_psychologydegreebs):
        sim.remove_trait(trait_university_psychologydegreebs)

    trait_university_villainydegreeba = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_VILLAINYDEGREEBA, Types.TRAIT))
    if sim.has_trait(trait_university_villainydegreeba):
        sim.remove_trait(trait_university_villainydegreeba)

    trait_university_villainydegreebs = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_VILLAINYDEGREEBS, Types.TRAIT))
    if sim.has_trait(trait_university_villainydegreebs):
        sim.remove_trait(trait_university_villainydegreebs)

    trait_walkstylecreepy = instance_manager.get(get_resource_key(TRAIT_WALKSTYLECREEPY, Types.TRAIT))
    if sim.has_trait(trait_walkstylecreepy):
        sim.remove_trait(trait_walkstylecreepy)

    trait_walkstyleenergetic = instance_manager.get(get_resource_key(TRAIT_WALKSTYLEENERGETIC, Types.TRAIT))
    if sim.has_trait(trait_walkstyleenergetic):
        sim.remove_trait(trait_walkstyleenergetic)

    trait_walkstyleenergetic = instance_manager.get(get_resource_key(TRAIT_WALKSTYLEENERGETIC, Types.TRAIT))
    if sim.has_trait(trait_walkstyleenergetic):
        sim.remove_trait(trait_walkstyleenergetic)

    trait_walkstylefeminine = instance_manager.get(get_resource_key(TRAIT_WALKSTYLEFEMININE, Types.TRAIT))
    if sim.has_trait(trait_walkstylefeminine):
        sim.remove_trait(trait_walkstylefeminine)

    trait_walkstylegoofy = instance_manager.get(get_resource_key(TRAIT_WALKSTYLEGOOFY, Types.TRAIT))
    if sim.has_trait(trait_walkstylegoofy):
        sim.remove_trait(trait_walkstylegoofy)

    trait_walkstyleperky = instance_manager.get(get_resource_key(TRAIT_WALKSTYLEPERKY, Types.TRAIT))
    if sim.has_trait(trait_walkstyleperky):
        sim.remove_trait(trait_walkstyleperky)

    trait_walkstylesleepy = instance_manager.get(get_resource_key(TRAIT_WALKSTYLESLEEPY, Types.TRAIT))
    if sim.has_trait(trait_walkstylesleepy):
        sim.remove_trait(trait_walkstylesleepy)

    trait_walkstylesnooty = instance_manager.get(get_resource_key(TRAIT_WALKSTYLESNOOTY, Types.TRAIT))
    if sim.has_trait(trait_walkstylesnooty):
        sim.remove_trait(trait_walkstylesnooty)

    trait_walkstyleswagger = instance_manager.get(get_resource_key(TRAIT_WALKSTYLESWAGGER, Types.TRAIT))
    if sim.has_trait(trait_walkstyleswagger):
        sim.remove_trait(trait_walkstyleswagger)

    trait_walkstyletough = instance_manager.get(get_resource_key(TRAIT_WALKSTYLETOUGH, Types.TRAIT))
    if sim.has_trait(trait_walkstyletough):
        sim.remove_trait(trait_walkstyletough)

    trait_waterproof = instance_manager.get(get_resource_key(TRAIT_WATERPROOF, Types.TRAIT))
    if not sim.has_trait(trait_waterproof):
        sim.add_trait(trait_waterproof)

    trait_webmaster = instance_manager.get(get_resource_key(TRAIT_WEBMASTER, Types.TRAIT))
    if not sim.has_trait(trait_webmaster):
        sim.add_trait(trait_webmaster)

    wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_breastslarge = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_BODYSHAPE_BREASTSLARGE, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_breastslarge):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_breastslarge)

    wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_breastssmall = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_BODYSHAPE_BREASTSSMALL, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_breastssmall):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_breastssmall)

    wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_buttlarge = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_BODYSHAPE_BUTTLARGE, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_buttlarge):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_buttlarge)

    wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_buttsmall = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_BODYSHAPE_BUTTSMALL, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_buttsmall):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_buttsmall)

    wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_heavy = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_BODYSHAPE_HEAVY, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_heavy):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_heavy)

    wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_high = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_BODYSHAPE_HIGH, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_high):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_high)

    wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_light = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_BODYSHAPE_LIGHT, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_light):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_light)

    wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_low = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_BODYSHAPE_LOW, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_low):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_low)

    wickedwhims_attractiveness_trait_simpreference_dislikes_detail_body_hair = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_DETAIL_BODY_HAIR, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_detail_body_hair):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_detail_body_hair)

    wickedwhims_attractiveness_trait_simpreference_dislikes_detail_freckles = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_DETAIL_FRECKLES, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_detail_freckles):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_detail_freckles)

    wickedwhims_attractiveness_trait_simpreference_dislikes_detail_glasses = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_DETAIL_GLASSES, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_detail_glasses):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_detail_glasses)

    wickedwhims_attractiveness_trait_simpreference_dislikes_detail_hats = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_DETAIL_HATS, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_detail_hats):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_detail_hats)

    wickedwhims_attractiveness_trait_simpreference_dislikes_detail_jewelery = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_DETAIL_JEWELERY, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_detail_jewelery):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_detail_jewelery)

    wickedwhims_attractiveness_trait_simpreference_dislikes_detail_makeup = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_DETAIL_MAKEUP, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_detail_makeup):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_detail_makeup)

    wickedwhims_attractiveness_trait_simpreference_dislikes_detail_piercing = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_DETAIL_PIERCING, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_detail_piercing):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_detail_piercing)

    wickedwhims_attractiveness_trait_simpreference_dislikes_detail_tattoos = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_DETAIL_TATTOOS, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_detail_tattoos):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_detail_tattoos)

    wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_blue = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_EYECOLOR_BLUE, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_blue):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_blue)

    wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_blue = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_EYECOLOR_BLUE, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_blue):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_blue)

    wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_brown = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_EYECOLOR_BROWN, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_brown):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_brown)

    wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_brown = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_EYECOLOR_BROWN, Types.TRAIT))
    if not sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_brown):
        sim.add_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_brown)

    wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_green = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_EYECOLOR_GREEN, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_green):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_green)

    wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_green = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_EYECOLOR_GREEN, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_green):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_green)

    wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_unnatural = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_EYECOLOR_UNNATURAL, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_unnatural):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_unnatural)

    wickedwhims_attractiveness_trait_simpreference_dislikes_facialhair_beard = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_FACIALHAIR_BEARD, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_facialhair_beard):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_facialhair_beard)

    wickedwhims_attractiveness_trait_simpreference_dislikes_facialhair_clean = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_FACIALHAIR_CLEAN, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_facialhair_clean):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_facialhair_clean)

    wickedwhims_attractiveness_trait_simpreference_dislikes_facialhair_goatee = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_FACIALHAIR_GOATEE, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_facialhair_goatee):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_facialhair_goatee)

    wickedwhims_attractiveness_trait_simpreference_dislikes_facialhair_mustache = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_FACIALHAIR_MUSTACHE, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_facialhair_mustache):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_facialhair_mustache)

    wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_black = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_HAIRCOLOR_BLACK, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_black):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_black)

    wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_blonde = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_HAIRCOLOR_BLONDE, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_blonde):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_blonde)

    wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_blonde = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_HAIRCOLOR_BLONDE, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_blonde):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_blonde)

    wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_blue = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_HAIRCOLOR_BLUE, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_blue):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_blue)

    wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_blue = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_HAIRCOLOR_BLUE, Types.TRAIT))
    if not sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_blue):
        sim.add_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_blue)

    wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_brown = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_HAIRCOLOR_BROWN, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_brown):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_brown)

    wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_brown = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_HAIRCOLOR_BROWN, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_brown):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_brown)

    wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_gray = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_HAIRCOLOR_GRAY, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_gray):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_gray)

    wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_green = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_HAIRCOLOR_GREEN, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_green):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_green)

    wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_green = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_HAIRCOLOR_GREEN, Types.TRAIT))
    if not sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_green):
        sim.add_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_green)

    wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_pink = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_HAIRCOLOR_PINK, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_pink):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_pink)

    wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_red = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_HAIRCOLOR_RED, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_red):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_red)

    wickedwhims_attractiveness_trait_simpreference_dislikes_hairlength_bald = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_HAIRLENGTH_BALD, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_hairlength_bald):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_hairlength_bald)

    wickedwhims_attractiveness_trait_simpreference_dislikes_hairlength_bald = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_HAIRLENGTH_BALD, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_hairlength_bald):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_hairlength_bald)

    wickedwhims_attractiveness_trait_simpreference_dislikes_hairlength_long = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_HAIRLENGTH_LONG, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_hairlength_long):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_hairlength_long)

    wickedwhims_attractiveness_trait_simpreference_dislikes_hairlength_medium = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_HAIRLENGTH_MEDIUM, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_hairlength_medium):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_hairlength_medium)

    wickedwhims_attractiveness_trait_simpreference_dislikes_hairlength_short = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_HAIRLENGTH_SHORT, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_hairlength_short):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_hairlength_short)

    wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_breastslarge = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_BODYSHAPE_BREASTSLARGE, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_breastslarge):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_breastslarge)

    wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_breastssmall = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_BODYSHAPE_BREASTSSMALL, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_breastssmall):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_breastssmall)

    wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_breastssmall = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_BODYSHAPE_BREASTSSMALL, Types.TRAIT))
    if not sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_breastssmall):
        sim.add_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_breastssmall)

    wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_buttlarge = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_BODYSHAPE_BUTTLARGE, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_buttlarge):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_buttlarge)

    wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_buttlarge = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_BODYSHAPE_BUTTLARGE, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_buttlarge):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_buttlarge)

    wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_buttsmall = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_BODYSHAPE_BUTTSMALL, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_buttsmall):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_buttsmall)

    wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_buttsmall = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_BODYSHAPE_BUTTSMALL, Types.TRAIT))
    if not sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_buttsmall):
        sim.add_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_buttsmall)

    wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_heavy = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_BODYSHAPE_HEAVY, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_heavy):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_heavy)

    wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_high = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_BODYSHAPE_HIGH, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_high):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_high)

    wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_light = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_BODYSHAPE_LIGHT, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_light):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_light)

    wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_low = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_BODYSHAPE_LOW, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_low):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_low)

    wickedwhims_attractiveness_trait_simpreference_likes_detail_body_hair = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_DETAIL_BODY_HAIR, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_body_hair):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_body_hair)

    wickedwhims_attractiveness_trait_simpreference_likes_detail_freckles = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_DETAIL_FRECKLES, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_freckles):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_freckles)

    wickedwhims_attractiveness_trait_simpreference_likes_detail_glasses = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_DETAIL_GLASSES, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_glasses):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_glasses)

    wickedwhims_attractiveness_trait_simpreference_likes_detail_glasses = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_DETAIL_GLASSES, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_glasses):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_glasses)

    wickedwhims_attractiveness_trait_simpreference_likes_detail_hats = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_DETAIL_HATS, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_hats):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_hats)

    wickedwhims_attractiveness_trait_simpreference_likes_detail_hats = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_DETAIL_HATS, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_hats):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_hats)

    wickedwhims_attractiveness_trait_simpreference_likes_detail_jewelery = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_DETAIL_JEWELERY, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_jewelery):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_jewelery)

    wickedwhims_attractiveness_trait_simpreference_likes_detail_makeup = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_DETAIL_MAKEUP, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_makeup):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_makeup)

    wickedwhims_attractiveness_trait_simpreference_likes_detail_piercing = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_DETAIL_PIERCING, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_piercing):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_piercing)

    wickedwhims_attractiveness_trait_simpreference_likes_detail_tattoos = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_DETAIL_TATTOOS, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_tattoos):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_tattoos)

    wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_blue = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_EYECOLOR_BLUE, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_blue):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_blue)

    wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_blue = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_EYECOLOR_BLUE, Types.TRAIT))
    if not sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_blue):
        sim.add_trait(wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_blue)

    wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_brown = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_EYECOLOR_BROWN, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_brown):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_brown)

    wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_brown = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_EYECOLOR_BROWN, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_brown):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_brown)

    wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_green = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_EYECOLOR_GREEN, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_green):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_green)

    wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_green = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_EYECOLOR_GREEN, Types.TRAIT))
    if not sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_green):
        sim.add_trait(wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_green)

    wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_unnatural = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_EYECOLOR_UNNATURAL, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_unnatural):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_unnatural)

    wickedwhims_attractiveness_trait_simpreference_likes_facialhair_beard = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_FACIALHAIR_BEARD, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_facialhair_beard):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_facialhair_beard)

    wickedwhims_attractiveness_trait_simpreference_likes_facialhair_clean = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_FACIALHAIR_CLEAN, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_facialhair_clean):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_facialhair_clean)

    wickedwhims_attractiveness_trait_simpreference_likes_facialhair_goatee = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_FACIALHAIR_GOATEE, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_facialhair_goatee):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_facialhair_goatee)

    wickedwhims_attractiveness_trait_simpreference_likes_facialhair_mustache = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_FACIALHAIR_MUSTACHE, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_facialhair_mustache):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_facialhair_mustache)

    wickedwhims_attractiveness_trait_simpreference_likes_haircolor_black = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_HAIRCOLOR_BLACK, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_black):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_black)

    wickedwhims_attractiveness_trait_simpreference_likes_haircolor_blonde = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_HAIRCOLOR_BLONDE, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_blonde):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_blonde)

    wickedwhims_attractiveness_trait_simpreference_likes_haircolor_blonde = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_HAIRCOLOR_BLONDE, Types.TRAIT))
    if not sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_blonde):
        sim.add_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_blonde)

    wickedwhims_attractiveness_trait_simpreference_likes_haircolor_blue = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_HAIRCOLOR_BLUE, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_blue):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_blue)

    wickedwhims_attractiveness_trait_simpreference_likes_haircolor_brown = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_HAIRCOLOR_BROWN, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_brown):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_brown)

    wickedwhims_attractiveness_trait_simpreference_likes_haircolor_brown = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_HAIRCOLOR_BROWN, Types.TRAIT))
    if not sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_brown):
        sim.add_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_brown)

    wickedwhims_attractiveness_trait_simpreference_likes_haircolor_gray = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_HAIRCOLOR_GRAY, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_gray):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_gray)

    wickedwhims_attractiveness_trait_simpreference_likes_haircolor_green = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_HAIRCOLOR_GREEN, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_green):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_green)

    wickedwhims_attractiveness_trait_simpreference_likes_haircolor_pink = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_HAIRCOLOR_PINK, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_pink):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_pink)

    wickedwhims_attractiveness_trait_simpreference_likes_haircolor_red = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_HAIRCOLOR_RED, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_red):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_red)

    wickedwhims_attractiveness_trait_simpreference_likes_hairlength_bald = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_HAIRLENGTH_BALD, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_hairlength_bald):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_hairlength_bald)

    wickedwhims_attractiveness_trait_simpreference_likes_hairlength_long = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_HAIRLENGTH_LONG, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_hairlength_long):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_hairlength_long)

    wickedwhims_attractiveness_trait_simpreference_likes_hairlength_medium = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_HAIRLENGTH_MEDIUM, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_hairlength_medium):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_hairlength_medium)

    wickedwhims_attractiveness_trait_simpreference_likes_hairlength_short = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_HAIRLENGTH_SHORT, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_hairlength_short):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_hairlength_short)

    wickedwhims_trait_attractivenessblacklist = instance_manager.get(get_resource_key(WICKEDWHIMS_TRAIT_ATTRACTIVENESSBLACKLIST, Types.TRAIT))
    if sim.has_trait(wickedwhims_trait_attractivenessblacklist):
        sim.remove_trait(wickedwhims_trait_attractivenessblacklist)

    wickedwhims_trait_bodyhair_pubichair_isdisabled = instance_manager.get(get_resource_key(WICKEDWHIMS_TRAIT_BODYHAIR_PUBICHAIR_ISDISABLED, Types.TRAIT))
    if not sim.has_trait(wickedwhims_trait_bodyhair_pubichair_isdisabled):
        sim.add_trait(wickedwhims_trait_bodyhair_pubichair_isdisabled)

    wickedwhims_trait_bodyhair_pubichair_isgrowthdisabled = instance_manager.get(get_resource_key(WICKEDWHIMS_TRAIT_BODYHAIR_PUBICHAIR_ISGROWTHDISABLED, Types.TRAIT))
    if not sim.has_trait(wickedwhims_trait_bodyhair_pubichair_isgrowthdisabled):
        sim.add_trait(wickedwhims_trait_bodyhair_pubichair_isgrowthdisabled)

    wickedwhims_trait_cumslut = instance_manager.get(get_resource_key(WICKEDWHIMS_TRAIT_CUMSLUT, Types.TRAIT))
    if not sim.has_trait(wickedwhims_trait_cumslut):
        sim.add_trait(wickedwhims_trait_cumslut)

    wickedwhims_trait_improved_absorbency = instance_manager.get(get_resource_key(WICKEDWHIMS_TRAIT_IMPROVED_ABSORBENCY, Types.TRAIT))
    if not sim.has_trait(wickedwhims_trait_improved_absorbency):
        sim.add_trait(wickedwhims_trait_improved_absorbency)

    wickedwhims_trait_postpubertyteen = instance_manager.get(get_resource_key(WICKEDWHIMS_TRAIT_POSTPUBERTYTEEN, Types.TRAIT))
    if not sim.has_trait(wickedwhims_trait_postpubertyteen):
        sim.add_trait(wickedwhims_trait_postpubertyteen)

    wickedwhims_trait_sex_attribute_badatsex = instance_manager.get(get_resource_key(WICKEDWHIMS_TRAIT_SEX_ATTRIBUTE_BADATSEX, Types.TRAIT))
    if sim.has_trait(wickedwhims_trait_sex_attribute_badatsex):
        sim.remove_trait(wickedwhims_trait_sex_attribute_badatsex)

    wickedwhims_trait_sex_sexuallyabstinent = instance_manager.get(get_resource_key(WICKEDWHIMS_TRAIT_SEX_SEXUALLYABSTINENT, Types.TRAIT))
    if sim.has_trait(wickedwhims_trait_sex_sexuallyabstinent):
        sim.remove_trait(wickedwhims_trait_sex_sexuallyabstinent)


    # Remove or add traits from my sim
    trait_alluring = instance_manager.get(get_resource_key(TRAIT_ALLURING, Types.TRAIT))
    if not sim.has_trait(trait_alluring):
        sim.add_trait(trait_alluring)

    trait_alwayswelcome = instance_manager.get(get_resource_key(TRAIT_ALWAYSWELCOME, Types.TRAIT))
    if not sim.has_trait(trait_alwayswelcome):
        sim.add_trait(trait_alwayswelcome)

    trait_brave = instance_manager.get(get_resource_key(TRAIT_BRAVE, Types.TRAIT))
    if not sim.has_trait(trait_brave):
        sim.add_trait(trait_brave)

    trait_commitmentissues = instance_manager.get(get_resource_key(TRAIT_COMMITMENTISSUES, Types.TRAIT))
    if sim.has_trait(trait_commitmentissues):
        sim.remove_trait(trait_commitmentissues)

    trait_dastardly = instance_manager.get(get_resource_key(TRAIT_DASTARDLY, Types.TRAIT))
    if sim.has_trait(trait_dastardly):
        sim.remove_trait(trait_dastardly)

    trait_dauntless = instance_manager.get(get_resource_key(TRAIT_DAUNTLESS, Types.TRAIT))
    if sim.has_trait(trait_dauntless):
        sim.remove_trait(trait_dauntless)

    trait_entrepreneur_theknowledge = instance_manager.get(get_resource_key(TRAIT_ENTREPRENEUR_THEKNOWLEDGE, Types.TRAIT))
    if not sim.has_trait(trait_entrepreneur_theknowledge):
        sim.add_trait(trait_entrepreneur_theknowledge)

    trait_evil = instance_manager.get(get_resource_key(TRAIT_EVIL, Types.TRAIT))
    if sim.has_trait(trait_evil):
        sim.remove_trait(trait_evil)

    trait_excursion_mountaineer_rank1 = instance_manager.get(get_resource_key(TRAIT_EXCURSION_MOUNTAINEER_RANK1, Types.TRAIT))
    if sim.has_trait(trait_excursion_mountaineer_rank1):
        sim.remove_trait(trait_excursion_mountaineer_rank1)

    trait_excursion_mountaineer_rank2 = instance_manager.get(get_resource_key(TRAIT_EXCURSION_MOUNTAINEER_RANK2, Types.TRAIT))
    if sim.has_trait(trait_excursion_mountaineer_rank2):
        sim.remove_trait(trait_excursion_mountaineer_rank2)

    trait_excursion_mountaineer_rank3 = instance_manager.get(get_resource_key(TRAIT_EXCURSION_MOUNTAINEER_RANK3, Types.TRAIT))
    if not sim.has_trait(trait_excursion_mountaineer_rank3):
        sim.add_trait(trait_excursion_mountaineer_rank3)

    trait_freshchef = instance_manager.get(get_resource_key(TRAIT_FRESHCHEF, Types.TRAIT))
    if not sim.has_trait(trait_freshchef):
        sim.add_trait(trait_freshchef)

    trait_genderoptions_attractedto_female = instance_manager.get(get_resource_key(TRAIT_GENDEROPTIONS_ATTRACTEDTO_FEMALE, Types.TRAIT))
    if not sim.has_trait(trait_genderoptions_attractedto_female):
        sim.add_trait(trait_genderoptions_attractedto_female)

    trait_genderoptions_attractedto_male = instance_manager.get(get_resource_key(TRAIT_GENDEROPTIONS_ATTRACTEDTO_MALE, Types.TRAIT))
    if not sim.has_trait(trait_genderoptions_attractedto_male):
        sim.add_trait(trait_genderoptions_attractedto_male)

    trait_gloomy = instance_manager.get(get_resource_key(TRAIT_GLOOMY, Types.TRAIT))
    if sim.has_trait(trait_gloomy):
        sim.remove_trait(trait_gloomy)

    trait_greatkisser = instance_manager.get(get_resource_key(TRAIT_GREATKISSER, Types.TRAIT))
    if not sim.has_trait(trait_greatkisser):
        sim.add_trait(trait_greatkisser)

    trait_hsexit_earnedged = instance_manager.get(get_resource_key(TRAIT_HSEXIT_EARNEDGED, Types.TRAIT))
    if not sim.has_trait(trait_hsexit_earnedged):
        sim.add_trait(trait_hsexit_earnedged)

    trait_incrediblyfriendly = instance_manager.get(get_resource_key(TRAIT_INCREDIBLYFRIENDLY, Types.TRAIT))
    if not sim.has_trait(trait_incrediblyfriendly):
        sim.add_trait(trait_incrediblyfriendly)

    trait_jealous = instance_manager.get(get_resource_key(TRAIT_JEALOUS, Types.TRAIT))
    if sim.has_trait(trait_jealous):
        sim.remove_trait(trait_jealous)

    trait_kleptomaniac = instance_manager.get(get_resource_key(TRAIT_KLEPTOMANIAC, Types.TRAIT))
    if sim.has_trait(trait_kleptomaniac):
        sim.remove_trait(trait_kleptomaniac)

    trait_legendary = instance_manager.get(get_resource_key(TRAIT_LEGENDARY, Types.TRAIT))
    if not sim.has_trait(trait_legendary):
        sim.add_trait(trait_legendary)

    trait_mentor = instance_manager.get(get_resource_key(TRAIT_MENTOR, Types.TRAIT))
    if not sim.has_trait(trait_mentor):
        sim.add_trait(trait_mentor)

    trait_observant = instance_manager.get(get_resource_key(TRAIT_OBSERVANT, Types.TRAIT))
    if not sim.has_trait(trait_observant):
        sim.add_trait(trait_observant)

    trait_onewithnature = instance_manager.get(get_resource_key(TRAIT_ONEWITHNATURE, Types.TRAIT))
    if not sim.has_trait(trait_onewithnature):
        sim.add_trait(trait_onewithnature)

    trait_pamatriarch = instance_manager.get(get_resource_key(TRAIT_PAMATRIARCH, Types.TRAIT))
    if not sim.has_trait(trait_pamatriarch):
        sim.add_trait(trait_pamatriarch)

    trait_player = instance_manager.get(get_resource_key(TRAIT_PLAYER, Types.TRAIT))
    if not sim.has_trait(trait_player):
        sim.add_trait(trait_player)

    trait_reward_incest = instance_manager.get(get_resource_key(TRAIT_REWARD_INCEST, Types.TRAIT))
    if not sim.has_trait(trait_reward_incest):
        sim.add_trait(trait_reward_incest)

    trait_shameless = instance_manager.get(get_resource_key(TRAIT_SHAMELESS, Types.TRAIT))
    if not sim.has_trait(trait_shameless):
        sim.add_trait(trait_shameless)

    trait_sicknessimmunity = instance_manager.get(get_resource_key(TRAIT_SICKNESSIMMUNITY, Types.TRAIT))
    if not sim.has_trait(trait_sicknessimmunity):
        sim.add_trait(trait_sicknessimmunity)

    trait_superparent_rolemodel = instance_manager.get(get_resource_key(TRAIT_SUPERPARENT_ROLEMODEL, Types.TRAIT))
    if not sim.has_trait(trait_superparent_rolemodel):
        sim.add_trait(trait_superparent_rolemodel)

    trait_university_computersciencedegreebshonors = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_COMPUTERSCIENCEDEGREEBSHONORS, Types.TRAIT))
    if not sim.has_trait(trait_university_computersciencedegreebshonors):
        sim.add_trait(trait_university_computersciencedegreebshonors)

    trait_university_fineartdegreebahonors = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_FINEARTDEGREEBAHONORS, Types.TRAIT))
    if not sim.has_trait(trait_university_fineartdegreebahonors):
        sim.add_trait(trait_university_fineartdegreebahonors)

    trait_university_physicsdegreebshonors = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_PHYSICSDEGREEBSHONORS, Types.TRAIT))
    if not sim.has_trait(trait_university_physicsdegreebshonors):
        sim.add_trait(trait_university_physicsdegreebshonors)

    wellness_selfcareexpertise = instance_manager.get(get_resource_key(WELLNESS_SELFCAREEXPERTISE, Types.TRAIT))
    if not sim.has_trait(wellness_selfcareexpertise):
        sim.add_trait(wellness_selfcareexpertise)

    wellness_spamembership = instance_manager.get(get_resource_key(WELLNESS_SPAMEMBERSHIP, Types.TRAIT))
    if not sim.has_trait(wellness_spamembership):
        sim.add_trait(wellness_spamembership)

    wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_breastslarge = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_BODYSHAPE_BREASTSLARGE, Types.TRAIT))
    if not sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_breastslarge):
        sim.add_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_breastslarge)

    wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_buttlarge = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_BODYSHAPE_BUTTLARGE, Types.TRAIT))
    if not sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_buttlarge):
        sim.add_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_buttlarge)

    wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_black = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_HAIRCOLOR_BLACK, Types.TRAIT))
    if not sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_black):
        sim.add_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_black)

    wickedwhims_trait_nudity_nosweat_reward = instance_manager.get(get_resource_key(WICKEDWHIMS_TRAIT_NUDITY_NOSWEAT_REWARD, Types.TRAIT))
    if not sim.has_trait(wickedwhims_trait_nudity_nosweat_reward):
        sim.add_trait(wickedwhims_trait_nudity_nosweat_reward)

    wickedwhims_trait_relationships_poly = instance_manager.get(get_resource_key(WICKEDWHIMS_TRAIT_RELATIONSHIPS_POLY, Types.TRAIT))
    if not sim.has_trait(wickedwhims_trait_relationships_poly):
        sim.add_trait(wickedwhims_trait_relationships_poly)

    wickedwhims_trait_relationships_sexcheater = instance_manager.get(get_resource_key(WICKEDWHIMS_TRAIT_RELATIONSHIPS_SEXCHEATER, Types.TRAIT))
    if not sim.has_trait(wickedwhims_trait_relationships_sexcheater):
        sim.add_trait(wickedwhims_trait_relationships_sexcheater)

    wickedwhims_trait_sex_attribute_generouslover = instance_manager.get(get_resource_key(WICKEDWHIMS_TRAIT_SEX_ATTRIBUTE_GENEROUSLOVER, Types.TRAIT))
    if not sim.has_trait(wickedwhims_trait_sex_attribute_generouslover):
        sim.add_trait(wickedwhims_trait_sex_attribute_generouslover)

    wickedwhims_trait_sex_cuckold = instance_manager.get(get_resource_key(WICKEDWHIMS_TRAIT_SEX_CUCKOLD, Types.TRAIT))
    if not sim.has_trait(wickedwhims_trait_sex_cuckold):
        sim.add_trait(wickedwhims_trait_sex_cuckold)

    wickedwhims_trait_sex_sexuallyalluring = instance_manager.get(get_resource_key(WICKEDWHIMS_TRAIT_SEX_SEXUALLYALLURING, Types.TRAIT))
    if not sim.has_trait(wickedwhims_trait_sex_sexuallyalluring):
        sim.add_trait(wickedwhims_trait_sex_sexuallyalluring)

    trait_genderfemale = instance_manager.get(get_resource_key(TRAIT_GENDERFEMALE, Types.TRAIT))
    trait_gendermale = instance_manager.get(get_resource_key(TRAIT_GENDERMALE, Types.TRAIT))
    # Add Female Traits
    if sim.has_trait(trait_genderfemale):
        trait_genderoptions_clothing_womenswear = instance_manager.get(get_resource_key(TRAIT_GENDEROPTIONS_CLOTHING_WOMENSWEAR, Types.TRAIT))
        if not sim.has_trait(trait_genderoptions_clothing_womenswear):
            sim.add_trait(trait_genderoptions_clothing_womenswear)

        trait_genderoptions_frame_feminine = instance_manager.get(get_resource_key(TRAIT_GENDEROPTIONS_FRAME_FEMININE, Types.TRAIT))
        if not sim.has_trait(trait_genderoptions_frame_feminine):
            sim.add_trait(trait_genderoptions_frame_feminine)

        trait_genderoptions_frame_masculine = instance_manager.get(get_resource_key(TRAIT_GENDEROPTIONS_FRAME_MASCULINE, Types.TRAIT))
        if sim.has_trait(trait_genderoptions_frame_masculine):
            sim.remove_trait(trait_genderoptions_frame_masculine)

        trait_genderoptions_pregnancy_canbeimpregnated = instance_manager.get(get_resource_key(TRAIT_GENDEROPTIONS_PREGNANCY_CANBEIMPREGNATED, Types.TRAIT))
        if not sim.has_trait(trait_genderoptions_pregnancy_canbeimpregnated):
            sim.add_trait(trait_genderoptions_pregnancy_canbeimpregnated)

        trait_genderoptions_pregnancy_cannotimpregnate = instance_manager.get(get_resource_key(TRAIT_GENDEROPTIONS_PREGNANCY_CANNOTIMPREGNATE, Types.TRAIT))
        if not sim.has_trait(trait_genderoptions_pregnancy_cannotimpregnate):
            sim.add_trait(trait_genderoptions_pregnancy_cannotimpregnate)

        trait_neat = instance_manager.get(get_resource_key(TRAIT_NEAT, Types.TRAIT))
        if not sim.has_trait(trait_neat):
            sim.add_trait(trait_neat)

        trait_phone_color_astropink = instance_manager.get(get_resource_key(TRAIT_PHONE_COLOR_ASTROPINK, Types.TRAIT))
        if not sim.has_trait(trait_phone_color_astropink):
            sim.add_trait(trait_phone_color_astropink)

        trait_university_highereducation = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_HIGHEREDUCATION, Types.TRAIT))
        if not sim.has_trait(trait_university_highereducation):
            sim.add_trait(trait_university_highereducation)

        trait_walkstylefeminine = instance_manager.get(get_resource_key(TRAIT_WALKSTYLEFEMININE, Types.TRAIT))
        if not sim.has_trait(trait_walkstylefeminine):
            sim.add_trait(trait_walkstylefeminine)

        wickedwhims_attractiveness_trait_simpreference_dislikes_facialhair_beard = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_FACIALHAIR_BEARD, Types.TRAIT))
        if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_facialhair_beard):
            sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_facialhair_beard)

        wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_heavy = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_BODYSHAPE_HEAVY, Types.TRAIT))
        if not sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_heavy):
            sim.add_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_heavy)

        wickedwhims_attractiveness_trait_simpreference_likes_detail_body_hair = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_DETAIL_BODY_HAIR, Types.TRAIT))
        if not sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_body_hair):
            sim.add_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_body_hair)

        wickedwhims_attractiveness_trait_simpreference_likes_facialhair_beard = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_FACIALHAIR_BEARD, Types.TRAIT))
        if not sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_facialhair_beard):
            sim.add_trait(wickedwhims_attractiveness_trait_simpreference_likes_facialhair_beard)

    # Add Male Traits
    if sim.has_trait(trait_gendermale):
        trait_genderoptions_attractedto_male = instance_manager.get(get_resource_key(TRAIT_GENDEROPTIONS_ATTRACTEDTO_MALE, Types.TRAIT))
        if sim.has_trait(trait_genderoptions_attractedto_male):
            sim.remove_trait(trait_genderoptions_attractedto_male)

        trait_genderoptions_clothing_menswear = instance_manager.get(get_resource_key(TRAIT_GENDEROPTIONS_CLOTHING_MENSWEAR, Types.TRAIT))
        if not sim.has_trait(trait_genderoptions_clothing_menswear):
            sim.add_trait(trait_genderoptions_clothing_menswear)

        trait_genderoptions_clothing_womenswear = instance_manager.get(get_resource_key(TRAIT_GENDEROPTIONS_CLOTHING_WOMENSWEAR, Types.TRAIT))
        if sim.has_trait(trait_genderoptions_clothing_womenswear):
            sim.remove_trait(trait_genderoptions_clothing_womenswear)

        trait_genderoptions_frame_feminine = instance_manager.get(get_resource_key(TRAIT_GENDEROPTIONS_FRAME_FEMININE, Types.TRAIT))
        if sim.has_trait(trait_genderoptions_frame_feminine):
            sim.remove_trait(trait_genderoptions_frame_feminine)

        trait_genderoptions_frame_masculine = instance_manager.get(get_resource_key(TRAIT_GENDEROPTIONS_FRAME_MASCULINE, Types.TRAIT))
        if not sim.has_trait(trait_genderoptions_frame_masculine):
            sim.add_trait(trait_genderoptions_frame_masculine)

        trait_genderoptions_pregnancy_canimpregnate = instance_manager.get(get_resource_key(TRAIT_GENDEROPTIONS_PREGNANCY_CANIMPREGNATE, Types.TRAIT))
        if not sim.has_trait(trait_genderoptions_pregnancy_canimpregnate):
            sim.add_trait(trait_genderoptions_pregnancy_canimpregnate)

        trait_genderoptions_pregnancy_cannot_beimpregnated = instance_manager.get(get_resource_key(TRAIT_GENDEROPTIONS_PREGNANCY_CANNOT_BEIMPREGNATED, Types.TRAIT))
        if not sim.has_trait(trait_genderoptions_pregnancy_cannot_beimpregnated):
            sim.add_trait(trait_genderoptions_pregnancy_cannot_beimpregnated)

        wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_heavy = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_BODYSHAPE_HEAVY, Types.TRAIT))
        if not sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_heavy):
            sim.add_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_heavy)

        wickedwhims_attractiveness_trait_simpreference_dislikes_facialhair_beard = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_FACIALHAIR_BEARD, Types.TRAIT))
        if not sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_facialhair_beard):
            sim.add_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_facialhair_beard)

        wickedwhims_attractiveness_trait_simpreference_dislikes_hairlength_bald = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_HAIRLENGTH_BALD, Types.TRAIT))
        if not sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_hairlength_bald):
            sim.add_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_hairlength_bald)

        wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_heavy = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_BODYSHAPE_HEAVY, Types.TRAIT))
        if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_heavy):
            sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_heavy)

        wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_light = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_BODYSHAPE_LIGHT, Types.TRAIT))
        if not sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_light):
            sim.add_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_light)

        wickedwhims_attractiveness_trait_simpreference_likes_detail_body_hair = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_DETAIL_BODY_HAIR, Types.TRAIT))
        if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_body_hair):
            sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_body_hair)

        wickedwhims_attractiveness_trait_simpreference_likes_detail_freckles = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_DETAIL_FRECKLES, Types.TRAIT))
        if not sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_freckles):
            sim.add_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_freckles)

        wickedwhims_attractiveness_trait_simpreference_likes_detail_makeup = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_DETAIL_MAKEUP, Types.TRAIT))
        if not sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_makeup):
            sim.add_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_makeup)

        wickedwhims_trait_cumslut = instance_manager.get(get_resource_key(WICKEDWHIMS_TRAIT_CUMSLUT, Types.TRAIT))
        if sim.has_trait(wickedwhims_trait_cumslut):
            sim.remove_trait(wickedwhims_trait_cumslut)


@sims4.commands.Command('pbs_nanny', command_type=sims4.commands.CommandType.Live)
def pbs_nanny(_connection=None):
    # Get the console output
    output = sims4.commands.CheatOutput(_connection)

    # Get the sim_info for the active sim
    sim = services.client_manager().get(_connection).active_sim.sim_info

    # Get the tuned trait instance from the tuning instance manager
    instance_manager = services.get_instance_manager(Types.TRAIT)

    # Remove or add traits from all sims
    archaeologyskill_giveauthenticationmail_prohibit = instance_manager.get(get_resource_key(ARCHAEOLOGYSKILL_GIVEAUTHENTICATIONMAIL_PROHIBIT, Types.TRAIT))
    if not sim.has_trait(archaeologyskill_giveauthenticationmail_prohibit):
        sim.add_trait(archaeologyskill_giveauthenticationmail_prohibit)

    fametraits_celebritywalk_on = instance_manager.get(get_resource_key(FAMETRAITS_CELEBRITYWALK_ON, Types.TRAIT))
    if sim.has_trait(fametraits_celebritywalk_on):
        sim.remove_trait(fametraits_celebritywalk_on)

    fametraits_shine_off = instance_manager.get(get_resource_key(FAMETRAITS_SHINE_OFF, Types.TRAIT))
    if not sim.has_trait(fametraits_shine_off):
        sim.add_trait(fametraits_shine_off)

    fametraits_shine_on_rank4 = instance_manager.get(get_resource_key(FAMETRAITS_SHINE_ON_RANK4, Types.TRAIT))
    if sim.has_trait(fametraits_shine_on_rank4):
        sim.remove_trait(fametraits_shine_on_rank4)

    fametraits_shine_on_rank5 = instance_manager.get(get_resource_key(FAMETRAITS_SHINE_ON_RANK5, Types.TRAIT))
    if sim.has_trait(fametraits_shine_on_rank5):
        sim.remove_trait(fametraits_shine_on_rank5)

    trait_computerglasses_wearing = instance_manager.get(get_resource_key(TRAIT_COMPUTERGLASSES_WEARING, Types.TRAIT))
    if sim.has_trait(trait_computerglasses_wearing):
        sim.remove_trait(trait_computerglasses_wearing)

    trait_computerglasses_wearing_blue = instance_manager.get(get_resource_key(TRAIT_COMPUTERGLASSES_WEARING_BLUE, Types.TRAIT))
    if sim.has_trait(trait_computerglasses_wearing_blue):
        sim.remove_trait(trait_computerglasses_wearing_blue)

    trait_computerglasses_wearing_green = instance_manager.get(get_resource_key(TRAIT_COMPUTERGLASSES_WEARING_GREEN, Types.TRAIT))
    if sim.has_trait(trait_computerglasses_wearing_green):
        sim.remove_trait(trait_computerglasses_wearing_green)

    trait_computerglasses_wearing_orange = instance_manager.get(get_resource_key(TRAIT_COMPUTERGLASSES_WEARING_ORANGE, Types.TRAIT))
    if sim.has_trait(trait_computerglasses_wearing_orange):
        sim.remove_trait(trait_computerglasses_wearing_orange)

    trait_computerglasses_wearing_pink = instance_manager.get(get_resource_key(TRAIT_COMPUTERGLASSES_WEARING_PINK, Types.TRAIT))
    if sim.has_trait(trait_computerglasses_wearing_pink):
        sim.remove_trait(trait_computerglasses_wearing_pink)

    trait_computerglasses_wearing_red = instance_manager.get(get_resource_key(TRAIT_COMPUTERGLASSES_WEARING_RED, Types.TRAIT))
    if sim.has_trait(trait_computerglasses_wearing_red):
        sim.remove_trait(trait_computerglasses_wearing_red)

    trait_computerglasses_wearing_yellow = instance_manager.get(get_resource_key(TRAIT_COMPUTERGLASSES_WEARING_YELLOW, Types.TRAIT))
    if sim.has_trait(trait_computerglasses_wearing_yellow):
        sim.remove_trait(trait_computerglasses_wearing_yellow)

    trait_crystalhelmet_alabaster = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_ALABASTER, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_alabaster):
        sim.remove_trait(trait_crystalhelmet_alabaster)

    trait_crystalhelmet_alexandrite_ep = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_ALEXANDRITE_EP, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_alexandrite_ep):
        sim.remove_trait(trait_crystalhelmet_alexandrite_ep)

    trait_crystalhelmet_amazonite_ep = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_AMAZONITE_EP, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_amazonite_ep):
        sim.remove_trait(trait_crystalhelmet_amazonite_ep)

    trait_crystalhelmet_amethyst = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_AMETHYST, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_amethyst):
        sim.remove_trait(trait_crystalhelmet_amethyst)

    trait_crystalhelmet_citrine = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_CITRINE, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_citrine):
        sim.remove_trait(trait_crystalhelmet_citrine)

    trait_crystalhelmet_crandestine_ep = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_CRANDESTINE_EP, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_crandestine_ep):
        sim.remove_trait(trait_crystalhelmet_crandestine_ep)

    trait_crystalhelmet_diamond = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_DIAMOND, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_diamond):
        sim.remove_trait(trait_crystalhelmet_diamond)

    trait_crystalhelmet_emerald = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_EMERALD, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_emerald):
        sim.remove_trait(trait_crystalhelmet_emerald)

    trait_crystalhelmet_fireopal = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_FIREOPAL, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_fireopal):
        sim.remove_trait(trait_crystalhelmet_fireopal)

    trait_crystalhelmet_hematite = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_HEMATITE, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_hematite):
        sim.remove_trait(trait_crystalhelmet_hematite)

    trait_crystalhelmet_jet = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_JET, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_jet):
        sim.remove_trait(trait_crystalhelmet_jet)

    trait_crystalhelmet_jonquilyst = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_JONQUILYST, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_jonquilyst):
        sim.remove_trait(trait_crystalhelmet_jonquilyst)

    trait_crystalhelmet_nitelite_ep = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_NITELITE_EP, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_nitelite_ep):
        sim.remove_trait(trait_crystalhelmet_nitelite_ep)

    trait_crystalhelmet_orangetopaz = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_ORANGETOPAZ, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_orangetopaz):
        sim.remove_trait(trait_crystalhelmet_orangetopaz)

    trait_crystalhelmet_peach = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_PEACH, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_peach):
        sim.remove_trait(trait_crystalhelmet_peach)

    trait_crystalhelmet_plumbite = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_PLUMBITE, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_plumbite):
        sim.remove_trait(trait_crystalhelmet_plumbite)

    trait_crystalhelmet_quartz = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_QUARTZ, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_quartz):
        sim.remove_trait(trait_crystalhelmet_quartz)

    trait_crystalhelmet_rainborz = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_RAINBORZ, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_rainborz):
        sim.remove_trait(trait_crystalhelmet_rainborz)

    trait_crystalhelmet_rose = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_ROSE, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_rose):
        sim.remove_trait(trait_crystalhelmet_rose)

    trait_crystalhelmet_ruby = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_RUBY, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_ruby):
        sim.remove_trait(trait_crystalhelmet_ruby)

    trait_crystalhelmet_sapphire = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_SAPPHIRE, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_sapphire):
        sim.remove_trait(trait_crystalhelmet_sapphire)

    trait_crystalhelmet_shinalite = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_SHINALITE, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_shinalite):
        sim.remove_trait(trait_crystalhelmet_shinalite)

    trait_crystalhelmet_simanite = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_SIMANITE, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_simanite):
        sim.remove_trait(trait_crystalhelmet_simanite)

    trait_crystalhelmet_turquoise = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_TURQUOISE, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_turquoise):
        sim.remove_trait(trait_crystalhelmet_turquoise)

    trait_doctor_sicknessresistant = instance_manager.get(get_resource_key(TRAIT_DOCTOR_SICKNESSRESISTANT, Types.TRAIT))
    if not sim.has_trait(trait_doctor_sicknessresistant):
        sim.add_trait(trait_doctor_sicknessresistant)

    trait_essenceofflavor = instance_manager.get(get_resource_key(TRAIT_ESSENCEOFFLAVOR, Types.TRAIT))
    if not sim.has_trait(trait_essenceofflavor):
        sim.add_trait(trait_essenceofflavor)

    trait_fear_beingcheatedon = instance_manager.get(get_resource_key(TRAIT_FEAR_BEINGCHEATEDON, Types.TRAIT))
    if sim.has_trait(trait_fear_beingcheatedon):
        sim.remove_trait(trait_fear_beingcheatedon)

    trait_fear_beingjudged = instance_manager.get(get_resource_key(TRAIT_FEAR_BEINGJUDGED, Types.TRAIT))
    if sim.has_trait(trait_fear_beingjudged):
        sim.remove_trait(trait_fear_beingjudged)

    trait_fear_cowplant = instance_manager.get(get_resource_key(TRAIT_FEAR_COWPLANT, Types.TRAIT))
    if sim.has_trait(trait_fear_cowplant):
        sim.remove_trait(trait_fear_cowplant)

    trait_fear_crowdedplaces = instance_manager.get(get_resource_key(TRAIT_FEAR_CROWDEDPLACES, Types.TRAIT))
    if sim.has_trait(trait_fear_crowdedplaces):
        sim.remove_trait(trait_fear_crowdedplaces)

    trait_fear_dark = instance_manager.get(get_resource_key(TRAIT_FEAR_DARK, Types.TRAIT))
    if sim.has_trait(trait_fear_dark):
        sim.remove_trait(trait_fear_dark)

    trait_fear_deadendjob = instance_manager.get(get_resource_key(TRAIT_FEAR_DEADENDJOB, Types.TRAIT))
    if sim.has_trait(trait_fear_deadendjob):
        sim.remove_trait(trait_fear_deadendjob)

    trait_fear_death = instance_manager.get(get_resource_key(TRAIT_FEAR_DEATH, Types.TRAIT))
    if sim.has_trait(trait_fear_death):
        sim.remove_trait(trait_fear_death)

    trait_fear_disappointingparents = instance_manager.get(get_resource_key(TRAIT_FEAR_DISAPPOINTINGPARENTS, Types.TRAIT))
    if sim.has_trait(trait_fear_disappointingparents):
        sim.remove_trait(trait_fear_disappointingparents)

    trait_fear_disappointingparents_parentdeceasedflag = instance_manager.get(get_resource_key(TRAIT_FEAR_DISAPPOINTINGPARENTS_PARENTDECEASEDFLAG, Types.TRAIT))
    if sim.has_trait(trait_fear_disappointingparents_parentdeceasedflag):
        sim.remove_trait(trait_fear_disappointingparents_parentdeceasedflag)

    trait_fear_failing_afterschoolactivities = instance_manager.get(get_resource_key(TRAIT_FEAR_FAILING_AFTERSCHOOLACTIVITIES, Types.TRAIT))
    if sim.has_trait(trait_fear_failing_afterschoolactivities):
        sim.remove_trait(trait_fear_failing_afterschoolactivities)

    trait_fear_failing_class = instance_manager.get(get_resource_key(TRAIT_FEAR_FAILING_CLASS, Types.TRAIT))
    if sim.has_trait(trait_fear_failing_class):
        sim.remove_trait(trait_fear_failing_class)

    trait_fear_failing_tests = instance_manager.get(get_resource_key(TRAIT_FEAR_FAILING_TESTS, Types.TRAIT))
    if sim.has_trait(trait_fear_failing_tests):
        sim.remove_trait(trait_fear_failing_tests)

    trait_fear_failure = instance_manager.get(get_resource_key(TRAIT_FEAR_FAILURE, Types.TRAIT))
    if sim.has_trait(trait_fear_failure):
        sim.remove_trait(trait_fear_failure)

    trait_fear_fire = instance_manager.get(get_resource_key(TRAIT_FEAR_FIRE, Types.TRAIT))
    if sim.has_trait(trait_fear_fire):
        sim.remove_trait(trait_fear_fire)

    trait_fear_ghosts = instance_manager.get(get_resource_key(TRAIT_FEAR_GHOSTS, Types.TRAIT))
    if sim.has_trait(trait_fear_ghosts):
        sim.remove_trait(trait_fear_ghosts)

    trait_fear_homework = instance_manager.get(get_resource_key(TRAIT_FEAR_HOMEWORK, Types.TRAIT))
    if sim.has_trait(trait_fear_homework):
        sim.remove_trait(trait_fear_homework)

    trait_fear_swimming = instance_manager.get(get_resource_key(TRAIT_FEAR_SWIMMING, Types.TRAIT))
    if sim.has_trait(trait_fear_swimming):
        sim.remove_trait(trait_fear_swimming)

    trait_fear_unfulfilled = instance_manager.get(get_resource_key(TRAIT_FEAR_UNFULFILLED, Types.TRAIT))
    if sim.has_trait(trait_fear_unfulfilled):
        sim.remove_trait(trait_fear_unfulfilled)

    trait_filthdweller = instance_manager.get(get_resource_key(TRAIT_FILTHDWELLER, Types.TRAIT))
    if sim.has_trait(trait_filthdweller):
        sim.remove_trait(trait_filthdweller)

    trait_freeservices = instance_manager.get(get_resource_key(TRAIT_FREESERVICES, Types.TRAIT))
    if not sim.has_trait(trait_freeservices):
        sim.add_trait(trait_freeservices)

    trait_frugal = instance_manager.get(get_resource_key(TRAIT_FRUGAL, Types.TRAIT))
    if not sim.has_trait(trait_frugal):
        sim.add_trait(trait_frugal)

    trait_genderoptions_attractedto_notfemale = instance_manager.get(get_resource_key(TRAIT_GENDEROPTIONS_ATTRACTEDTO_NOTFEMALE, Types.TRAIT))
    if sim.has_trait(trait_genderoptions_attractedto_notfemale):
        sim.remove_trait(trait_genderoptions_attractedto_notfemale)

    trait_genderoptions_attractedto_notmale = instance_manager.get(get_resource_key(TRAIT_GENDEROPTIONS_ATTRACTEDTO_NOTMALE, Types.TRAIT))
    if sim.has_trait(trait_genderoptions_attractedto_notmale):
        sim.remove_trait(trait_genderoptions_attractedto_notmale)

    trait_genderoptions_sexuality_exploring = instance_manager.get(get_resource_key(TRAIT_GENDEROPTIONS_SEXUALITY_EXPLORING, Types.TRAIT))
    if not sim.has_trait(trait_genderoptions_sexuality_exploring):
        sim.add_trait(trait_genderoptions_sexuality_exploring)

    trait_genderoptions_sexuality_notexploring = instance_manager.get(get_resource_key(TRAIT_GENDEROPTIONS_SEXUALITY_NOTEXPLORING, Types.TRAIT))
    if sim.has_trait(trait_genderoptions_sexuality_notexploring):
        sim.remove_trait(trait_genderoptions_sexuality_notexploring)

    trait_glutton = instance_manager.get(get_resource_key(TRAIT_GLUTTON, Types.TRAIT))
    if sim.has_trait(trait_glutton):
        sim.remove_trait(trait_glutton)

    trait_gradeschool_a = instance_manager.get(get_resource_key(TRAIT_GRADESCHOOL_A, Types.TRAIT))
    if not sim.has_trait(trait_gradeschool_a):
        sim.add_trait(trait_gradeschool_a)

    trait_gradeschool_b = instance_manager.get(get_resource_key(TRAIT_GRADESCHOOL_B, Types.TRAIT))
    if sim.has_trait(trait_gradeschool_b):
        sim.remove_trait(trait_gradeschool_b)

    trait_gradeschool_c = instance_manager.get(get_resource_key(TRAIT_GRADESCHOOL_C, Types.TRAIT))
    if sim.has_trait(trait_gradeschool_c):
        sim.remove_trait(trait_gradeschool_c)

    trait_gradeschool_d = instance_manager.get(get_resource_key(TRAIT_GRADESCHOOL_D, Types.TRAIT))
    if sim.has_trait(trait_gradeschool_d):
        sim.remove_trait(trait_gradeschool_d)

    trait_gradeschool_f = instance_manager.get(get_resource_key(TRAIT_GRADESCHOOL_F, Types.TRAIT))
    if sim.has_trait(trait_gradeschool_f):
        sim.remove_trait(trait_gradeschool_f)

    trait_highschool_a = instance_manager.get(get_resource_key(TRAIT_HIGHSCHOOL_A, Types.TRAIT))
    if not sim.has_trait(trait_highschool_a):
        sim.add_trait(trait_highschool_a)

    trait_highschool_b = instance_manager.get(get_resource_key(TRAIT_HIGHSCHOOL_B, Types.TRAIT))
    if sim.has_trait(trait_highschool_b):
        sim.remove_trait(trait_highschool_b)

    trait_highschool_c = instance_manager.get(get_resource_key(TRAIT_HIGHSCHOOL_C, Types.TRAIT))
    if sim.has_trait(trait_highschool_c):
        sim.remove_trait(trait_highschool_c)

    trait_highschool_d = instance_manager.get(get_resource_key(TRAIT_HIGHSCHOOL_D, Types.TRAIT))
    if sim.has_trait(trait_highschool_d):
        sim.remove_trait(trait_highschool_d)

    trait_highschool_f = instance_manager.get(get_resource_key(TRAIT_HIGHSCHOOL_F, Types.TRAIT))
    if sim.has_trait(trait_highschool_f):
        sim.remove_trait(trait_highschool_f)

    trait_hotheaded = instance_manager.get(get_resource_key(TRAIT_HOTHEADED, Types.TRAIT))
    if sim.has_trait(trait_hotheaded):
        sim.remove_trait(trait_hotheaded)

    trait_hsexit_expelled = instance_manager.get(get_resource_key(TRAIT_HSEXIT_EXPELLED, Types.TRAIT))
    if sim.has_trait(trait_hsexit_expelled):
        sim.remove_trait(trait_hsexit_expelled)

    trait_insane = instance_manager.get(get_resource_key(TRAIT_INSANE, Types.TRAIT))
    if sim.has_trait(trait_insane):
        sim.remove_trait(trait_insane)

    trait_invested = instance_manager.get(get_resource_key(TRAIT_INVESTED, Types.TRAIT))
    if not sim.has_trait(trait_invested):
        sim.add_trait(trait_invested)

    trait_ispregnant = instance_manager.get(get_resource_key(TRAIT_ISPREGNANT, Types.TRAIT))
    if sim.has_trait(trait_ispregnant):
        sim.remove_trait(trait_ispregnant)

    trait_mechanicalsuit_hoverengaged = instance_manager.get(get_resource_key(TRAIT_MECHANICALSUIT_HOVERENGAGED, Types.TRAIT))
    if sim.has_trait(trait_mechanicalsuit_hoverengaged):
        sim.remove_trait(trait_mechanicalsuit_hoverengaged)

    trait_mechanicalsuit_wearing_body_beigewhite = instance_manager.get(get_resource_key(TRAIT_MECHANICALSUIT_WEARING_BODY_BEIGEWHITE, Types.TRAIT))
    if sim.has_trait(trait_mechanicalsuit_wearing_body_beigewhite):
        sim.remove_trait(trait_mechanicalsuit_wearing_body_beigewhite)

    trait_mechanicalsuit_wearing_body_blackblue = instance_manager.get(get_resource_key(TRAIT_MECHANICALSUIT_WEARING_BODY_BLACKBLUE, Types.TRAIT))
    if sim.has_trait(trait_mechanicalsuit_wearing_body_blackblue):
        sim.remove_trait(trait_mechanicalsuit_wearing_body_blackblue)

    trait_mechanicalsuit_wearing_body_bluered = instance_manager.get(get_resource_key(TRAIT_MECHANICALSUIT_WEARING_BODY_BLUERED, Types.TRAIT))
    if sim.has_trait(trait_mechanicalsuit_wearing_body_bluered):
        sim.remove_trait(trait_mechanicalsuit_wearing_body_bluered)

    trait_mechanicalsuit_wearing_body_graybrown = instance_manager.get(get_resource_key(TRAIT_MECHANICALSUIT_WEARING_BODY_GRAYBROWN, Types.TRAIT))
    if sim.has_trait(trait_mechanicalsuit_wearing_body_graybrown):
        sim.remove_trait(trait_mechanicalsuit_wearing_body_graybrown)

    trait_mechanicalsuit_wearing_body_greenbrown = instance_manager.get(get_resource_key(TRAIT_MECHANICALSUIT_WEARING_BODY_GREENBROWN, Types.TRAIT))
    if sim.has_trait(trait_mechanicalsuit_wearing_body_greenbrown):
        sim.remove_trait(trait_mechanicalsuit_wearing_body_greenbrown)

    trait_mechanicalsuit_wearing_body_redgreen = instance_manager.get(get_resource_key(TRAIT_MECHANICALSUIT_WEARING_BODY_REDGREEN, Types.TRAIT))
    if sim.has_trait(trait_mechanicalsuit_wearing_body_redgreen):
        sim.remove_trait(trait_mechanicalsuit_wearing_body_redgreen)

    trait_mechanicalsuit_wearing_body_whitecopper = instance_manager.get(get_resource_key(TRAIT_MECHANICALSUIT_WEARING_BODY_WHITECOPPER, Types.TRAIT))
    if sim.has_trait(trait_mechanicalsuit_wearing_body_whitecopper):
        sim.remove_trait(trait_mechanicalsuit_wearing_body_whitecopper)

    trait_mechanicalsuit_wearing_helmet_blackblue = instance_manager.get(get_resource_key(TRAIT_MECHANICALSUIT_WEARING_HELMET_BLACKBLUE, Types.TRAIT))
    if sim.has_trait(trait_mechanicalsuit_wearing_helmet_blackblue):
        sim.remove_trait(trait_mechanicalsuit_wearing_helmet_blackblue)

    trait_mechanicalsuit_wearing_helmet_blackcopper = instance_manager.get(get_resource_key(TRAIT_MECHANICALSUIT_WEARING_HELMET_BLACKCOPPER, Types.TRAIT))
    if sim.has_trait(trait_mechanicalsuit_wearing_helmet_blackcopper):
        sim.remove_trait(trait_mechanicalsuit_wearing_helmet_blackcopper)

    trait_mechanicalsuit_wearing_helmet_blackgold = instance_manager.get(get_resource_key(TRAIT_MECHANICALSUIT_WEARING_HELMET_BLACKGOLD, Types.TRAIT))
    if sim.has_trait(trait_mechanicalsuit_wearing_helmet_blackgold):
        sim.remove_trait(trait_mechanicalsuit_wearing_helmet_blackgold)

    trait_mechanicalsuit_wearing_helmet_blackgray = instance_manager.get(get_resource_key(TRAIT_MECHANICALSUIT_WEARING_HELMET_BLACKGRAY, Types.TRAIT))
    if sim.has_trait(trait_mechanicalsuit_wearing_helmet_blackgray):
        sim.remove_trait(trait_mechanicalsuit_wearing_helmet_blackgray)

    trait_mechanicalsuit_wearing_helmet_bluegray = instance_manager.get(get_resource_key(TRAIT_MECHANICALSUIT_WEARING_HELMET_BLUEGRAY, Types.TRAIT))
    if sim.has_trait(trait_mechanicalsuit_wearing_helmet_bluegray):
        sim.remove_trait(trait_mechanicalsuit_wearing_helmet_bluegray)

    trait_mechanicalsuit_wearing_helmet_grayblack = instance_manager.get(get_resource_key(TRAIT_MECHANICALSUIT_WEARING_HELMET_GRAYBLACK, Types.TRAIT))
    if sim.has_trait(trait_mechanicalsuit_wearing_helmet_grayblack):
        sim.remove_trait(trait_mechanicalsuit_wearing_helmet_grayblack)

    trait_mechanicalsuit_wearing_helmet_greenblack = instance_manager.get(get_resource_key(TRAIT_MECHANICALSUIT_WEARING_HELMET_GREENBLACK, Types.TRAIT))
    if sim.has_trait(trait_mechanicalsuit_wearing_helmet_greenblack):
        sim.remove_trait(trait_mechanicalsuit_wearing_helmet_greenblack)

    trait_nightowl_crystalhelmet = instance_manager.get(get_resource_key(TRAIT_NIGHTOWL_CRYSTALHELMET, Types.TRAIT))
    if sim.has_trait(trait_nightowl_crystalhelmet):
        sim.remove_trait(trait_nightowl_crystalhelmet)

    trait_roboticsarm_wearing_beigewhite = instance_manager.get(get_resource_key(TRAIT_ROBOTICSARM_WEARING_BEIGEWHITE, Types.TRAIT))
    if sim.has_trait(trait_roboticsarm_wearing_beigewhite):
        sim.remove_trait(trait_roboticsarm_wearing_beigewhite)

    trait_roboticsarm_wearing_blackblue = instance_manager.get(get_resource_key(TRAIT_ROBOTICSARM_WEARING_BLACKBLUE, Types.TRAIT))
    if sim.has_trait(trait_roboticsarm_wearing_blackblue):
        sim.remove_trait(trait_roboticsarm_wearing_blackblue)

    trait_roboticsarm_wearing_bluered = instance_manager.get(get_resource_key(TRAIT_ROBOTICSARM_WEARING_BLUERED, Types.TRAIT))
    if sim.has_trait(trait_roboticsarm_wearing_bluered):
        sim.remove_trait(trait_roboticsarm_wearing_bluered)

    trait_roboticsarm_wearing_graybrown = instance_manager.get(get_resource_key(TRAIT_ROBOTICSARM_WEARING_GRAYBROWN, Types.TRAIT))
    if sim.has_trait(trait_roboticsarm_wearing_graybrown):
        sim.remove_trait(trait_roboticsarm_wearing_graybrown)

    trait_roboticsarm_wearing_greenbrown = instance_manager.get(get_resource_key(TRAIT_ROBOTICSARM_WEARING_GREENBROWN, Types.TRAIT))
    if sim.has_trait(trait_roboticsarm_wearing_greenbrown):
        sim.remove_trait(trait_roboticsarm_wearing_greenbrown)

    trait_roboticsarm_wearing_redgreen = instance_manager.get(get_resource_key(TRAIT_ROBOTICSARM_WEARING_REDGREEN, Types.TRAIT))
    if sim.has_trait(trait_roboticsarm_wearing_redgreen):
        sim.remove_trait(trait_roboticsarm_wearing_redgreen)

    trait_roboticsarm_wearing_whitecopper = instance_manager.get(get_resource_key(TRAIT_ROBOTICSARM_WEARING_WHITECOPPER, Types.TRAIT))
    if sim.has_trait(trait_roboticsarm_wearing_whitecopper):
        sim.remove_trait(trait_roboticsarm_wearing_whitecopper)

    trait_selfassured = instance_manager.get(get_resource_key(TRAIT_SELFASSURED, Types.TRAIT))
    if not sim.has_trait(trait_selfassured):
        sim.add_trait(trait_selfassured)

    trait_sexualorientation_woohoointerests_female = instance_manager.get(get_resource_key(TRAIT_SEXUALORIENTATION_WOOHOOINTERESTS_FEMALE, Types.TRAIT))
    if not sim.has_trait(trait_sexualorientation_woohoointerests_female):
        sim.add_trait(trait_sexualorientation_woohoointerests_female)

    trait_sexualorientation_woohoointerests_male = instance_manager.get(get_resource_key(TRAIT_SEXUALORIENTATION_WOOHOOINTERESTS_MALE, Types.TRAIT))
    if not sim.has_trait(trait_sexualorientation_woohoointerests_male):
        sim.add_trait(trait_sexualorientation_woohoointerests_male)

    trait_sexualorientation_woohoointerests_notfemale = instance_manager.get(get_resource_key(TRAIT_SEXUALORIENTATION_WOOHOOINTERESTS_NOTFEMALE, Types.TRAIT))
    if sim.has_trait(trait_sexualorientation_woohoointerests_notfemale):
        sim.remove_trait(trait_sexualorientation_woohoointerests_notfemale)

    trait_simpreference_dislikes_activities_djmixing = instance_manager.get(get_resource_key(TRAIT_SIMPREFERENCE_DISLIKES_ACTIVITIES_DJMIXING, Types.TRAIT))
    if sim.has_trait(trait_simpreference_dislikes_activities_djmixing):
        sim.remove_trait(trait_simpreference_dislikes_activities_djmixing)

    trait_simpreference_dislikes_activities_fitness = instance_manager.get(get_resource_key(TRAIT_SIMPREFERENCE_DISLIKES_ACTIVITIES_FITNESS, Types.TRAIT))
    if sim.has_trait(trait_simpreference_dislikes_activities_fitness):
        sim.remove_trait(trait_simpreference_dislikes_activities_fitness)

    trait_simpreference_dislikes_activities_guitar = instance_manager.get(get_resource_key(TRAIT_SIMPREFERENCE_DISLIKES_ACTIVITIES_GUITAR, Types.TRAIT))
    if sim.has_trait(trait_simpreference_dislikes_activities_guitar):
        sim.remove_trait(trait_simpreference_dislikes_activities_guitar)

    trait_simpreference_dislikes_activities_piano = instance_manager.get(get_resource_key(TRAIT_SIMPREFERENCE_DISLIKES_ACTIVITIES_PIANO, Types.TRAIT))
    if sim.has_trait(trait_simpreference_dislikes_activities_piano):
        sim.remove_trait(trait_simpreference_dislikes_activities_piano)

    trait_simpreference_dislikes_activities_pipeorgan = instance_manager.get(get_resource_key(TRAIT_SIMPREFERENCE_DISLIKES_ACTIVITIES_PIPEORGAN, Types.TRAIT))
    if sim.has_trait(trait_simpreference_dislikes_activities_pipeorgan):
        sim.remove_trait(trait_simpreference_dislikes_activities_pipeorgan)

    trait_simpreference_dislikes_activities_programming = instance_manager.get(get_resource_key(TRAIT_SIMPREFERENCE_DISLIKES_ACTIVITIES_PROGRAMMING, Types.TRAIT))
    if sim.has_trait(trait_simpreference_dislikes_activities_programming):
        sim.remove_trait(trait_simpreference_dislikes_activities_programming)

    trait_simpreference_dislikes_activities_rockclimbing = instance_manager.get(get_resource_key(TRAIT_SIMPREFERENCE_DISLIKES_ACTIVITIES_ROCKCLIMBING, Types.TRAIT))
    if sim.has_trait(trait_simpreference_dislikes_activities_rockclimbing):
        sim.remove_trait(trait_simpreference_dislikes_activities_rockclimbing)

    trait_simpreference_dislikes_activities_singing = instance_manager.get(get_resource_key(TRAIT_SIMPREFERENCE_DISLIKES_ACTIVITIES_SINGING, Types.TRAIT))
    if sim.has_trait(trait_simpreference_dislikes_activities_singing):
        sim.remove_trait(trait_simpreference_dislikes_activities_singing)

    trait_simpreference_dislikes_activities_violin = instance_manager.get(get_resource_key(TRAIT_SIMPREFERENCE_DISLIKES_ACTIVITIES_VIOLIN, Types.TRAIT))
    if sim.has_trait(trait_simpreference_dislikes_activities_violin):
        sim.remove_trait(trait_simpreference_dislikes_activities_violin)

    trait_simpreference_dislikes_activities_wellness = instance_manager.get(get_resource_key(TRAIT_SIMPREFERENCE_DISLIKES_ACTIVITIES_WELLNESS, Types.TRAIT))
    if sim.has_trait(trait_simpreference_dislikes_activities_wellness):
        sim.remove_trait(trait_simpreference_dislikes_activities_wellness)

    trait_simpreference_dislikes_activities_writing = instance_manager.get(get_resource_key(TRAIT_SIMPREFERENCE_DISLIKES_ACTIVITIES_WRITING, Types.TRAIT))
    if sim.has_trait(trait_simpreference_dislikes_activities_writing):
        sim.remove_trait(trait_simpreference_dislikes_activities_writing)

    trait_simpreference_likes_activities_fitness = instance_manager.get(get_resource_key(TRAIT_SIMPREFERENCE_LIKES_ACTIVITIES_FITNESS, Types.TRAIT))
    if not sim.has_trait(trait_simpreference_likes_activities_fitness):
        sim.add_trait(trait_simpreference_likes_activities_fitness)

    trait_simpreference_likes_activities_wellness = instance_manager.get(get_resource_key(TRAIT_SIMPREFERENCE_LIKES_ACTIVITIES_WELLNESS, Types.TRAIT))
    if not sim.has_trait(trait_simpreference_likes_activities_wellness):
        sim.add_trait(trait_simpreference_likes_activities_wellness)

    trait_simpreference_noopinion_activities_fitness = instance_manager.get(get_resource_key(TRAIT_SIMPREFERENCE_NOOPINION_ACTIVITIES_FITNESS, Types.TRAIT))
    if sim.has_trait(trait_simpreference_noopinion_activities_fitness):
        sim.remove_trait(trait_simpreference_noopinion_activities_fitness)

    trait_simpreference_noopinion_activities_wellness = instance_manager.get(get_resource_key(TRAIT_SIMPREFERENCE_NOOPINION_ACTIVITIES_WELLNESS, Types.TRAIT))
    if sim.has_trait(trait_simpreference_noopinion_activities_wellness):
        sim.remove_trait(trait_simpreference_noopinion_activities_wellness)

    trait_slob = instance_manager.get(get_resource_key(TRAIT_SLOB, Types.TRAIT))
    if sim.has_trait(trait_slob):
        sim.remove_trait(trait_slob)

    trait_speedcleaner = instance_manager.get(get_resource_key(TRAIT_SPEEDCLEANER, Types.TRAIT))
    if not sim.has_trait(trait_speedcleaner):
        sim.add_trait(trait_speedcleaner)

    trait_speedreader = instance_manager.get(get_resource_key(TRAIT_SPEEDREADER, Types.TRAIT))
    if not sim.has_trait(trait_speedreader):
        sim.add_trait(trait_speedreader)

    trait_stormchaser = instance_manager.get(get_resource_key(TRAIT_STORMCHASER, Types.TRAIT))
    if not sim.has_trait(trait_stormchaser):
        sim.add_trait(trait_stormchaser)

    trait_temperature_burningman = instance_manager.get(get_resource_key(TRAIT_TEMPERATURE_BURNINGMAN, Types.TRAIT))
    if not sim.has_trait(trait_temperature_burningman):
        sim.add_trait(trait_temperature_burningman)

    trait_temperature_coldacclimation = instance_manager.get(get_resource_key(TRAIT_TEMPERATURE_COLDACCLIMATION, Types.TRAIT))
    if sim.has_trait(trait_temperature_coldacclimation):
        sim.remove_trait(trait_temperature_coldacclimation)

    trait_temperature_heatacclimation = instance_manager.get(get_resource_key(TRAIT_TEMPERATURE_HEATACCLIMATION, Types.TRAIT))
    if sim.has_trait(trait_temperature_heatacclimation):
        sim.remove_trait(trait_temperature_heatacclimation)

    trait_temperature_iceman = instance_manager.get(get_resource_key(TRAIT_TEMPERATURE_ICEMAN, Types.TRAIT))
    if not sim.has_trait(trait_temperature_iceman):
        sim.add_trait(trait_temperature_iceman)

    trait_theknack = instance_manager.get(get_resource_key(TRAIT_THEKNACK, Types.TRAIT))
    if not sim.has_trait(trait_theknack):
        sim.add_trait(trait_theknack)

    trait_university_arthistorydegreeba = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_ARTHISTORYDEGREEBA, Types.TRAIT))
    if sim.has_trait(trait_university_arthistorydegreeba):
        sim.remove_trait(trait_university_arthistorydegreeba)

    trait_university_arthistorydegreebs = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_ARTHISTORYDEGREEBS, Types.TRAIT))
    if sim.has_trait(trait_university_arthistorydegreebs):
        sim.remove_trait(trait_university_arthistorydegreebs)

    trait_university_biologydegreeba = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_BIOLOGYDEGREEBA, Types.TRAIT))
    if sim.has_trait(trait_university_biologydegreeba):
        sim.remove_trait(trait_university_biologydegreeba)

    trait_university_biologydegreebs = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_BIOLOGYDEGREEBS, Types.TRAIT))
    if sim.has_trait(trait_university_biologydegreebs):
        sim.remove_trait(trait_university_biologydegreebs)

    trait_university_communicationsdegreeba = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_COMMUNICATIONSDEGREEBA, Types.TRAIT))
    if sim.has_trait(trait_university_communicationsdegreeba):
        sim.remove_trait(trait_university_communicationsdegreeba)

    trait_university_communicationsdegreebs = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_COMMUNICATIONSDEGREEBS, Types.TRAIT))
    if sim.has_trait(trait_university_communicationsdegreebs):
        sim.remove_trait(trait_university_communicationsdegreebs)

    trait_university_computersciencedegreeba = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_COMPUTERSCIENCEDEGREEBA, Types.TRAIT))
    if sim.has_trait(trait_university_computersciencedegreeba):
        sim.remove_trait(trait_university_computersciencedegreeba)

    trait_university_computersciencedegreebs = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_COMPUTERSCIENCEDEGREEBS, Types.TRAIT))
    if sim.has_trait(trait_university_computersciencedegreebs):
        sim.remove_trait(trait_university_computersciencedegreebs)

    trait_university_culinaryartsdegreeba = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_CULINARYARTSDEGREEBA, Types.TRAIT))
    if sim.has_trait(trait_university_culinaryartsdegreeba):
        sim.remove_trait(trait_university_culinaryartsdegreeba)

    trait_university_culinaryartsdegreebs = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_CULINARYARTSDEGREEBS, Types.TRAIT))
    if sim.has_trait(trait_university_culinaryartsdegreebs):
        sim.remove_trait(trait_university_culinaryartsdegreebs)

    trait_university_dramadegreeba = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_DRAMADEGREEBA, Types.TRAIT))
    if sim.has_trait(trait_university_dramadegreeba):
        sim.remove_trait(trait_university_dramadegreeba)

    trait_university_dramadegreebs = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_DRAMADEGREEBS, Types.TRAIT))
    if sim.has_trait(trait_university_dramadegreebs):
        sim.remove_trait(trait_university_dramadegreebs)

    trait_university_economicsdegreeba = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_ECONOMICSDEGREEBA, Types.TRAIT))
    if sim.has_trait(trait_university_economicsdegreeba):
        sim.remove_trait(trait_university_economicsdegreeba)

    trait_university_economicsdegreebs = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_ECONOMICSDEGREEBS, Types.TRAIT))
    if sim.has_trait(trait_university_economicsdegreebs):
        sim.remove_trait(trait_university_economicsdegreebs)

    trait_university_fineartdegreeba = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_FINEARTDEGREEBA, Types.TRAIT))
    if sim.has_trait(trait_university_fineartdegreeba):
        sim.remove_trait(trait_university_fineartdegreeba)

    trait_university_fineartdegreebs = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_FINEARTDEGREEBS, Types.TRAIT))
    if sim.has_trait(trait_university_fineartdegreebs):
        sim.remove_trait(trait_university_fineartdegreebs)

    trait_university_historydegreeba = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_HISTORYDEGREEBA, Types.TRAIT))
    if sim.has_trait(trait_university_historydegreeba):
        sim.remove_trait(trait_university_historydegreeba)

    trait_university_historydegreebs = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_HISTORYDEGREEBS, Types.TRAIT))
    if sim.has_trait(trait_university_historydegreebs):
        sim.remove_trait(trait_university_historydegreebs)

    trait_university_languageandliteraturedegreeba = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_LANGUAGEANDLITERATUREDEGREEBA, Types.TRAIT))
    if sim.has_trait(trait_university_languageandliteraturedegreeba):
        sim.remove_trait(trait_university_languageandliteraturedegreeba)

    trait_university_languageandliteraturedegreebs = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_LANGUAGEANDLITERATUREDEGREEBS, Types.TRAIT))
    if sim.has_trait(trait_university_languageandliteraturedegreebs):
        sim.remove_trait(trait_university_languageandliteraturedegreebs)

    trait_university_physicsdegreeba = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_PHYSICSDEGREEBA, Types.TRAIT))
    if sim.has_trait(trait_university_physicsdegreeba):
        sim.remove_trait(trait_university_physicsdegreeba)

    trait_university_physicsdegreebs = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_PHYSICSDEGREEBS, Types.TRAIT))
    if sim.has_trait(trait_university_physicsdegreebs):
        sim.remove_trait(trait_university_physicsdegreebs)

    trait_university_psychologydegreeba = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_PSYCHOLOGYDEGREEBA, Types.TRAIT))
    if sim.has_trait(trait_university_psychologydegreeba):
        sim.remove_trait(trait_university_psychologydegreeba)

    trait_university_psychologydegreebs = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_PSYCHOLOGYDEGREEBS, Types.TRAIT))
    if sim.has_trait(trait_university_psychologydegreebs):
        sim.remove_trait(trait_university_psychologydegreebs)

    trait_university_villainydegreeba = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_VILLAINYDEGREEBA, Types.TRAIT))
    if sim.has_trait(trait_university_villainydegreeba):
        sim.remove_trait(trait_university_villainydegreeba)

    trait_university_villainydegreebs = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_VILLAINYDEGREEBS, Types.TRAIT))
    if sim.has_trait(trait_university_villainydegreebs):
        sim.remove_trait(trait_university_villainydegreebs)

    trait_walkstylecreepy = instance_manager.get(get_resource_key(TRAIT_WALKSTYLECREEPY, Types.TRAIT))
    if sim.has_trait(trait_walkstylecreepy):
        sim.remove_trait(trait_walkstylecreepy)

    trait_walkstyleenergetic = instance_manager.get(get_resource_key(TRAIT_WALKSTYLEENERGETIC, Types.TRAIT))
    if sim.has_trait(trait_walkstyleenergetic):
        sim.remove_trait(trait_walkstyleenergetic)

    trait_walkstyleenergetic = instance_manager.get(get_resource_key(TRAIT_WALKSTYLEENERGETIC, Types.TRAIT))
    if sim.has_trait(trait_walkstyleenergetic):
        sim.remove_trait(trait_walkstyleenergetic)

    trait_walkstylefeminine = instance_manager.get(get_resource_key(TRAIT_WALKSTYLEFEMININE, Types.TRAIT))
    if sim.has_trait(trait_walkstylefeminine):
        sim.remove_trait(trait_walkstylefeminine)

    trait_walkstylegoofy = instance_manager.get(get_resource_key(TRAIT_WALKSTYLEGOOFY, Types.TRAIT))
    if sim.has_trait(trait_walkstylegoofy):
        sim.remove_trait(trait_walkstylegoofy)

    trait_walkstyleperky = instance_manager.get(get_resource_key(TRAIT_WALKSTYLEPERKY, Types.TRAIT))
    if sim.has_trait(trait_walkstyleperky):
        sim.remove_trait(trait_walkstyleperky)

    trait_walkstylesleepy = instance_manager.get(get_resource_key(TRAIT_WALKSTYLESLEEPY, Types.TRAIT))
    if sim.has_trait(trait_walkstylesleepy):
        sim.remove_trait(trait_walkstylesleepy)

    trait_walkstylesnooty = instance_manager.get(get_resource_key(TRAIT_WALKSTYLESNOOTY, Types.TRAIT))
    if sim.has_trait(trait_walkstylesnooty):
        sim.remove_trait(trait_walkstylesnooty)

    trait_walkstyleswagger = instance_manager.get(get_resource_key(TRAIT_WALKSTYLESWAGGER, Types.TRAIT))
    if sim.has_trait(trait_walkstyleswagger):
        sim.remove_trait(trait_walkstyleswagger)

    trait_walkstyletough = instance_manager.get(get_resource_key(TRAIT_WALKSTYLETOUGH, Types.TRAIT))
    if sim.has_trait(trait_walkstyletough):
        sim.remove_trait(trait_walkstyletough)

    trait_waterproof = instance_manager.get(get_resource_key(TRAIT_WATERPROOF, Types.TRAIT))
    if not sim.has_trait(trait_waterproof):
        sim.add_trait(trait_waterproof)

    trait_webmaster = instance_manager.get(get_resource_key(TRAIT_WEBMASTER, Types.TRAIT))
    if not sim.has_trait(trait_webmaster):
        sim.add_trait(trait_webmaster)

    wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_breastslarge = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_BODYSHAPE_BREASTSLARGE, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_breastslarge):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_breastslarge)

    wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_breastssmall = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_BODYSHAPE_BREASTSSMALL, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_breastssmall):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_breastssmall)

    wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_buttlarge = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_BODYSHAPE_BUTTLARGE, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_buttlarge):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_buttlarge)

    wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_buttsmall = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_BODYSHAPE_BUTTSMALL, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_buttsmall):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_buttsmall)

    wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_heavy = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_BODYSHAPE_HEAVY, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_heavy):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_heavy)

    wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_high = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_BODYSHAPE_HIGH, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_high):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_high)

    wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_light = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_BODYSHAPE_LIGHT, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_light):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_light)

    wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_low = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_BODYSHAPE_LOW, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_low):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_low)

    wickedwhims_attractiveness_trait_simpreference_dislikes_detail_body_hair = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_DETAIL_BODY_HAIR, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_detail_body_hair):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_detail_body_hair)

    wickedwhims_attractiveness_trait_simpreference_dislikes_detail_freckles = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_DETAIL_FRECKLES, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_detail_freckles):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_detail_freckles)

    wickedwhims_attractiveness_trait_simpreference_dislikes_detail_glasses = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_DETAIL_GLASSES, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_detail_glasses):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_detail_glasses)

    wickedwhims_attractiveness_trait_simpreference_dislikes_detail_hats = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_DETAIL_HATS, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_detail_hats):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_detail_hats)

    wickedwhims_attractiveness_trait_simpreference_dislikes_detail_jewelery = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_DETAIL_JEWELERY, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_detail_jewelery):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_detail_jewelery)

    wickedwhims_attractiveness_trait_simpreference_dislikes_detail_makeup = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_DETAIL_MAKEUP, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_detail_makeup):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_detail_makeup)

    wickedwhims_attractiveness_trait_simpreference_dislikes_detail_piercing = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_DETAIL_PIERCING, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_detail_piercing):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_detail_piercing)

    wickedwhims_attractiveness_trait_simpreference_dislikes_detail_tattoos = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_DETAIL_TATTOOS, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_detail_tattoos):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_detail_tattoos)

    wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_blue = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_EYECOLOR_BLUE, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_blue):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_blue)

    wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_blue = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_EYECOLOR_BLUE, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_blue):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_blue)

    wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_brown = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_EYECOLOR_BROWN, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_brown):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_brown)

    wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_brown = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_EYECOLOR_BROWN, Types.TRAIT))
    if not sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_brown):
        sim.add_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_brown)

    wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_green = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_EYECOLOR_GREEN, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_green):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_green)

    wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_green = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_EYECOLOR_GREEN, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_green):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_green)

    wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_unnatural = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_EYECOLOR_UNNATURAL, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_unnatural):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_unnatural)

    wickedwhims_attractiveness_trait_simpreference_dislikes_facialhair_beard = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_FACIALHAIR_BEARD, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_facialhair_beard):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_facialhair_beard)

    wickedwhims_attractiveness_trait_simpreference_dislikes_facialhair_clean = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_FACIALHAIR_CLEAN, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_facialhair_clean):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_facialhair_clean)

    wickedwhims_attractiveness_trait_simpreference_dislikes_facialhair_goatee = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_FACIALHAIR_GOATEE, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_facialhair_goatee):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_facialhair_goatee)

    wickedwhims_attractiveness_trait_simpreference_dislikes_facialhair_mustache = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_FACIALHAIR_MUSTACHE, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_facialhair_mustache):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_facialhair_mustache)

    wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_black = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_HAIRCOLOR_BLACK, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_black):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_black)

    wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_blonde = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_HAIRCOLOR_BLONDE, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_blonde):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_blonde)

    wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_blonde = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_HAIRCOLOR_BLONDE, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_blonde):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_blonde)

    wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_blue = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_HAIRCOLOR_BLUE, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_blue):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_blue)

    wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_blue = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_HAIRCOLOR_BLUE, Types.TRAIT))
    if not sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_blue):
        sim.add_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_blue)

    wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_brown = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_HAIRCOLOR_BROWN, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_brown):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_brown)

    wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_brown = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_HAIRCOLOR_BROWN, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_brown):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_brown)

    wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_gray = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_HAIRCOLOR_GRAY, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_gray):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_gray)

    wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_green = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_HAIRCOLOR_GREEN, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_green):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_green)

    wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_green = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_HAIRCOLOR_GREEN, Types.TRAIT))
    if not sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_green):
        sim.add_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_green)

    wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_pink = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_HAIRCOLOR_PINK, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_pink):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_pink)

    wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_red = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_HAIRCOLOR_RED, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_red):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_red)

    wickedwhims_attractiveness_trait_simpreference_dislikes_hairlength_bald = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_HAIRLENGTH_BALD, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_hairlength_bald):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_hairlength_bald)

    wickedwhims_attractiveness_trait_simpreference_dislikes_hairlength_bald = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_HAIRLENGTH_BALD, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_hairlength_bald):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_hairlength_bald)

    wickedwhims_attractiveness_trait_simpreference_dislikes_hairlength_long = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_HAIRLENGTH_LONG, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_hairlength_long):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_hairlength_long)

    wickedwhims_attractiveness_trait_simpreference_dislikes_hairlength_medium = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_HAIRLENGTH_MEDIUM, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_hairlength_medium):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_hairlength_medium)

    wickedwhims_attractiveness_trait_simpreference_dislikes_hairlength_short = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_HAIRLENGTH_SHORT, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_hairlength_short):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_hairlength_short)

    wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_breastslarge = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_BODYSHAPE_BREASTSLARGE, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_breastslarge):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_breastslarge)

    wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_breastssmall = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_BODYSHAPE_BREASTSSMALL, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_breastssmall):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_breastssmall)

    wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_breastssmall = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_BODYSHAPE_BREASTSSMALL, Types.TRAIT))
    if not sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_breastssmall):
        sim.add_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_breastssmall)

    wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_buttlarge = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_BODYSHAPE_BUTTLARGE, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_buttlarge):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_buttlarge)

    wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_buttlarge = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_BODYSHAPE_BUTTLARGE, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_buttlarge):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_buttlarge)

    wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_buttsmall = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_BODYSHAPE_BUTTSMALL, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_buttsmall):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_buttsmall)

    wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_buttsmall = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_BODYSHAPE_BUTTSMALL, Types.TRAIT))
    if not sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_buttsmall):
        sim.add_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_buttsmall)

    wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_heavy = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_BODYSHAPE_HEAVY, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_heavy):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_heavy)

    wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_high = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_BODYSHAPE_HIGH, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_high):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_high)

    wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_light = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_BODYSHAPE_LIGHT, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_light):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_light)

    wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_low = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_BODYSHAPE_LOW, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_low):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_low)

    wickedwhims_attractiveness_trait_simpreference_likes_detail_body_hair = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_DETAIL_BODY_HAIR, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_body_hair):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_body_hair)

    wickedwhims_attractiveness_trait_simpreference_likes_detail_freckles = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_DETAIL_FRECKLES, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_freckles):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_freckles)

    wickedwhims_attractiveness_trait_simpreference_likes_detail_glasses = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_DETAIL_GLASSES, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_glasses):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_glasses)

    wickedwhims_attractiveness_trait_simpreference_likes_detail_glasses = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_DETAIL_GLASSES, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_glasses):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_glasses)

    wickedwhims_attractiveness_trait_simpreference_likes_detail_hats = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_DETAIL_HATS, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_hats):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_hats)

    wickedwhims_attractiveness_trait_simpreference_likes_detail_hats = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_DETAIL_HATS, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_hats):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_hats)

    wickedwhims_attractiveness_trait_simpreference_likes_detail_jewelery = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_DETAIL_JEWELERY, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_jewelery):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_jewelery)

    wickedwhims_attractiveness_trait_simpreference_likes_detail_makeup = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_DETAIL_MAKEUP, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_makeup):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_makeup)

    wickedwhims_attractiveness_trait_simpreference_likes_detail_piercing = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_DETAIL_PIERCING, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_piercing):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_piercing)

    wickedwhims_attractiveness_trait_simpreference_likes_detail_tattoos = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_DETAIL_TATTOOS, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_tattoos):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_tattoos)

    wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_blue = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_EYECOLOR_BLUE, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_blue):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_blue)

    wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_blue = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_EYECOLOR_BLUE, Types.TRAIT))
    if not sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_blue):
        sim.add_trait(wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_blue)

    wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_brown = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_EYECOLOR_BROWN, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_brown):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_brown)

    wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_brown = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_EYECOLOR_BROWN, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_brown):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_brown)

    wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_green = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_EYECOLOR_GREEN, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_green):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_green)

    wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_green = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_EYECOLOR_GREEN, Types.TRAIT))
    if not sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_green):
        sim.add_trait(wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_green)

    wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_unnatural = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_EYECOLOR_UNNATURAL, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_unnatural):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_unnatural)

    wickedwhims_attractiveness_trait_simpreference_likes_facialhair_beard = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_FACIALHAIR_BEARD, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_facialhair_beard):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_facialhair_beard)

    wickedwhims_attractiveness_trait_simpreference_likes_facialhair_clean = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_FACIALHAIR_CLEAN, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_facialhair_clean):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_facialhair_clean)

    wickedwhims_attractiveness_trait_simpreference_likes_facialhair_goatee = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_FACIALHAIR_GOATEE, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_facialhair_goatee):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_facialhair_goatee)

    wickedwhims_attractiveness_trait_simpreference_likes_facialhair_mustache = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_FACIALHAIR_MUSTACHE, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_facialhair_mustache):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_facialhair_mustache)

    wickedwhims_attractiveness_trait_simpreference_likes_haircolor_black = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_HAIRCOLOR_BLACK, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_black):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_black)

    wickedwhims_attractiveness_trait_simpreference_likes_haircolor_blonde = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_HAIRCOLOR_BLONDE, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_blonde):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_blonde)

    wickedwhims_attractiveness_trait_simpreference_likes_haircolor_blonde = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_HAIRCOLOR_BLONDE, Types.TRAIT))
    if not sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_blonde):
        sim.add_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_blonde)

    wickedwhims_attractiveness_trait_simpreference_likes_haircolor_blue = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_HAIRCOLOR_BLUE, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_blue):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_blue)

    wickedwhims_attractiveness_trait_simpreference_likes_haircolor_brown = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_HAIRCOLOR_BROWN, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_brown):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_brown)

    wickedwhims_attractiveness_trait_simpreference_likes_haircolor_brown = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_HAIRCOLOR_BROWN, Types.TRAIT))
    if not sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_brown):
        sim.add_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_brown)

    wickedwhims_attractiveness_trait_simpreference_likes_haircolor_gray = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_HAIRCOLOR_GRAY, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_gray):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_gray)

    wickedwhims_attractiveness_trait_simpreference_likes_haircolor_green = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_HAIRCOLOR_GREEN, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_green):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_green)

    wickedwhims_attractiveness_trait_simpreference_likes_haircolor_pink = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_HAIRCOLOR_PINK, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_pink):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_pink)

    wickedwhims_attractiveness_trait_simpreference_likes_haircolor_red = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_HAIRCOLOR_RED, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_red):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_red)

    wickedwhims_attractiveness_trait_simpreference_likes_hairlength_bald = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_HAIRLENGTH_BALD, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_hairlength_bald):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_hairlength_bald)

    wickedwhims_attractiveness_trait_simpreference_likes_hairlength_long = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_HAIRLENGTH_LONG, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_hairlength_long):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_hairlength_long)

    wickedwhims_attractiveness_trait_simpreference_likes_hairlength_medium = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_HAIRLENGTH_MEDIUM, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_hairlength_medium):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_hairlength_medium)

    wickedwhims_attractiveness_trait_simpreference_likes_hairlength_short = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_HAIRLENGTH_SHORT, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_hairlength_short):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_hairlength_short)

    wickedwhims_trait_attractivenessblacklist = instance_manager.get(get_resource_key(WICKEDWHIMS_TRAIT_ATTRACTIVENESSBLACKLIST, Types.TRAIT))
    if sim.has_trait(wickedwhims_trait_attractivenessblacklist):
        sim.remove_trait(wickedwhims_trait_attractivenessblacklist)

    wickedwhims_trait_bodyhair_pubichair_isdisabled = instance_manager.get(get_resource_key(WICKEDWHIMS_TRAIT_BODYHAIR_PUBICHAIR_ISDISABLED, Types.TRAIT))
    if not sim.has_trait(wickedwhims_trait_bodyhair_pubichair_isdisabled):
        sim.add_trait(wickedwhims_trait_bodyhair_pubichair_isdisabled)

    wickedwhims_trait_bodyhair_pubichair_isgrowthdisabled = instance_manager.get(get_resource_key(WICKEDWHIMS_TRAIT_BODYHAIR_PUBICHAIR_ISGROWTHDISABLED, Types.TRAIT))
    if not sim.has_trait(wickedwhims_trait_bodyhair_pubichair_isgrowthdisabled):
        sim.add_trait(wickedwhims_trait_bodyhair_pubichair_isgrowthdisabled)

    wickedwhims_trait_cumslut = instance_manager.get(get_resource_key(WICKEDWHIMS_TRAIT_CUMSLUT, Types.TRAIT))
    if not sim.has_trait(wickedwhims_trait_cumslut):
        sim.add_trait(wickedwhims_trait_cumslut)

    wickedwhims_trait_improved_absorbency = instance_manager.get(get_resource_key(WICKEDWHIMS_TRAIT_IMPROVED_ABSORBENCY, Types.TRAIT))
    if not sim.has_trait(wickedwhims_trait_improved_absorbency):
        sim.add_trait(wickedwhims_trait_improved_absorbency)

    wickedwhims_trait_postpubertyteen = instance_manager.get(get_resource_key(WICKEDWHIMS_TRAIT_POSTPUBERTYTEEN, Types.TRAIT))
    if not sim.has_trait(wickedwhims_trait_postpubertyteen):
        sim.add_trait(wickedwhims_trait_postpubertyteen)

    wickedwhims_trait_sex_attribute_badatsex = instance_manager.get(get_resource_key(WICKEDWHIMS_TRAIT_SEX_ATTRIBUTE_BADATSEX, Types.TRAIT))
    if sim.has_trait(wickedwhims_trait_sex_attribute_badatsex):
        sim.remove_trait(wickedwhims_trait_sex_attribute_badatsex)

    wickedwhims_trait_sex_sexuallyabstinent = instance_manager.get(get_resource_key(WICKEDWHIMS_TRAIT_SEX_SEXUALLYABSTINENT, Types.TRAIT))
    if sim.has_trait(wickedwhims_trait_sex_sexuallyabstinent):
        sim.remove_trait(wickedwhims_trait_sex_sexuallyabstinent)


    # Remove or add traits from nanny sims
    trait_alluring = instance_manager.get(get_resource_key(TRAIT_ALLURING, Types.TRAIT))
    if not sim.has_trait(trait_alluring):
        sim.add_trait(trait_alluring)

    trait_dastardly = instance_manager.get(get_resource_key(TRAIT_DASTARDLY, Types.TRAIT))
    if sim.has_trait(trait_dastardly):
        sim.remove_trait(trait_dastardly)

    trait_evil = instance_manager.get(get_resource_key(TRAIT_EVIL, Types.TRAIT))
    if sim.has_trait(trait_evil):
        sim.remove_trait(trait_evil)

    trait_freshchef = instance_manager.get(get_resource_key(TRAIT_FRESHCHEF, Types.TRAIT))
    if not sim.has_trait(trait_freshchef):
        sim.add_trait(trait_freshchef)

    trait_genderoptions_attractedto_female = instance_manager.get(get_resource_key(TRAIT_GENDEROPTIONS_ATTRACTEDTO_FEMALE, Types.TRAIT))
    if not sim.has_trait(trait_genderoptions_attractedto_female):
        sim.add_trait(trait_genderoptions_attractedto_female)

    trait_genderoptions_attractedto_male = instance_manager.get(get_resource_key(TRAIT_GENDEROPTIONS_ATTRACTEDTO_MALE, Types.TRAIT))
    if not sim.has_trait(trait_genderoptions_attractedto_male):
        sim.add_trait(trait_genderoptions_attractedto_male)

    trait_genderoptions_clothing_womenswear = instance_manager.get(get_resource_key(TRAIT_GENDEROPTIONS_CLOTHING_WOMENSWEAR, Types.TRAIT))
    if not sim.has_trait(trait_genderoptions_clothing_womenswear):
        sim.add_trait(trait_genderoptions_clothing_womenswear)

    trait_genderoptions_frame_feminine = instance_manager.get(get_resource_key(TRAIT_GENDEROPTIONS_FRAME_FEMININE, Types.TRAIT))
    if not sim.has_trait(trait_genderoptions_frame_feminine):
        sim.add_trait(trait_genderoptions_frame_feminine)

    trait_genderoptions_frame_masculine = instance_manager.get(get_resource_key(TRAIT_GENDEROPTIONS_FRAME_MASCULINE, Types.TRAIT))
    if sim.has_trait(trait_genderoptions_frame_masculine):
        sim.remove_trait(trait_genderoptions_frame_masculine)

    trait_genderoptions_pregnancy_canbeimpregnated = instance_manager.get(get_resource_key(TRAIT_GENDEROPTIONS_PREGNANCY_CANBEIMPREGNATED, Types.TRAIT))
    if not sim.has_trait(trait_genderoptions_pregnancy_canbeimpregnated):
        sim.add_trait(trait_genderoptions_pregnancy_canbeimpregnated)

    trait_genderoptions_pregnancy_cannotimpregnate = instance_manager.get(get_resource_key(TRAIT_GENDEROPTIONS_PREGNANCY_CANNOTIMPREGNATE, Types.TRAIT))
    if not sim.has_trait(trait_genderoptions_pregnancy_cannotimpregnate):
        sim.add_trait(trait_genderoptions_pregnancy_cannotimpregnate)

    trait_gloomy = instance_manager.get(get_resource_key(TRAIT_GLOOMY, Types.TRAIT))
    if sim.has_trait(trait_gloomy):
        sim.remove_trait(trait_gloomy)

    trait_greatkisser = instance_manager.get(get_resource_key(TRAIT_GREATKISSER, Types.TRAIT))
    if not sim.has_trait(trait_greatkisser):
        sim.add_trait(trait_greatkisser)

    trait_hsexit_earnedged = instance_manager.get(get_resource_key(TRAIT_HSEXIT_EARNEDGED, Types.TRAIT))
    if not sim.has_trait(trait_hsexit_earnedged):
        sim.add_trait(trait_hsexit_earnedged)

    trait_incrediblyfriendly = instance_manager.get(get_resource_key(TRAIT_INCREDIBLYFRIENDLY, Types.TRAIT))
    if not sim.has_trait(trait_incrediblyfriendly):
        sim.add_trait(trait_incrediblyfriendly)

    trait_isnanny = instance_manager.get(get_resource_key(TRAIT_ISNANNY, Types.TRAIT))
    if not sim.has_trait(trait_isnanny):
        sim.add_trait(trait_isnanny)

    trait_jealous = instance_manager.get(get_resource_key(TRAIT_JEALOUS, Types.TRAIT))
    if sim.has_trait(trait_jealous):
        sim.remove_trait(trait_jealous)

    trait_kleptomaniac = instance_manager.get(get_resource_key(TRAIT_KLEPTOMANIAC, Types.TRAIT))
    if sim.has_trait(trait_kleptomaniac):
        sim.remove_trait(trait_kleptomaniac)

    trait_legendary = instance_manager.get(get_resource_key(TRAIT_LEGENDARY, Types.TRAIT))
    if not sim.has_trait(trait_legendary):
        sim.add_trait(trait_legendary)

    trait_mentor = instance_manager.get(get_resource_key(TRAIT_MENTOR, Types.TRAIT))
    if not sim.has_trait(trait_mentor):
        sim.add_trait(trait_mentor)

    trait_neat = instance_manager.get(get_resource_key(TRAIT_NEAT, Types.TRAIT))
    if not sim.has_trait(trait_neat):
        sim.add_trait(trait_neat)

    trait_player = instance_manager.get(get_resource_key(TRAIT_PLAYER, Types.TRAIT))
    if not sim.has_trait(trait_player):
        sim.add_trait(trait_player)

    trait_proper = instance_manager.get(get_resource_key(TRAIT_PROPER, Types.TRAIT))
    if not sim.has_trait(trait_proper):
        sim.add_trait(trait_proper)

    trait_shameless = instance_manager.get(get_resource_key(TRAIT_SHAMELESS, Types.TRAIT))
    if not sim.has_trait(trait_shameless):
        sim.add_trait(trait_shameless)

    trait_sicknessimmunity = instance_manager.get(get_resource_key(TRAIT_SICKNESSIMMUNITY, Types.TRAIT))
    if not sim.has_trait(trait_sicknessimmunity):
        sim.add_trait(trait_sicknessimmunity)

    trait_superparent_rolemodel = instance_manager.get(get_resource_key(TRAIT_SUPERPARENT_ROLEMODEL, Types.TRAIT))
    if not sim.has_trait(trait_superparent_rolemodel):
        sim.add_trait(trait_superparent_rolemodel)

    trait_university_fineartdegreebahonors = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_FINEARTDEGREEBAHONORS, Types.TRAIT))
    if not sim.has_trait(trait_university_fineartdegreebahonors):
        sim.add_trait(trait_university_fineartdegreebahonors)

    trait_university_highereducation = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_HIGHEREDUCATION, Types.TRAIT))
    if not sim.has_trait(trait_university_highereducation):
        sim.add_trait(trait_university_highereducation)

    trait_university_languageandliteraturedegreebahonors = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_LANGUAGEANDLITERATUREDEGREEBAHONORS, Types.TRAIT))
    if not sim.has_trait(trait_university_languageandliteraturedegreebahonors):
        sim.add_trait(trait_university_languageandliteraturedegreebahonors)

    trait_university_psychologydegreebshonors = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_PSYCHOLOGYDEGREEBSHONORS, Types.TRAIT))
    if not sim.has_trait(trait_university_psychologydegreebshonors):
        sim.add_trait(trait_university_psychologydegreebshonors)

    trait_walkstylefeminine = instance_manager.get(get_resource_key(TRAIT_WALKSTYLEFEMININE, Types.TRAIT))
    if not sim.has_trait(trait_walkstylefeminine):
        sim.add_trait(trait_walkstylefeminine)

    wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_breastslarge = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_BODYSHAPE_BREASTSLARGE, Types.TRAIT))
    if not sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_breastslarge):
        sim.add_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_breastslarge)

    wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_buttlarge = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_BODYSHAPE_BUTTLARGE, Types.TRAIT))
    if not sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_buttlarge):
        sim.add_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_buttlarge)

    wickedwhims_attractiveness_trait_simpreference_dislikes_facialhair_beard = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_FACIALHAIR_BEARD, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_facialhair_beard):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_facialhair_beard)

    wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_black = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_HAIRCOLOR_BLACK, Types.TRAIT))
    if not sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_black):
        sim.add_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_black)

    wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_heavy = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_BODYSHAPE_HEAVY, Types.TRAIT))
    if not sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_heavy):
        sim.add_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_heavy)

    wickedwhims_attractiveness_trait_simpreference_likes_detail_body_hair = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_DETAIL_BODY_HAIR, Types.TRAIT))
    if not sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_body_hair):
        sim.add_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_body_hair)

    wickedwhims_attractiveness_trait_simpreference_likes_facialhair_beard = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_FACIALHAIR_BEARD, Types.TRAIT))
    if not sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_facialhair_beard):
        sim.add_trait(wickedwhims_attractiveness_trait_simpreference_likes_facialhair_beard)

    wickedwhims_trait_relationships_poly = instance_manager.get(get_resource_key(WICKEDWHIMS_TRAIT_RELATIONSHIPS_POLY, Types.TRAIT))
    if not sim.has_trait(wickedwhims_trait_relationships_poly):
        sim.add_trait(wickedwhims_trait_relationships_poly)

    wickedwhims_trait_relationships_sexcheater = instance_manager.get(get_resource_key(WICKEDWHIMS_TRAIT_RELATIONSHIPS_SEXCHEATER, Types.TRAIT))
    if not sim.has_trait(wickedwhims_trait_relationships_sexcheater):
        sim.add_trait(wickedwhims_trait_relationships_sexcheater)

    wickedwhims_trait_sex_attribute_generouslover = instance_manager.get(get_resource_key(WICKEDWHIMS_TRAIT_SEX_ATTRIBUTE_GENEROUSLOVER, Types.TRAIT))
    if not sim.has_trait(wickedwhims_trait_sex_attribute_generouslover):
        sim.add_trait(wickedwhims_trait_sex_attribute_generouslover)

    wickedwhims_trait_sex_cuckold = instance_manager.get(get_resource_key(WICKEDWHIMS_TRAIT_SEX_CUCKOLD, Types.TRAIT))
    if not sim.has_trait(wickedwhims_trait_sex_cuckold):
        sim.add_trait(wickedwhims_trait_sex_cuckold)

    wickedwhims_trait_sex_sexuallyalluring = instance_manager.get(get_resource_key(WICKEDWHIMS_TRAIT_SEX_SEXUALLYALLURING, Types.TRAIT))
    if not sim.has_trait(wickedwhims_trait_sex_sexuallyalluring):
        sim.add_trait(wickedwhims_trait_sex_sexuallyalluring)


@sims4.commands.Command('pbs_othersim', command_type=sims4.commands.CommandType.Live)
def pbs_othersim(_connection=None):
    # Get the console output
    output = sims4.commands.CheatOutput(_connection)

    # Get the sim_info for the active sim
    sim = services.client_manager().get(_connection).active_sim.sim_info

    # Get the tuned trait instance from the tuning instance manager
    instance_manager = services.get_instance_manager(Types.TRAIT)

    # Remove or add traits from all sims

    archaeologyskill_giveauthenticationmail_prohibit = instance_manager.get(get_resource_key(ARCHAEOLOGYSKILL_GIVEAUTHENTICATIONMAIL_PROHIBIT, Types.TRAIT))
    if not sim.has_trait(archaeologyskill_giveauthenticationmail_prohibit):
        sim.add_trait(archaeologyskill_giveauthenticationmail_prohibit)

    fametraits_celebritywalk_on = instance_manager.get(get_resource_key(FAMETRAITS_CELEBRITYWALK_ON, Types.TRAIT))
    if sim.has_trait(fametraits_celebritywalk_on):
        sim.remove_trait(fametraits_celebritywalk_on)

    fametraits_shine_off = instance_manager.get(get_resource_key(FAMETRAITS_SHINE_OFF, Types.TRAIT))
    if not sim.has_trait(fametraits_shine_off):
        sim.add_trait(fametraits_shine_off)

    fametraits_shine_on_rank4 = instance_manager.get(get_resource_key(FAMETRAITS_SHINE_ON_RANK4, Types.TRAIT))
    if sim.has_trait(fametraits_shine_on_rank4):
        sim.remove_trait(fametraits_shine_on_rank4)

    fametraits_shine_on_rank5 = instance_manager.get(get_resource_key(FAMETRAITS_SHINE_ON_RANK5, Types.TRAIT))
    if sim.has_trait(fametraits_shine_on_rank5):
        sim.remove_trait(fametraits_shine_on_rank5)

    trait_computerglasses_wearing = instance_manager.get(get_resource_key(TRAIT_COMPUTERGLASSES_WEARING, Types.TRAIT))
    if sim.has_trait(trait_computerglasses_wearing):
        sim.remove_trait(trait_computerglasses_wearing)

    trait_computerglasses_wearing_blue = instance_manager.get(get_resource_key(TRAIT_COMPUTERGLASSES_WEARING_BLUE, Types.TRAIT))
    if sim.has_trait(trait_computerglasses_wearing_blue):
        sim.remove_trait(trait_computerglasses_wearing_blue)

    trait_computerglasses_wearing_green = instance_manager.get(get_resource_key(TRAIT_COMPUTERGLASSES_WEARING_GREEN, Types.TRAIT))
    if sim.has_trait(trait_computerglasses_wearing_green):
        sim.remove_trait(trait_computerglasses_wearing_green)

    trait_computerglasses_wearing_orange = instance_manager.get(get_resource_key(TRAIT_COMPUTERGLASSES_WEARING_ORANGE, Types.TRAIT))
    if sim.has_trait(trait_computerglasses_wearing_orange):
        sim.remove_trait(trait_computerglasses_wearing_orange)

    trait_computerglasses_wearing_pink = instance_manager.get(get_resource_key(TRAIT_COMPUTERGLASSES_WEARING_PINK, Types.TRAIT))
    if sim.has_trait(trait_computerglasses_wearing_pink):
        sim.remove_trait(trait_computerglasses_wearing_pink)

    trait_computerglasses_wearing_red = instance_manager.get(get_resource_key(TRAIT_COMPUTERGLASSES_WEARING_RED, Types.TRAIT))
    if sim.has_trait(trait_computerglasses_wearing_red):
        sim.remove_trait(trait_computerglasses_wearing_red)

    trait_computerglasses_wearing_yellow = instance_manager.get(get_resource_key(TRAIT_COMPUTERGLASSES_WEARING_YELLOW, Types.TRAIT))
    if sim.has_trait(trait_computerglasses_wearing_yellow):
        sim.remove_trait(trait_computerglasses_wearing_yellow)

    trait_crystalhelmet_alabaster = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_ALABASTER, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_alabaster):
        sim.remove_trait(trait_crystalhelmet_alabaster)

    trait_crystalhelmet_alexandrite_ep = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_ALEXANDRITE_EP, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_alexandrite_ep):
        sim.remove_trait(trait_crystalhelmet_alexandrite_ep)

    trait_crystalhelmet_amazonite_ep = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_AMAZONITE_EP, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_amazonite_ep):
        sim.remove_trait(trait_crystalhelmet_amazonite_ep)

    trait_crystalhelmet_amethyst = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_AMETHYST, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_amethyst):
        sim.remove_trait(trait_crystalhelmet_amethyst)

    trait_crystalhelmet_citrine = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_CITRINE, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_citrine):
        sim.remove_trait(trait_crystalhelmet_citrine)

    trait_crystalhelmet_crandestine_ep = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_CRANDESTINE_EP, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_crandestine_ep):
        sim.remove_trait(trait_crystalhelmet_crandestine_ep)

    trait_crystalhelmet_diamond = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_DIAMOND, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_diamond):
        sim.remove_trait(trait_crystalhelmet_diamond)

    trait_crystalhelmet_emerald = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_EMERALD, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_emerald):
        sim.remove_trait(trait_crystalhelmet_emerald)

    trait_crystalhelmet_fireopal = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_FIREOPAL, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_fireopal):
        sim.remove_trait(trait_crystalhelmet_fireopal)

    trait_crystalhelmet_hematite = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_HEMATITE, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_hematite):
        sim.remove_trait(trait_crystalhelmet_hematite)

    trait_crystalhelmet_jet = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_JET, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_jet):
        sim.remove_trait(trait_crystalhelmet_jet)

    trait_crystalhelmet_jonquilyst = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_JONQUILYST, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_jonquilyst):
        sim.remove_trait(trait_crystalhelmet_jonquilyst)

    trait_crystalhelmet_nitelite_ep = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_NITELITE_EP, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_nitelite_ep):
        sim.remove_trait(trait_crystalhelmet_nitelite_ep)

    trait_crystalhelmet_orangetopaz = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_ORANGETOPAZ, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_orangetopaz):
        sim.remove_trait(trait_crystalhelmet_orangetopaz)

    trait_crystalhelmet_peach = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_PEACH, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_peach):
        sim.remove_trait(trait_crystalhelmet_peach)

    trait_crystalhelmet_plumbite = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_PLUMBITE, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_plumbite):
        sim.remove_trait(trait_crystalhelmet_plumbite)

    trait_crystalhelmet_quartz = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_QUARTZ, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_quartz):
        sim.remove_trait(trait_crystalhelmet_quartz)

    trait_crystalhelmet_rainborz = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_RAINBORZ, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_rainborz):
        sim.remove_trait(trait_crystalhelmet_rainborz)

    trait_crystalhelmet_rose = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_ROSE, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_rose):
        sim.remove_trait(trait_crystalhelmet_rose)

    trait_crystalhelmet_ruby = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_RUBY, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_ruby):
        sim.remove_trait(trait_crystalhelmet_ruby)

    trait_crystalhelmet_sapphire = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_SAPPHIRE, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_sapphire):
        sim.remove_trait(trait_crystalhelmet_sapphire)

    trait_crystalhelmet_shinalite = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_SHINALITE, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_shinalite):
        sim.remove_trait(trait_crystalhelmet_shinalite)

    trait_crystalhelmet_simanite = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_SIMANITE, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_simanite):
        sim.remove_trait(trait_crystalhelmet_simanite)

    trait_crystalhelmet_turquoise = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_TURQUOISE, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_turquoise):
        sim.remove_trait(trait_crystalhelmet_turquoise)

    trait_doctor_sicknessresistant = instance_manager.get(get_resource_key(TRAIT_DOCTOR_SICKNESSRESISTANT, Types.TRAIT))
    if not sim.has_trait(trait_doctor_sicknessresistant):
        sim.add_trait(trait_doctor_sicknessresistant)

    trait_essenceofflavor = instance_manager.get(get_resource_key(TRAIT_ESSENCEOFFLAVOR, Types.TRAIT))
    if not sim.has_trait(trait_essenceofflavor):
        sim.add_trait(trait_essenceofflavor)

    trait_fear_beingcheatedon = instance_manager.get(get_resource_key(TRAIT_FEAR_BEINGCHEATEDON, Types.TRAIT))
    if sim.has_trait(trait_fear_beingcheatedon):
        sim.remove_trait(trait_fear_beingcheatedon)

    trait_fear_beingjudged = instance_manager.get(get_resource_key(TRAIT_FEAR_BEINGJUDGED, Types.TRAIT))
    if sim.has_trait(trait_fear_beingjudged):
        sim.remove_trait(trait_fear_beingjudged)

    trait_fear_cowplant = instance_manager.get(get_resource_key(TRAIT_FEAR_COWPLANT, Types.TRAIT))
    if sim.has_trait(trait_fear_cowplant):
        sim.remove_trait(trait_fear_cowplant)

    trait_fear_crowdedplaces = instance_manager.get(get_resource_key(TRAIT_FEAR_CROWDEDPLACES, Types.TRAIT))
    if sim.has_trait(trait_fear_crowdedplaces):
        sim.remove_trait(trait_fear_crowdedplaces)

    trait_fear_dark = instance_manager.get(get_resource_key(TRAIT_FEAR_DARK, Types.TRAIT))
    if sim.has_trait(trait_fear_dark):
        sim.remove_trait(trait_fear_dark)

    trait_fear_deadendjob = instance_manager.get(get_resource_key(TRAIT_FEAR_DEADENDJOB, Types.TRAIT))
    if sim.has_trait(trait_fear_deadendjob):
        sim.remove_trait(trait_fear_deadendjob)

    trait_fear_death = instance_manager.get(get_resource_key(TRAIT_FEAR_DEATH, Types.TRAIT))
    if sim.has_trait(trait_fear_death):
        sim.remove_trait(trait_fear_death)

    trait_fear_disappointingparents = instance_manager.get(get_resource_key(TRAIT_FEAR_DISAPPOINTINGPARENTS, Types.TRAIT))
    if sim.has_trait(trait_fear_disappointingparents):
        sim.remove_trait(trait_fear_disappointingparents)

    trait_fear_disappointingparents_parentdeceasedflag = instance_manager.get(get_resource_key(TRAIT_FEAR_DISAPPOINTINGPARENTS_PARENTDECEASEDFLAG, Types.TRAIT))
    if sim.has_trait(trait_fear_disappointingparents_parentdeceasedflag):
        sim.remove_trait(trait_fear_disappointingparents_parentdeceasedflag)

    trait_fear_failing_afterschoolactivities = instance_manager.get(get_resource_key(TRAIT_FEAR_FAILING_AFTERSCHOOLACTIVITIES, Types.TRAIT))
    if sim.has_trait(trait_fear_failing_afterschoolactivities):
        sim.remove_trait(trait_fear_failing_afterschoolactivities)

    trait_fear_failing_class = instance_manager.get(get_resource_key(TRAIT_FEAR_FAILING_CLASS, Types.TRAIT))
    if sim.has_trait(trait_fear_failing_class):
        sim.remove_trait(trait_fear_failing_class)

    trait_fear_failing_tests = instance_manager.get(get_resource_key(TRAIT_FEAR_FAILING_TESTS, Types.TRAIT))
    if sim.has_trait(trait_fear_failing_tests):
        sim.remove_trait(trait_fear_failing_tests)

    trait_fear_failure = instance_manager.get(get_resource_key(TRAIT_FEAR_FAILURE, Types.TRAIT))
    if sim.has_trait(trait_fear_failure):
        sim.remove_trait(trait_fear_failure)

    trait_fear_fire = instance_manager.get(get_resource_key(TRAIT_FEAR_FIRE, Types.TRAIT))
    if sim.has_trait(trait_fear_fire):
        sim.remove_trait(trait_fear_fire)

    trait_fear_ghosts = instance_manager.get(get_resource_key(TRAIT_FEAR_GHOSTS, Types.TRAIT))
    if sim.has_trait(trait_fear_ghosts):
        sim.remove_trait(trait_fear_ghosts)

    trait_fear_homework = instance_manager.get(get_resource_key(TRAIT_FEAR_HOMEWORK, Types.TRAIT))
    if sim.has_trait(trait_fear_homework):
        sim.remove_trait(trait_fear_homework)

    trait_fear_swimming = instance_manager.get(get_resource_key(TRAIT_FEAR_SWIMMING, Types.TRAIT))
    if sim.has_trait(trait_fear_swimming):
        sim.remove_trait(trait_fear_swimming)

    trait_fear_unfulfilled = instance_manager.get(get_resource_key(TRAIT_FEAR_UNFULFILLED, Types.TRAIT))
    if sim.has_trait(trait_fear_unfulfilled):
        sim.remove_trait(trait_fear_unfulfilled)

    trait_filthdweller = instance_manager.get(get_resource_key(TRAIT_FILTHDWELLER, Types.TRAIT))
    if sim.has_trait(trait_filthdweller):
        sim.remove_trait(trait_filthdweller)

    trait_freeservices = instance_manager.get(get_resource_key(TRAIT_FREESERVICES, Types.TRAIT))
    if not sim.has_trait(trait_freeservices):
        sim.add_trait(trait_freeservices)

    trait_frugal = instance_manager.get(get_resource_key(TRAIT_FRUGAL, Types.TRAIT))
    if not sim.has_trait(trait_frugal):
        sim.add_trait(trait_frugal)

    trait_genderoptions_attractedto_notfemale = instance_manager.get(get_resource_key(TRAIT_GENDEROPTIONS_ATTRACTEDTO_NOTFEMALE, Types.TRAIT))
    if sim.has_trait(trait_genderoptions_attractedto_notfemale):
        sim.remove_trait(trait_genderoptions_attractedto_notfemale)

    trait_genderoptions_attractedto_notmale = instance_manager.get(get_resource_key(TRAIT_GENDEROPTIONS_ATTRACTEDTO_NOTMALE, Types.TRAIT))
    if sim.has_trait(trait_genderoptions_attractedto_notmale):
        sim.remove_trait(trait_genderoptions_attractedto_notmale)

    trait_genderoptions_sexuality_exploring = instance_manager.get(get_resource_key(TRAIT_GENDEROPTIONS_SEXUALITY_EXPLORING, Types.TRAIT))
    if not sim.has_trait(trait_genderoptions_sexuality_exploring):
        sim.add_trait(trait_genderoptions_sexuality_exploring)

    trait_genderoptions_sexuality_notexploring = instance_manager.get(get_resource_key(TRAIT_GENDEROPTIONS_SEXUALITY_NOTEXPLORING, Types.TRAIT))
    if sim.has_trait(trait_genderoptions_sexuality_notexploring):
        sim.remove_trait(trait_genderoptions_sexuality_notexploring)

    trait_glutton = instance_manager.get(get_resource_key(TRAIT_GLUTTON, Types.TRAIT))
    if sim.has_trait(trait_glutton):
        sim.remove_trait(trait_glutton)

    trait_gradeschool_a = instance_manager.get(get_resource_key(TRAIT_GRADESCHOOL_A, Types.TRAIT))
    if not sim.has_trait(trait_gradeschool_a):
        sim.add_trait(trait_gradeschool_a)

    trait_gradeschool_b = instance_manager.get(get_resource_key(TRAIT_GRADESCHOOL_B, Types.TRAIT))
    if sim.has_trait(trait_gradeschool_b):
        sim.remove_trait(trait_gradeschool_b)

    trait_gradeschool_c = instance_manager.get(get_resource_key(TRAIT_GRADESCHOOL_C, Types.TRAIT))
    if sim.has_trait(trait_gradeschool_c):
        sim.remove_trait(trait_gradeschool_c)

    trait_gradeschool_d = instance_manager.get(get_resource_key(TRAIT_GRADESCHOOL_D, Types.TRAIT))
    if sim.has_trait(trait_gradeschool_d):
        sim.remove_trait(trait_gradeschool_d)

    trait_gradeschool_f = instance_manager.get(get_resource_key(TRAIT_GRADESCHOOL_F, Types.TRAIT))
    if sim.has_trait(trait_gradeschool_f):
        sim.remove_trait(trait_gradeschool_f)

    trait_highschool_a = instance_manager.get(get_resource_key(TRAIT_HIGHSCHOOL_A, Types.TRAIT))
    if not sim.has_trait(trait_highschool_a):
        sim.add_trait(trait_highschool_a)

    trait_highschool_b = instance_manager.get(get_resource_key(TRAIT_HIGHSCHOOL_B, Types.TRAIT))
    if sim.has_trait(trait_highschool_b):
        sim.remove_trait(trait_highschool_b)

    trait_highschool_c = instance_manager.get(get_resource_key(TRAIT_HIGHSCHOOL_C, Types.TRAIT))
    if sim.has_trait(trait_highschool_c):
        sim.remove_trait(trait_highschool_c)

    trait_highschool_d = instance_manager.get(get_resource_key(TRAIT_HIGHSCHOOL_D, Types.TRAIT))
    if sim.has_trait(trait_highschool_d):
        sim.remove_trait(trait_highschool_d)

    trait_highschool_f = instance_manager.get(get_resource_key(TRAIT_HIGHSCHOOL_F, Types.TRAIT))
    if sim.has_trait(trait_highschool_f):
        sim.remove_trait(trait_highschool_f)

    trait_hotheaded = instance_manager.get(get_resource_key(TRAIT_HOTHEADED, Types.TRAIT))
    if sim.has_trait(trait_hotheaded):
        sim.remove_trait(trait_hotheaded)

    trait_hsexit_expelled = instance_manager.get(get_resource_key(TRAIT_HSEXIT_EXPELLED, Types.TRAIT))
    if sim.has_trait(trait_hsexit_expelled):
        sim.remove_trait(trait_hsexit_expelled)

    trait_insane = instance_manager.get(get_resource_key(TRAIT_INSANE, Types.TRAIT))
    if sim.has_trait(trait_insane):
        sim.remove_trait(trait_insane)

    trait_invested = instance_manager.get(get_resource_key(TRAIT_INVESTED, Types.TRAIT))
    if not sim.has_trait(trait_invested):
        sim.add_trait(trait_invested)

    trait_ispregnant = instance_manager.get(get_resource_key(TRAIT_ISPREGNANT, Types.TRAIT))
    if sim.has_trait(trait_ispregnant):
        sim.remove_trait(trait_ispregnant)

    trait_mechanicalsuit_hoverengaged = instance_manager.get(get_resource_key(TRAIT_MECHANICALSUIT_HOVERENGAGED, Types.TRAIT))
    if sim.has_trait(trait_mechanicalsuit_hoverengaged):
        sim.remove_trait(trait_mechanicalsuit_hoverengaged)

    trait_mechanicalsuit_wearing_body_beigewhite = instance_manager.get(get_resource_key(TRAIT_MECHANICALSUIT_WEARING_BODY_BEIGEWHITE, Types.TRAIT))
    if sim.has_trait(trait_mechanicalsuit_wearing_body_beigewhite):
        sim.remove_trait(trait_mechanicalsuit_wearing_body_beigewhite)

    trait_mechanicalsuit_wearing_body_blackblue = instance_manager.get(get_resource_key(TRAIT_MECHANICALSUIT_WEARING_BODY_BLACKBLUE, Types.TRAIT))
    if sim.has_trait(trait_mechanicalsuit_wearing_body_blackblue):
        sim.remove_trait(trait_mechanicalsuit_wearing_body_blackblue)

    trait_mechanicalsuit_wearing_body_bluered = instance_manager.get(get_resource_key(TRAIT_MECHANICALSUIT_WEARING_BODY_BLUERED, Types.TRAIT))
    if sim.has_trait(trait_mechanicalsuit_wearing_body_bluered):
        sim.remove_trait(trait_mechanicalsuit_wearing_body_bluered)

    trait_mechanicalsuit_wearing_body_graybrown = instance_manager.get(get_resource_key(TRAIT_MECHANICALSUIT_WEARING_BODY_GRAYBROWN, Types.TRAIT))
    if sim.has_trait(trait_mechanicalsuit_wearing_body_graybrown):
        sim.remove_trait(trait_mechanicalsuit_wearing_body_graybrown)

    trait_mechanicalsuit_wearing_body_greenbrown = instance_manager.get(get_resource_key(TRAIT_MECHANICALSUIT_WEARING_BODY_GREENBROWN, Types.TRAIT))
    if sim.has_trait(trait_mechanicalsuit_wearing_body_greenbrown):
        sim.remove_trait(trait_mechanicalsuit_wearing_body_greenbrown)

    trait_mechanicalsuit_wearing_body_redgreen = instance_manager.get(get_resource_key(TRAIT_MECHANICALSUIT_WEARING_BODY_REDGREEN, Types.TRAIT))
    if sim.has_trait(trait_mechanicalsuit_wearing_body_redgreen):
        sim.remove_trait(trait_mechanicalsuit_wearing_body_redgreen)

    trait_mechanicalsuit_wearing_body_whitecopper = instance_manager.get(get_resource_key(TRAIT_MECHANICALSUIT_WEARING_BODY_WHITECOPPER, Types.TRAIT))
    if sim.has_trait(trait_mechanicalsuit_wearing_body_whitecopper):
        sim.remove_trait(trait_mechanicalsuit_wearing_body_whitecopper)

    trait_mechanicalsuit_wearing_helmet_blackblue = instance_manager.get(get_resource_key(TRAIT_MECHANICALSUIT_WEARING_HELMET_BLACKBLUE, Types.TRAIT))
    if sim.has_trait(trait_mechanicalsuit_wearing_helmet_blackblue):
        sim.remove_trait(trait_mechanicalsuit_wearing_helmet_blackblue)

    trait_mechanicalsuit_wearing_helmet_blackcopper = instance_manager.get(get_resource_key(TRAIT_MECHANICALSUIT_WEARING_HELMET_BLACKCOPPER, Types.TRAIT))
    if sim.has_trait(trait_mechanicalsuit_wearing_helmet_blackcopper):
        sim.remove_trait(trait_mechanicalsuit_wearing_helmet_blackcopper)

    trait_mechanicalsuit_wearing_helmet_blackgold = instance_manager.get(get_resource_key(TRAIT_MECHANICALSUIT_WEARING_HELMET_BLACKGOLD, Types.TRAIT))
    if sim.has_trait(trait_mechanicalsuit_wearing_helmet_blackgold):
        sim.remove_trait(trait_mechanicalsuit_wearing_helmet_blackgold)

    trait_mechanicalsuit_wearing_helmet_blackgray = instance_manager.get(get_resource_key(TRAIT_MECHANICALSUIT_WEARING_HELMET_BLACKGRAY, Types.TRAIT))
    if sim.has_trait(trait_mechanicalsuit_wearing_helmet_blackgray):
        sim.remove_trait(trait_mechanicalsuit_wearing_helmet_blackgray)

    trait_mechanicalsuit_wearing_helmet_bluegray = instance_manager.get(get_resource_key(TRAIT_MECHANICALSUIT_WEARING_HELMET_BLUEGRAY, Types.TRAIT))
    if sim.has_trait(trait_mechanicalsuit_wearing_helmet_bluegray):
        sim.remove_trait(trait_mechanicalsuit_wearing_helmet_bluegray)

    trait_mechanicalsuit_wearing_helmet_grayblack = instance_manager.get(get_resource_key(TRAIT_MECHANICALSUIT_WEARING_HELMET_GRAYBLACK, Types.TRAIT))
    if sim.has_trait(trait_mechanicalsuit_wearing_helmet_grayblack):
        sim.remove_trait(trait_mechanicalsuit_wearing_helmet_grayblack)

    trait_mechanicalsuit_wearing_helmet_greenblack = instance_manager.get(get_resource_key(TRAIT_MECHANICALSUIT_WEARING_HELMET_GREENBLACK, Types.TRAIT))
    if sim.has_trait(trait_mechanicalsuit_wearing_helmet_greenblack):
        sim.remove_trait(trait_mechanicalsuit_wearing_helmet_greenblack)

    trait_nightowl_crystalhelmet = instance_manager.get(get_resource_key(TRAIT_NIGHTOWL_CRYSTALHELMET, Types.TRAIT))
    if sim.has_trait(trait_nightowl_crystalhelmet):
        sim.remove_trait(trait_nightowl_crystalhelmet)

    trait_roboticsarm_wearing_beigewhite = instance_manager.get(get_resource_key(TRAIT_ROBOTICSARM_WEARING_BEIGEWHITE, Types.TRAIT))
    if sim.has_trait(trait_roboticsarm_wearing_beigewhite):
        sim.remove_trait(trait_roboticsarm_wearing_beigewhite)

    trait_roboticsarm_wearing_blackblue = instance_manager.get(get_resource_key(TRAIT_ROBOTICSARM_WEARING_BLACKBLUE, Types.TRAIT))
    if sim.has_trait(trait_roboticsarm_wearing_blackblue):
        sim.remove_trait(trait_roboticsarm_wearing_blackblue)

    trait_roboticsarm_wearing_bluered = instance_manager.get(get_resource_key(TRAIT_ROBOTICSARM_WEARING_BLUERED, Types.TRAIT))
    if sim.has_trait(trait_roboticsarm_wearing_bluered):
        sim.remove_trait(trait_roboticsarm_wearing_bluered)

    trait_roboticsarm_wearing_graybrown = instance_manager.get(get_resource_key(TRAIT_ROBOTICSARM_WEARING_GRAYBROWN, Types.TRAIT))
    if sim.has_trait(trait_roboticsarm_wearing_graybrown):
        sim.remove_trait(trait_roboticsarm_wearing_graybrown)

    trait_roboticsarm_wearing_greenbrown = instance_manager.get(get_resource_key(TRAIT_ROBOTICSARM_WEARING_GREENBROWN, Types.TRAIT))
    if sim.has_trait(trait_roboticsarm_wearing_greenbrown):
        sim.remove_trait(trait_roboticsarm_wearing_greenbrown)

    trait_roboticsarm_wearing_redgreen = instance_manager.get(get_resource_key(TRAIT_ROBOTICSARM_WEARING_REDGREEN, Types.TRAIT))
    if sim.has_trait(trait_roboticsarm_wearing_redgreen):
        sim.remove_trait(trait_roboticsarm_wearing_redgreen)

    trait_roboticsarm_wearing_whitecopper = instance_manager.get(get_resource_key(TRAIT_ROBOTICSARM_WEARING_WHITECOPPER, Types.TRAIT))
    if sim.has_trait(trait_roboticsarm_wearing_whitecopper):
        sim.remove_trait(trait_roboticsarm_wearing_whitecopper)

    trait_selfassured = instance_manager.get(get_resource_key(TRAIT_SELFASSURED, Types.TRAIT))
    if not sim.has_trait(trait_selfassured):
        sim.add_trait(trait_selfassured)

    trait_sexualorientation_woohoointerests_female = instance_manager.get(get_resource_key(TRAIT_SEXUALORIENTATION_WOOHOOINTERESTS_FEMALE, Types.TRAIT))
    if not sim.has_trait(trait_sexualorientation_woohoointerests_female):
        sim.add_trait(trait_sexualorientation_woohoointerests_female)

    trait_sexualorientation_woohoointerests_male = instance_manager.get(get_resource_key(TRAIT_SEXUALORIENTATION_WOOHOOINTERESTS_MALE, Types.TRAIT))
    if not sim.has_trait(trait_sexualorientation_woohoointerests_male):
        sim.add_trait(trait_sexualorientation_woohoointerests_male)

    trait_sexualorientation_woohoointerests_notfemale = instance_manager.get(get_resource_key(TRAIT_SEXUALORIENTATION_WOOHOOINTERESTS_NOTFEMALE, Types.TRAIT))
    if sim.has_trait(trait_sexualorientation_woohoointerests_notfemale):
        sim.remove_trait(trait_sexualorientation_woohoointerests_notfemale)

    trait_simpreference_dislikes_activities_djmixing = instance_manager.get(get_resource_key(TRAIT_SIMPREFERENCE_DISLIKES_ACTIVITIES_DJMIXING, Types.TRAIT))
    if sim.has_trait(trait_simpreference_dislikes_activities_djmixing):
        sim.remove_trait(trait_simpreference_dislikes_activities_djmixing)

    trait_simpreference_dislikes_activities_fitness = instance_manager.get(get_resource_key(TRAIT_SIMPREFERENCE_DISLIKES_ACTIVITIES_FITNESS, Types.TRAIT))
    if sim.has_trait(trait_simpreference_dislikes_activities_fitness):
        sim.remove_trait(trait_simpreference_dislikes_activities_fitness)

    trait_simpreference_dislikes_activities_guitar = instance_manager.get(get_resource_key(TRAIT_SIMPREFERENCE_DISLIKES_ACTIVITIES_GUITAR, Types.TRAIT))
    if sim.has_trait(trait_simpreference_dislikes_activities_guitar):
        sim.remove_trait(trait_simpreference_dislikes_activities_guitar)

    trait_simpreference_dislikes_activities_piano = instance_manager.get(get_resource_key(TRAIT_SIMPREFERENCE_DISLIKES_ACTIVITIES_PIANO, Types.TRAIT))
    if sim.has_trait(trait_simpreference_dislikes_activities_piano):
        sim.remove_trait(trait_simpreference_dislikes_activities_piano)

    trait_simpreference_dislikes_activities_pipeorgan = instance_manager.get(get_resource_key(TRAIT_SIMPREFERENCE_DISLIKES_ACTIVITIES_PIPEORGAN, Types.TRAIT))
    if sim.has_trait(trait_simpreference_dislikes_activities_pipeorgan):
        sim.remove_trait(trait_simpreference_dislikes_activities_pipeorgan)

    trait_simpreference_dislikes_activities_programming = instance_manager.get(get_resource_key(TRAIT_SIMPREFERENCE_DISLIKES_ACTIVITIES_PROGRAMMING, Types.TRAIT))
    if sim.has_trait(trait_simpreference_dislikes_activities_programming):
        sim.remove_trait(trait_simpreference_dislikes_activities_programming)

    trait_simpreference_dislikes_activities_rockclimbing = instance_manager.get(get_resource_key(TRAIT_SIMPREFERENCE_DISLIKES_ACTIVITIES_ROCKCLIMBING, Types.TRAIT))
    if sim.has_trait(trait_simpreference_dislikes_activities_rockclimbing):
        sim.remove_trait(trait_simpreference_dislikes_activities_rockclimbing)

    trait_simpreference_dislikes_activities_singing = instance_manager.get(get_resource_key(TRAIT_SIMPREFERENCE_DISLIKES_ACTIVITIES_SINGING, Types.TRAIT))
    if sim.has_trait(trait_simpreference_dislikes_activities_singing):
        sim.remove_trait(trait_simpreference_dislikes_activities_singing)

    trait_simpreference_dislikes_activities_violin = instance_manager.get(get_resource_key(TRAIT_SIMPREFERENCE_DISLIKES_ACTIVITIES_VIOLIN, Types.TRAIT))
    if sim.has_trait(trait_simpreference_dislikes_activities_violin):
        sim.remove_trait(trait_simpreference_dislikes_activities_violin)

    trait_simpreference_dislikes_activities_wellness = instance_manager.get(get_resource_key(TRAIT_SIMPREFERENCE_DISLIKES_ACTIVITIES_WELLNESS, Types.TRAIT))
    if sim.has_trait(trait_simpreference_dislikes_activities_wellness):
        sim.remove_trait(trait_simpreference_dislikes_activities_wellness)

    trait_simpreference_dislikes_activities_writing = instance_manager.get(get_resource_key(TRAIT_SIMPREFERENCE_DISLIKES_ACTIVITIES_WRITING, Types.TRAIT))
    if sim.has_trait(trait_simpreference_dislikes_activities_writing):
        sim.remove_trait(trait_simpreference_dislikes_activities_writing)

    trait_simpreference_likes_activities_fitness = instance_manager.get(get_resource_key(TRAIT_SIMPREFERENCE_LIKES_ACTIVITIES_FITNESS, Types.TRAIT))
    if not sim.has_trait(trait_simpreference_likes_activities_fitness):
        sim.add_trait(trait_simpreference_likes_activities_fitness)

    trait_simpreference_likes_activities_wellness = instance_manager.get(get_resource_key(TRAIT_SIMPREFERENCE_LIKES_ACTIVITIES_WELLNESS, Types.TRAIT))
    if not sim.has_trait(trait_simpreference_likes_activities_wellness):
        sim.add_trait(trait_simpreference_likes_activities_wellness)

    trait_simpreference_noopinion_activities_fitness = instance_manager.get(get_resource_key(TRAIT_SIMPREFERENCE_NOOPINION_ACTIVITIES_FITNESS, Types.TRAIT))
    if sim.has_trait(trait_simpreference_noopinion_activities_fitness):
        sim.remove_trait(trait_simpreference_noopinion_activities_fitness)

    trait_simpreference_noopinion_activities_wellness = instance_manager.get(get_resource_key(TRAIT_SIMPREFERENCE_NOOPINION_ACTIVITIES_WELLNESS, Types.TRAIT))
    if sim.has_trait(trait_simpreference_noopinion_activities_wellness):
        sim.remove_trait(trait_simpreference_noopinion_activities_wellness)

    trait_slob = instance_manager.get(get_resource_key(TRAIT_SLOB, Types.TRAIT))
    if sim.has_trait(trait_slob):
        sim.remove_trait(trait_slob)

    trait_speedcleaner = instance_manager.get(get_resource_key(TRAIT_SPEEDCLEANER, Types.TRAIT))
    if not sim.has_trait(trait_speedcleaner):
        sim.add_trait(trait_speedcleaner)

    trait_speedreader = instance_manager.get(get_resource_key(TRAIT_SPEEDREADER, Types.TRAIT))
    if not sim.has_trait(trait_speedreader):
        sim.add_trait(trait_speedreader)

    trait_stormchaser = instance_manager.get(get_resource_key(TRAIT_STORMCHASER, Types.TRAIT))
    if not sim.has_trait(trait_stormchaser):
        sim.add_trait(trait_stormchaser)

    trait_temperature_burningman = instance_manager.get(get_resource_key(TRAIT_TEMPERATURE_BURNINGMAN, Types.TRAIT))
    if not sim.has_trait(trait_temperature_burningman):
        sim.add_trait(trait_temperature_burningman)

    trait_temperature_coldacclimation = instance_manager.get(get_resource_key(TRAIT_TEMPERATURE_COLDACCLIMATION, Types.TRAIT))
    if sim.has_trait(trait_temperature_coldacclimation):
        sim.remove_trait(trait_temperature_coldacclimation)

    trait_temperature_heatacclimation = instance_manager.get(get_resource_key(TRAIT_TEMPERATURE_HEATACCLIMATION, Types.TRAIT))
    if sim.has_trait(trait_temperature_heatacclimation):
        sim.remove_trait(trait_temperature_heatacclimation)

    trait_temperature_iceman = instance_manager.get(get_resource_key(TRAIT_TEMPERATURE_ICEMAN, Types.TRAIT))
    if not sim.has_trait(trait_temperature_iceman):
        sim.add_trait(trait_temperature_iceman)

    trait_theknack = instance_manager.get(get_resource_key(TRAIT_THEKNACK, Types.TRAIT))
    if not sim.has_trait(trait_theknack):
        sim.add_trait(trait_theknack)

    trait_university_arthistorydegreeba = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_ARTHISTORYDEGREEBA, Types.TRAIT))
    if sim.has_trait(trait_university_arthistorydegreeba):
        sim.remove_trait(trait_university_arthistorydegreeba)

    trait_university_arthistorydegreebs = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_ARTHISTORYDEGREEBS, Types.TRAIT))
    if sim.has_trait(trait_university_arthistorydegreebs):
        sim.remove_trait(trait_university_arthistorydegreebs)

    trait_university_biologydegreeba = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_BIOLOGYDEGREEBA, Types.TRAIT))
    if sim.has_trait(trait_university_biologydegreeba):
        sim.remove_trait(trait_university_biologydegreeba)

    trait_university_biologydegreebs = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_BIOLOGYDEGREEBS, Types.TRAIT))
    if sim.has_trait(trait_university_biologydegreebs):
        sim.remove_trait(trait_university_biologydegreebs)

    trait_university_communicationsdegreeba = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_COMMUNICATIONSDEGREEBA, Types.TRAIT))
    if sim.has_trait(trait_university_communicationsdegreeba):
        sim.remove_trait(trait_university_communicationsdegreeba)

    trait_university_communicationsdegreebs = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_COMMUNICATIONSDEGREEBS, Types.TRAIT))
    if sim.has_trait(trait_university_communicationsdegreebs):
        sim.remove_trait(trait_university_communicationsdegreebs)

    trait_university_computersciencedegreeba = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_COMPUTERSCIENCEDEGREEBA, Types.TRAIT))
    if sim.has_trait(trait_university_computersciencedegreeba):
        sim.remove_trait(trait_university_computersciencedegreeba)

    trait_university_computersciencedegreebs = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_COMPUTERSCIENCEDEGREEBS, Types.TRAIT))
    if sim.has_trait(trait_university_computersciencedegreebs):
        sim.remove_trait(trait_university_computersciencedegreebs)

    trait_university_culinaryartsdegreeba = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_CULINARYARTSDEGREEBA, Types.TRAIT))
    if sim.has_trait(trait_university_culinaryartsdegreeba):
        sim.remove_trait(trait_university_culinaryartsdegreeba)

    trait_university_culinaryartsdegreebs = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_CULINARYARTSDEGREEBS, Types.TRAIT))
    if sim.has_trait(trait_university_culinaryartsdegreebs):
        sim.remove_trait(trait_university_culinaryartsdegreebs)

    trait_university_dramadegreeba = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_DRAMADEGREEBA, Types.TRAIT))
    if sim.has_trait(trait_university_dramadegreeba):
        sim.remove_trait(trait_university_dramadegreeba)

    trait_university_dramadegreebs = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_DRAMADEGREEBS, Types.TRAIT))
    if sim.has_trait(trait_university_dramadegreebs):
        sim.remove_trait(trait_university_dramadegreebs)

    trait_university_economicsdegreeba = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_ECONOMICSDEGREEBA, Types.TRAIT))
    if sim.has_trait(trait_university_economicsdegreeba):
        sim.remove_trait(trait_university_economicsdegreeba)

    trait_university_economicsdegreebs = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_ECONOMICSDEGREEBS, Types.TRAIT))
    if sim.has_trait(trait_university_economicsdegreebs):
        sim.remove_trait(trait_university_economicsdegreebs)

    trait_university_fineartdegreeba = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_FINEARTDEGREEBA, Types.TRAIT))
    if sim.has_trait(trait_university_fineartdegreeba):
        sim.remove_trait(trait_university_fineartdegreeba)

    trait_university_fineartdegreebs = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_FINEARTDEGREEBS, Types.TRAIT))
    if sim.has_trait(trait_university_fineartdegreebs):
        sim.remove_trait(trait_university_fineartdegreebs)

    trait_university_historydegreeba = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_HISTORYDEGREEBA, Types.TRAIT))
    if sim.has_trait(trait_university_historydegreeba):
        sim.remove_trait(trait_university_historydegreeba)

    trait_university_historydegreebs = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_HISTORYDEGREEBS, Types.TRAIT))
    if sim.has_trait(trait_university_historydegreebs):
        sim.remove_trait(trait_university_historydegreebs)

    trait_university_languageandliteraturedegreeba = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_LANGUAGEANDLITERATUREDEGREEBA, Types.TRAIT))
    if sim.has_trait(trait_university_languageandliteraturedegreeba):
        sim.remove_trait(trait_university_languageandliteraturedegreeba)

    trait_university_languageandliteraturedegreebs = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_LANGUAGEANDLITERATUREDEGREEBS, Types.TRAIT))
    if sim.has_trait(trait_university_languageandliteraturedegreebs):
        sim.remove_trait(trait_university_languageandliteraturedegreebs)

    trait_university_physicsdegreeba = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_PHYSICSDEGREEBA, Types.TRAIT))
    if sim.has_trait(trait_university_physicsdegreeba):
        sim.remove_trait(trait_university_physicsdegreeba)

    trait_university_physicsdegreebs = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_PHYSICSDEGREEBS, Types.TRAIT))
    if sim.has_trait(trait_university_physicsdegreebs):
        sim.remove_trait(trait_university_physicsdegreebs)

    trait_university_psychologydegreeba = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_PSYCHOLOGYDEGREEBA, Types.TRAIT))
    if sim.has_trait(trait_university_psychologydegreeba):
        sim.remove_trait(trait_university_psychologydegreeba)

    trait_university_psychologydegreebs = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_PSYCHOLOGYDEGREEBS, Types.TRAIT))
    if sim.has_trait(trait_university_psychologydegreebs):
        sim.remove_trait(trait_university_psychologydegreebs)

    trait_university_villainydegreeba = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_VILLAINYDEGREEBA, Types.TRAIT))
    if sim.has_trait(trait_university_villainydegreeba):
        sim.remove_trait(trait_university_villainydegreeba)

    trait_university_villainydegreebs = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_VILLAINYDEGREEBS, Types.TRAIT))
    if sim.has_trait(trait_university_villainydegreebs):
        sim.remove_trait(trait_university_villainydegreebs)

    trait_walkstylecreepy = instance_manager.get(get_resource_key(TRAIT_WALKSTYLECREEPY, Types.TRAIT))
    if sim.has_trait(trait_walkstylecreepy):
        sim.remove_trait(trait_walkstylecreepy)

    trait_walkstyleenergetic = instance_manager.get(get_resource_key(TRAIT_WALKSTYLEENERGETIC, Types.TRAIT))
    if sim.has_trait(trait_walkstyleenergetic):
        sim.remove_trait(trait_walkstyleenergetic)

    trait_walkstyleenergetic = instance_manager.get(get_resource_key(TRAIT_WALKSTYLEENERGETIC, Types.TRAIT))
    if sim.has_trait(trait_walkstyleenergetic):
        sim.remove_trait(trait_walkstyleenergetic)

    trait_walkstylefeminine = instance_manager.get(get_resource_key(TRAIT_WALKSTYLEFEMININE, Types.TRAIT))
    if sim.has_trait(trait_walkstylefeminine):
        sim.remove_trait(trait_walkstylefeminine)

    trait_walkstylegoofy = instance_manager.get(get_resource_key(TRAIT_WALKSTYLEGOOFY, Types.TRAIT))
    if sim.has_trait(trait_walkstylegoofy):
        sim.remove_trait(trait_walkstylegoofy)

    trait_walkstyleperky = instance_manager.get(get_resource_key(TRAIT_WALKSTYLEPERKY, Types.TRAIT))
    if sim.has_trait(trait_walkstyleperky):
        sim.remove_trait(trait_walkstyleperky)

    trait_walkstylesleepy = instance_manager.get(get_resource_key(TRAIT_WALKSTYLESLEEPY, Types.TRAIT))
    if sim.has_trait(trait_walkstylesleepy):
        sim.remove_trait(trait_walkstylesleepy)

    trait_walkstylesnooty = instance_manager.get(get_resource_key(TRAIT_WALKSTYLESNOOTY, Types.TRAIT))
    if sim.has_trait(trait_walkstylesnooty):
        sim.remove_trait(trait_walkstylesnooty)

    trait_walkstyleswagger = instance_manager.get(get_resource_key(TRAIT_WALKSTYLESWAGGER, Types.TRAIT))
    if sim.has_trait(trait_walkstyleswagger):
        sim.remove_trait(trait_walkstyleswagger)

    trait_walkstyletough = instance_manager.get(get_resource_key(TRAIT_WALKSTYLETOUGH, Types.TRAIT))
    if sim.has_trait(trait_walkstyletough):
        sim.remove_trait(trait_walkstyletough)

    trait_waterproof = instance_manager.get(get_resource_key(TRAIT_WATERPROOF, Types.TRAIT))
    if not sim.has_trait(trait_waterproof):
        sim.add_trait(trait_waterproof)

    trait_webmaster = instance_manager.get(get_resource_key(TRAIT_WEBMASTER, Types.TRAIT))
    if not sim.has_trait(trait_webmaster):
        sim.add_trait(trait_webmaster)

    wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_breastslarge = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_BODYSHAPE_BREASTSLARGE, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_breastslarge):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_breastslarge)

    wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_breastssmall = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_BODYSHAPE_BREASTSSMALL, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_breastssmall):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_breastssmall)

    wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_buttlarge = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_BODYSHAPE_BUTTLARGE, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_buttlarge):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_buttlarge)

    wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_buttsmall = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_BODYSHAPE_BUTTSMALL, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_buttsmall):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_buttsmall)

    wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_heavy = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_BODYSHAPE_HEAVY, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_heavy):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_heavy)

    wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_high = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_BODYSHAPE_HIGH, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_high):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_high)

    wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_light = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_BODYSHAPE_LIGHT, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_light):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_light)

    wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_low = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_BODYSHAPE_LOW, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_low):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_low)

    wickedwhims_attractiveness_trait_simpreference_dislikes_detail_body_hair = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_DETAIL_BODY_HAIR, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_detail_body_hair):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_detail_body_hair)

    wickedwhims_attractiveness_trait_simpreference_dislikes_detail_freckles = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_DETAIL_FRECKLES, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_detail_freckles):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_detail_freckles)

    wickedwhims_attractiveness_trait_simpreference_dislikes_detail_glasses = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_DETAIL_GLASSES, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_detail_glasses):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_detail_glasses)

    wickedwhims_attractiveness_trait_simpreference_dislikes_detail_hats = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_DETAIL_HATS, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_detail_hats):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_detail_hats)

    wickedwhims_attractiveness_trait_simpreference_dislikes_detail_jewelery = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_DETAIL_JEWELERY, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_detail_jewelery):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_detail_jewelery)

    wickedwhims_attractiveness_trait_simpreference_dislikes_detail_makeup = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_DETAIL_MAKEUP, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_detail_makeup):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_detail_makeup)

    wickedwhims_attractiveness_trait_simpreference_dislikes_detail_piercing = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_DETAIL_PIERCING, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_detail_piercing):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_detail_piercing)

    wickedwhims_attractiveness_trait_simpreference_dislikes_detail_tattoos = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_DETAIL_TATTOOS, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_detail_tattoos):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_detail_tattoos)

    wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_blue = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_EYECOLOR_BLUE, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_blue):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_blue)

    wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_blue = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_EYECOLOR_BLUE, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_blue):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_blue)

    wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_brown = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_EYECOLOR_BROWN, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_brown):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_brown)

    wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_brown = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_EYECOLOR_BROWN, Types.TRAIT))
    if not sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_brown):
        sim.add_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_brown)

    wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_green = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_EYECOLOR_GREEN, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_green):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_green)

    wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_green = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_EYECOLOR_GREEN, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_green):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_green)

    wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_unnatural = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_EYECOLOR_UNNATURAL, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_unnatural):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_unnatural)

    wickedwhims_attractiveness_trait_simpreference_dislikes_facialhair_beard = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_FACIALHAIR_BEARD, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_facialhair_beard):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_facialhair_beard)

    wickedwhims_attractiveness_trait_simpreference_dislikes_facialhair_clean = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_FACIALHAIR_CLEAN, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_facialhair_clean):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_facialhair_clean)

    wickedwhims_attractiveness_trait_simpreference_dislikes_facialhair_goatee = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_FACIALHAIR_GOATEE, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_facialhair_goatee):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_facialhair_goatee)

    wickedwhims_attractiveness_trait_simpreference_dislikes_facialhair_mustache = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_FACIALHAIR_MUSTACHE, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_facialhair_mustache):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_facialhair_mustache)

    wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_black = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_HAIRCOLOR_BLACK, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_black):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_black)

    wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_blonde = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_HAIRCOLOR_BLONDE, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_blonde):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_blonde)

    wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_blonde = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_HAIRCOLOR_BLONDE, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_blonde):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_blonde)

    wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_blue = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_HAIRCOLOR_BLUE, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_blue):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_blue)

    wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_blue = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_HAIRCOLOR_BLUE, Types.TRAIT))
    if not sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_blue):
        sim.add_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_blue)

    wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_brown = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_HAIRCOLOR_BROWN, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_brown):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_brown)

    wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_brown = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_HAIRCOLOR_BROWN, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_brown):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_brown)

    wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_gray = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_HAIRCOLOR_GRAY, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_gray):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_gray)

    wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_green = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_HAIRCOLOR_GREEN, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_green):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_green)

    wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_green = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_HAIRCOLOR_GREEN, Types.TRAIT))
    if not sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_green):
        sim.add_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_green)

    wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_pink = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_HAIRCOLOR_PINK, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_pink):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_pink)

    wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_red = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_HAIRCOLOR_RED, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_red):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_red)

    wickedwhims_attractiveness_trait_simpreference_dislikes_hairlength_bald = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_HAIRLENGTH_BALD, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_hairlength_bald):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_hairlength_bald)

    wickedwhims_attractiveness_trait_simpreference_dislikes_hairlength_bald = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_HAIRLENGTH_BALD, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_hairlength_bald):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_hairlength_bald)

    wickedwhims_attractiveness_trait_simpreference_dislikes_hairlength_long = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_HAIRLENGTH_LONG, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_hairlength_long):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_hairlength_long)

    wickedwhims_attractiveness_trait_simpreference_dislikes_hairlength_medium = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_HAIRLENGTH_MEDIUM, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_hairlength_medium):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_hairlength_medium)

    wickedwhims_attractiveness_trait_simpreference_dislikes_hairlength_short = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_HAIRLENGTH_SHORT, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_hairlength_short):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_hairlength_short)

    wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_breastslarge = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_BODYSHAPE_BREASTSLARGE, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_breastslarge):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_breastslarge)

    wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_breastssmall = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_BODYSHAPE_BREASTSSMALL, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_breastssmall):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_breastssmall)

    wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_breastssmall = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_BODYSHAPE_BREASTSSMALL, Types.TRAIT))
    if not sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_breastssmall):
        sim.add_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_breastssmall)

    wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_buttlarge = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_BODYSHAPE_BUTTLARGE, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_buttlarge):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_buttlarge)

    wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_buttlarge = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_BODYSHAPE_BUTTLARGE, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_buttlarge):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_buttlarge)

    wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_buttsmall = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_BODYSHAPE_BUTTSMALL, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_buttsmall):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_buttsmall)

    wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_buttsmall = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_BODYSHAPE_BUTTSMALL, Types.TRAIT))
    if not sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_buttsmall):
        sim.add_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_buttsmall)

    wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_heavy = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_BODYSHAPE_HEAVY, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_heavy):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_heavy)

    wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_high = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_BODYSHAPE_HIGH, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_high):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_high)

    wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_light = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_BODYSHAPE_LIGHT, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_light):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_light)

    wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_low = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_BODYSHAPE_LOW, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_low):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_low)

    wickedwhims_attractiveness_trait_simpreference_likes_detail_body_hair = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_DETAIL_BODY_HAIR, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_body_hair):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_body_hair)

    wickedwhims_attractiveness_trait_simpreference_likes_detail_freckles = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_DETAIL_FRECKLES, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_freckles):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_freckles)

    wickedwhims_attractiveness_trait_simpreference_likes_detail_glasses = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_DETAIL_GLASSES, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_glasses):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_glasses)

    wickedwhims_attractiveness_trait_simpreference_likes_detail_glasses = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_DETAIL_GLASSES, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_glasses):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_glasses)

    wickedwhims_attractiveness_trait_simpreference_likes_detail_hats = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_DETAIL_HATS, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_hats):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_hats)

    wickedwhims_attractiveness_trait_simpreference_likes_detail_hats = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_DETAIL_HATS, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_hats):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_hats)

    wickedwhims_attractiveness_trait_simpreference_likes_detail_jewelery = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_DETAIL_JEWELERY, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_jewelery):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_jewelery)

    wickedwhims_attractiveness_trait_simpreference_likes_detail_makeup = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_DETAIL_MAKEUP, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_makeup):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_makeup)

    wickedwhims_attractiveness_trait_simpreference_likes_detail_piercing = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_DETAIL_PIERCING, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_piercing):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_piercing)

    wickedwhims_attractiveness_trait_simpreference_likes_detail_tattoos = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_DETAIL_TATTOOS, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_tattoos):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_tattoos)

    wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_blue = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_EYECOLOR_BLUE, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_blue):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_blue)

    wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_blue = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_EYECOLOR_BLUE, Types.TRAIT))
    if not sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_blue):
        sim.add_trait(wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_blue)

    wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_brown = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_EYECOLOR_BROWN, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_brown):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_brown)

    wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_brown = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_EYECOLOR_BROWN, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_brown):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_brown)

    wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_green = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_EYECOLOR_GREEN, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_green):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_green)

    wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_green = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_EYECOLOR_GREEN, Types.TRAIT))
    if not sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_green):
        sim.add_trait(wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_green)

    wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_unnatural = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_EYECOLOR_UNNATURAL, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_unnatural):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_unnatural)

    wickedwhims_attractiveness_trait_simpreference_likes_facialhair_beard = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_FACIALHAIR_BEARD, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_facialhair_beard):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_facialhair_beard)

    wickedwhims_attractiveness_trait_simpreference_likes_facialhair_clean = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_FACIALHAIR_CLEAN, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_facialhair_clean):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_facialhair_clean)

    wickedwhims_attractiveness_trait_simpreference_likes_facialhair_goatee = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_FACIALHAIR_GOATEE, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_facialhair_goatee):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_facialhair_goatee)

    wickedwhims_attractiveness_trait_simpreference_likes_facialhair_mustache = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_FACIALHAIR_MUSTACHE, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_facialhair_mustache):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_facialhair_mustache)

    wickedwhims_attractiveness_trait_simpreference_likes_haircolor_black = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_HAIRCOLOR_BLACK, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_black):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_black)

    wickedwhims_attractiveness_trait_simpreference_likes_haircolor_blonde = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_HAIRCOLOR_BLONDE, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_blonde):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_blonde)

    wickedwhims_attractiveness_trait_simpreference_likes_haircolor_blonde = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_HAIRCOLOR_BLONDE, Types.TRAIT))
    if not sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_blonde):
        sim.add_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_blonde)

    wickedwhims_attractiveness_trait_simpreference_likes_haircolor_blue = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_HAIRCOLOR_BLUE, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_blue):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_blue)

    wickedwhims_attractiveness_trait_simpreference_likes_haircolor_brown = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_HAIRCOLOR_BROWN, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_brown):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_brown)

    wickedwhims_attractiveness_trait_simpreference_likes_haircolor_brown = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_HAIRCOLOR_BROWN, Types.TRAIT))
    if not sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_brown):
        sim.add_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_brown)

    wickedwhims_attractiveness_trait_simpreference_likes_haircolor_gray = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_HAIRCOLOR_GRAY, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_gray):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_gray)

    wickedwhims_attractiveness_trait_simpreference_likes_haircolor_green = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_HAIRCOLOR_GREEN, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_green):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_green)

    wickedwhims_attractiveness_trait_simpreference_likes_haircolor_pink = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_HAIRCOLOR_PINK, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_pink):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_pink)

    wickedwhims_attractiveness_trait_simpreference_likes_haircolor_red = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_HAIRCOLOR_RED, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_red):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_red)

    wickedwhims_attractiveness_trait_simpreference_likes_hairlength_bald = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_HAIRLENGTH_BALD, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_hairlength_bald):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_hairlength_bald)

    wickedwhims_attractiveness_trait_simpreference_likes_hairlength_long = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_HAIRLENGTH_LONG, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_hairlength_long):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_hairlength_long)

    wickedwhims_attractiveness_trait_simpreference_likes_hairlength_medium = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_HAIRLENGTH_MEDIUM, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_hairlength_medium):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_hairlength_medium)

    wickedwhims_attractiveness_trait_simpreference_likes_hairlength_short = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_HAIRLENGTH_SHORT, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_hairlength_short):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_hairlength_short)

    wickedwhims_trait_attractivenessblacklist = instance_manager.get(get_resource_key(WICKEDWHIMS_TRAIT_ATTRACTIVENESSBLACKLIST, Types.TRAIT))
    if sim.has_trait(wickedwhims_trait_attractivenessblacklist):
        sim.remove_trait(wickedwhims_trait_attractivenessblacklist)

    wickedwhims_trait_bodyhair_pubichair_isdisabled = instance_manager.get(get_resource_key(WICKEDWHIMS_TRAIT_BODYHAIR_PUBICHAIR_ISDISABLED, Types.TRAIT))
    if not sim.has_trait(wickedwhims_trait_bodyhair_pubichair_isdisabled):
        sim.add_trait(wickedwhims_trait_bodyhair_pubichair_isdisabled)

    wickedwhims_trait_bodyhair_pubichair_isgrowthdisabled = instance_manager.get(get_resource_key(WICKEDWHIMS_TRAIT_BODYHAIR_PUBICHAIR_ISGROWTHDISABLED, Types.TRAIT))
    if not sim.has_trait(wickedwhims_trait_bodyhair_pubichair_isgrowthdisabled):
        sim.add_trait(wickedwhims_trait_bodyhair_pubichair_isgrowthdisabled)

    wickedwhims_trait_cumslut = instance_manager.get(get_resource_key(WICKEDWHIMS_TRAIT_CUMSLUT, Types.TRAIT))
    if not sim.has_trait(wickedwhims_trait_cumslut):
        sim.add_trait(wickedwhims_trait_cumslut)

    wickedwhims_trait_improved_absorbency = instance_manager.get(get_resource_key(WICKEDWHIMS_TRAIT_IMPROVED_ABSORBENCY, Types.TRAIT))
    if not sim.has_trait(wickedwhims_trait_improved_absorbency):
        sim.add_trait(wickedwhims_trait_improved_absorbency)

    wickedwhims_trait_postpubertyteen = instance_manager.get(get_resource_key(WICKEDWHIMS_TRAIT_POSTPUBERTYTEEN, Types.TRAIT))
    if not sim.has_trait(wickedwhims_trait_postpubertyteen):
        sim.add_trait(wickedwhims_trait_postpubertyteen)

    wickedwhims_trait_sex_attribute_badatsex = instance_manager.get(get_resource_key(WICKEDWHIMS_TRAIT_SEX_ATTRIBUTE_BADATSEX, Types.TRAIT))
    if sim.has_trait(wickedwhims_trait_sex_attribute_badatsex):
        sim.remove_trait(wickedwhims_trait_sex_attribute_badatsex)

    wickedwhims_trait_sex_sexuallyabstinent = instance_manager.get(get_resource_key(WICKEDWHIMS_TRAIT_SEX_SEXUALLYABSTINENT, Types.TRAIT))
    if sim.has_trait(wickedwhims_trait_sex_sexuallyabstinent):
        sim.remove_trait(wickedwhims_trait_sex_sexuallyabstinent)


    # Remove or add traits from other sim
    fametrait_level5 = instance_manager.get(get_resource_key(FAMETRAIT_LEVEL5, Types.TRAIT))
    if sim.has_trait(fametrait_level5):
        sim.remove_trait(fametrait_level5)

    trait_entrepreneur_theknowledge = instance_manager.get(get_resource_key(TRAIT_ENTREPRENEUR_THEKNOWLEDGE, Types.TRAIT))
    if not sim.has_trait(trait_entrepreneur_theknowledge):
        sim.add_trait(trait_entrepreneur_theknowledge)

    trait_hsexit_earnedged = instance_manager.get(get_resource_key(TRAIT_HSEXIT_EARNEDGED, Types.TRAIT))
    if not sim.has_trait(trait_hsexit_earnedged):
        sim.add_trait(trait_hsexit_earnedged)

    trait_quick_learner = instance_manager.get(get_resource_key(TRAIT_QUICK_LEARNER, Types.TRAIT))
    if not sim.has_trait(trait_quick_learner):
        sim.add_trait(trait_quick_learner)

    trait_genderfemale = instance_manager.get(get_resource_key(TRAIT_GENDERFEMALE, Types.TRAIT))
    trait_gendermale = instance_manager.get(get_resource_key(TRAIT_GENDERMALE, Types.TRAIT))
    # Add Female Traits
    if sim.has_trait(trait_genderfemale):
        trait_genderoptions_attractedto_male = instance_manager.get(get_resource_key(TRAIT_GENDEROPTIONS_ATTRACTEDTO_MALE, Types.TRAIT))
        if not sim.has_trait(trait_genderoptions_attractedto_male):
            sim.add_trait(trait_genderoptions_attractedto_male)

        trait_genderoptions_clothing_womenswear = instance_manager.get(get_resource_key(TRAIT_GENDEROPTIONS_CLOTHING_WOMENSWEAR, Types.TRAIT))
        if not sim.has_trait(trait_genderoptions_clothing_womenswear):
            sim.add_trait(trait_genderoptions_clothing_womenswear)

        trait_genderoptions_frame_feminine = instance_manager.get(get_resource_key(TRAIT_GENDEROPTIONS_FRAME_FEMININE, Types.TRAIT))
        if not sim.has_trait(trait_genderoptions_frame_feminine):
            sim.add_trait(trait_genderoptions_frame_feminine)

        trait_genderoptions_frame_masculine = instance_manager.get(get_resource_key(TRAIT_GENDEROPTIONS_FRAME_MASCULINE, Types.TRAIT))
        if sim.has_trait(trait_genderoptions_frame_masculine):
            sim.remove_trait(trait_genderoptions_frame_masculine)

        trait_genderoptions_pregnancy_canbeimpregnated = instance_manager.get(get_resource_key(TRAIT_GENDEROPTIONS_PREGNANCY_CANBEIMPREGNATED, Types.TRAIT))
        if not sim.has_trait(trait_genderoptions_pregnancy_canbeimpregnated):
            sim.add_trait(trait_genderoptions_pregnancy_canbeimpregnated)

        trait_genderoptions_pregnancy_cannotimpregnate = instance_manager.get(get_resource_key(TRAIT_GENDEROPTIONS_PREGNANCY_CANNOTIMPREGNATE, Types.TRAIT))
        if not sim.has_trait(trait_genderoptions_pregnancy_cannotimpregnate):
            sim.add_trait(trait_genderoptions_pregnancy_cannotimpregnate)

        trait_neat = instance_manager.get(get_resource_key(TRAIT_NEAT, Types.TRAIT))
        if not sim.has_trait(trait_neat):
            sim.add_trait(trait_neat)

        trait_phone_lightpink = instance_manager.get(get_resource_key(TRAIT_PHONE_LIGHTPINK, Types.TRAIT))
        if not sim.has_trait(trait_phone_lightpink):
            sim.add_trait(trait_phone_lightpink)

        trait_walkstylefeminine = instance_manager.get(get_resource_key(TRAIT_WALKSTYLEFEMININE, Types.TRAIT))
        if not sim.has_trait(trait_walkstylefeminine):
            sim.add_trait(trait_walkstylefeminine)

        wickedwhims_attractiveness_trait_simpreference_dislikes_facialhair_beard = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_FACIALHAIR_BEARD, Types.TRAIT))
        if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_facialhair_beard):
            sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_facialhair_beard)

        wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_heavy = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_BODYSHAPE_HEAVY, Types.TRAIT))
        if not sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_heavy):
            sim.add_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_heavy)

        wickedwhims_attractiveness_trait_simpreference_likes_detail_body_hair = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_DETAIL_BODY_HAIR, Types.TRAIT))
        if not sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_body_hair):
            sim.add_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_body_hair)

        wickedwhims_attractiveness_trait_simpreference_likes_facialhair_beard = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_FACIALHAIR_BEARD, Types.TRAIT))
        if not sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_facialhair_beard):
            sim.add_trait(wickedwhims_attractiveness_trait_simpreference_likes_facialhair_beard)

        wickedwhims_trait_sex_attribute_generouslover = instance_manager.get(get_resource_key(WICKEDWHIMS_TRAIT_SEX_ATTRIBUTE_GENEROUSLOVER, Types.TRAIT))
        if not sim.has_trait(wickedwhims_trait_sex_attribute_generouslover):
            sim.add_trait(wickedwhims_trait_sex_attribute_generouslover)

    # Add Male Traits
    if sim.has_trait(trait_gendermale):
        trait_genderoptions_attractedto_female = instance_manager.get(get_resource_key(TRAIT_GENDEROPTIONS_ATTRACTEDTO_FEMALE, Types.TRAIT))
        if not sim.has_trait(trait_genderoptions_attractedto_female):
            sim.add_trait(trait_genderoptions_attractedto_female)

        trait_genderoptions_clothing_menswear = instance_manager.get(get_resource_key(TRAIT_GENDEROPTIONS_CLOTHING_MENSWEAR, Types.TRAIT))
        if not sim.has_trait(trait_genderoptions_clothing_menswear):
            sim.add_trait(trait_genderoptions_clothing_menswear)

        trait_genderoptions_clothing_womenswear = instance_manager.get(get_resource_key(TRAIT_GENDEROPTIONS_CLOTHING_WOMENSWEAR, Types.TRAIT))
        if sim.has_trait(trait_genderoptions_clothing_womenswear):
            sim.remove_trait(trait_genderoptions_clothing_womenswear)

        trait_genderoptions_frame_feminine = instance_manager.get(get_resource_key(TRAIT_GENDEROPTIONS_FRAME_FEMININE, Types.TRAIT))
        if sim.has_trait(trait_genderoptions_frame_feminine):
            sim.remove_trait(trait_genderoptions_frame_feminine)

        trait_genderoptions_frame_masculine = instance_manager.get(get_resource_key(TRAIT_GENDEROPTIONS_FRAME_MASCULINE, Types.TRAIT))
        if not sim.has_trait(trait_genderoptions_frame_masculine):
            sim.add_trait(trait_genderoptions_frame_masculine)

        trait_genderoptions_pregnancy_canimpregnate = instance_manager.get(get_resource_key(TRAIT_GENDEROPTIONS_PREGNANCY_CANIMPREGNATE, Types.TRAIT))
        if not sim.has_trait(trait_genderoptions_pregnancy_canimpregnate):
            sim.add_trait(trait_genderoptions_pregnancy_canimpregnate)

        trait_genderoptions_pregnancy_cannot_beimpregnated = instance_manager.get(get_resource_key(TRAIT_GENDEROPTIONS_PREGNANCY_CANNOT_BEIMPREGNATED, Types.TRAIT))
        if not sim.has_trait(trait_genderoptions_pregnancy_cannot_beimpregnated):
            sim.add_trait(trait_genderoptions_pregnancy_cannot_beimpregnated)

        wickedwhims_attractiveness_trait_simpreference_dislikes_facialhair_beard = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_FACIALHAIR_BEARD, Types.TRAIT))
        if not sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_facialhair_beard):
            sim.add_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_facialhair_beard)

        wickedwhims_attractiveness_trait_simpreference_likes_detail_body_hair = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_DETAIL_BODY_HAIR, Types.TRAIT))
        if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_body_hair):
            sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_body_hair)


@sims4.commands.Command('pbs_ss', command_type=sims4.commands.CommandType.Live)
def pbs_ss(_connection=None):
    # Get the console output
    output = sims4.commands.CheatOutput(_connection)

    # Get the sim_info for the active sim
    sim = services.client_manager().get(_connection).active_sim.sim_info

    # Get the tuned trait instance from the tuning instance manager
    instance_manager = services.get_instance_manager(Types.TRAIT)

    # Remove or add traits from all sims
    archaeologyskill_giveauthenticationmail_prohibit = instance_manager.get(get_resource_key(ARCHAEOLOGYSKILL_GIVEAUTHENTICATIONMAIL_PROHIBIT, Types.TRAIT))
    if not sim.has_trait(archaeologyskill_giveauthenticationmail_prohibit):
        sim.add_trait(archaeologyskill_giveauthenticationmail_prohibit)

    fametraits_celebritywalk_on = instance_manager.get(get_resource_key(FAMETRAITS_CELEBRITYWALK_ON, Types.TRAIT))
    if sim.has_trait(fametraits_celebritywalk_on):
        sim.remove_trait(fametraits_celebritywalk_on)

    fametraits_shine_off = instance_manager.get(get_resource_key(FAMETRAITS_SHINE_OFF, Types.TRAIT))
    if not sim.has_trait(fametraits_shine_off):
        sim.add_trait(fametraits_shine_off)

    fametraits_shine_on_rank4 = instance_manager.get(get_resource_key(FAMETRAITS_SHINE_ON_RANK4, Types.TRAIT))
    if sim.has_trait(fametraits_shine_on_rank4):
        sim.remove_trait(fametraits_shine_on_rank4)

    fametraits_shine_on_rank5 = instance_manager.get(get_resource_key(FAMETRAITS_SHINE_ON_RANK5, Types.TRAIT))
    if sim.has_trait(fametraits_shine_on_rank5):
        sim.remove_trait(fametraits_shine_on_rank5)

    trait_computerglasses_wearing = instance_manager.get(get_resource_key(TRAIT_COMPUTERGLASSES_WEARING, Types.TRAIT))
    if sim.has_trait(trait_computerglasses_wearing):
        sim.remove_trait(trait_computerglasses_wearing)

    trait_computerglasses_wearing_blue = instance_manager.get(get_resource_key(TRAIT_COMPUTERGLASSES_WEARING_BLUE, Types.TRAIT))
    if sim.has_trait(trait_computerglasses_wearing_blue):
        sim.remove_trait(trait_computerglasses_wearing_blue)

    trait_computerglasses_wearing_green = instance_manager.get(get_resource_key(TRAIT_COMPUTERGLASSES_WEARING_GREEN, Types.TRAIT))
    if sim.has_trait(trait_computerglasses_wearing_green):
        sim.remove_trait(trait_computerglasses_wearing_green)

    trait_computerglasses_wearing_orange = instance_manager.get(get_resource_key(TRAIT_COMPUTERGLASSES_WEARING_ORANGE, Types.TRAIT))
    if sim.has_trait(trait_computerglasses_wearing_orange):
        sim.remove_trait(trait_computerglasses_wearing_orange)

    trait_computerglasses_wearing_pink = instance_manager.get(get_resource_key(TRAIT_COMPUTERGLASSES_WEARING_PINK, Types.TRAIT))
    if sim.has_trait(trait_computerglasses_wearing_pink):
        sim.remove_trait(trait_computerglasses_wearing_pink)

    trait_computerglasses_wearing_red = instance_manager.get(get_resource_key(TRAIT_COMPUTERGLASSES_WEARING_RED, Types.TRAIT))
    if sim.has_trait(trait_computerglasses_wearing_red):
        sim.remove_trait(trait_computerglasses_wearing_red)

    trait_computerglasses_wearing_yellow = instance_manager.get(get_resource_key(TRAIT_COMPUTERGLASSES_WEARING_YELLOW, Types.TRAIT))
    if sim.has_trait(trait_computerglasses_wearing_yellow):
        sim.remove_trait(trait_computerglasses_wearing_yellow)

    trait_crystalhelmet_alabaster = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_ALABASTER, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_alabaster):
        sim.remove_trait(trait_crystalhelmet_alabaster)

    trait_crystalhelmet_alexandrite_ep = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_ALEXANDRITE_EP, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_alexandrite_ep):
        sim.remove_trait(trait_crystalhelmet_alexandrite_ep)

    trait_crystalhelmet_amazonite_ep = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_AMAZONITE_EP, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_amazonite_ep):
        sim.remove_trait(trait_crystalhelmet_amazonite_ep)

    trait_crystalhelmet_amethyst = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_AMETHYST, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_amethyst):
        sim.remove_trait(trait_crystalhelmet_amethyst)

    trait_crystalhelmet_citrine = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_CITRINE, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_citrine):
        sim.remove_trait(trait_crystalhelmet_citrine)

    trait_crystalhelmet_crandestine_ep = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_CRANDESTINE_EP, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_crandestine_ep):
        sim.remove_trait(trait_crystalhelmet_crandestine_ep)

    trait_crystalhelmet_diamond = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_DIAMOND, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_diamond):
        sim.remove_trait(trait_crystalhelmet_diamond)

    trait_crystalhelmet_emerald = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_EMERALD, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_emerald):
        sim.remove_trait(trait_crystalhelmet_emerald)

    trait_crystalhelmet_fireopal = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_FIREOPAL, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_fireopal):
        sim.remove_trait(trait_crystalhelmet_fireopal)

    trait_crystalhelmet_hematite = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_HEMATITE, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_hematite):
        sim.remove_trait(trait_crystalhelmet_hematite)

    trait_crystalhelmet_jet = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_JET, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_jet):
        sim.remove_trait(trait_crystalhelmet_jet)

    trait_crystalhelmet_jonquilyst = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_JONQUILYST, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_jonquilyst):
        sim.remove_trait(trait_crystalhelmet_jonquilyst)

    trait_crystalhelmet_nitelite_ep = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_NITELITE_EP, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_nitelite_ep):
        sim.remove_trait(trait_crystalhelmet_nitelite_ep)

    trait_crystalhelmet_orangetopaz = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_ORANGETOPAZ, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_orangetopaz):
        sim.remove_trait(trait_crystalhelmet_orangetopaz)

    trait_crystalhelmet_peach = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_PEACH, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_peach):
        sim.remove_trait(trait_crystalhelmet_peach)

    trait_crystalhelmet_plumbite = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_PLUMBITE, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_plumbite):
        sim.remove_trait(trait_crystalhelmet_plumbite)

    trait_crystalhelmet_quartz = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_QUARTZ, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_quartz):
        sim.remove_trait(trait_crystalhelmet_quartz)

    trait_crystalhelmet_rainborz = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_RAINBORZ, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_rainborz):
        sim.remove_trait(trait_crystalhelmet_rainborz)

    trait_crystalhelmet_rose = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_ROSE, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_rose):
        sim.remove_trait(trait_crystalhelmet_rose)

    trait_crystalhelmet_ruby = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_RUBY, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_ruby):
        sim.remove_trait(trait_crystalhelmet_ruby)

    trait_crystalhelmet_sapphire = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_SAPPHIRE, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_sapphire):
        sim.remove_trait(trait_crystalhelmet_sapphire)

    trait_crystalhelmet_shinalite = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_SHINALITE, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_shinalite):
        sim.remove_trait(trait_crystalhelmet_shinalite)

    trait_crystalhelmet_simanite = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_SIMANITE, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_simanite):
        sim.remove_trait(trait_crystalhelmet_simanite)

    trait_crystalhelmet_turquoise = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_TURQUOISE, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_turquoise):
        sim.remove_trait(trait_crystalhelmet_turquoise)

    trait_doctor_sicknessresistant = instance_manager.get(get_resource_key(TRAIT_DOCTOR_SICKNESSRESISTANT, Types.TRAIT))
    if not sim.has_trait(trait_doctor_sicknessresistant):
        sim.add_trait(trait_doctor_sicknessresistant)

    trait_essenceofflavor = instance_manager.get(get_resource_key(TRAIT_ESSENCEOFFLAVOR, Types.TRAIT))
    if not sim.has_trait(trait_essenceofflavor):
        sim.add_trait(trait_essenceofflavor)

    trait_fear_beingcheatedon = instance_manager.get(get_resource_key(TRAIT_FEAR_BEINGCHEATEDON, Types.TRAIT))
    if sim.has_trait(trait_fear_beingcheatedon):
        sim.remove_trait(trait_fear_beingcheatedon)

    trait_fear_beingjudged = instance_manager.get(get_resource_key(TRAIT_FEAR_BEINGJUDGED, Types.TRAIT))
    if sim.has_trait(trait_fear_beingjudged):
        sim.remove_trait(trait_fear_beingjudged)

    trait_fear_cowplant = instance_manager.get(get_resource_key(TRAIT_FEAR_COWPLANT, Types.TRAIT))
    if sim.has_trait(trait_fear_cowplant):
        sim.remove_trait(trait_fear_cowplant)

    trait_fear_crowdedplaces = instance_manager.get(get_resource_key(TRAIT_FEAR_CROWDEDPLACES, Types.TRAIT))
    if sim.has_trait(trait_fear_crowdedplaces):
        sim.remove_trait(trait_fear_crowdedplaces)

    trait_fear_dark = instance_manager.get(get_resource_key(TRAIT_FEAR_DARK, Types.TRAIT))
    if sim.has_trait(trait_fear_dark):
        sim.remove_trait(trait_fear_dark)

    trait_fear_deadendjob = instance_manager.get(get_resource_key(TRAIT_FEAR_DEADENDJOB, Types.TRAIT))
    if sim.has_trait(trait_fear_deadendjob):
        sim.remove_trait(trait_fear_deadendjob)

    trait_fear_death = instance_manager.get(get_resource_key(TRAIT_FEAR_DEATH, Types.TRAIT))
    if sim.has_trait(trait_fear_death):
        sim.remove_trait(trait_fear_death)

    trait_fear_disappointingparents = instance_manager.get(get_resource_key(TRAIT_FEAR_DISAPPOINTINGPARENTS, Types.TRAIT))
    if sim.has_trait(trait_fear_disappointingparents):
        sim.remove_trait(trait_fear_disappointingparents)

    trait_fear_disappointingparents_parentdeceasedflag = instance_manager.get(get_resource_key(TRAIT_FEAR_DISAPPOINTINGPARENTS_PARENTDECEASEDFLAG, Types.TRAIT))
    if sim.has_trait(trait_fear_disappointingparents_parentdeceasedflag):
        sim.remove_trait(trait_fear_disappointingparents_parentdeceasedflag)

    trait_fear_failing_afterschoolactivities = instance_manager.get(get_resource_key(TRAIT_FEAR_FAILING_AFTERSCHOOLACTIVITIES, Types.TRAIT))
    if sim.has_trait(trait_fear_failing_afterschoolactivities):
        sim.remove_trait(trait_fear_failing_afterschoolactivities)

    trait_fear_failing_class = instance_manager.get(get_resource_key(TRAIT_FEAR_FAILING_CLASS, Types.TRAIT))
    if sim.has_trait(trait_fear_failing_class):
        sim.remove_trait(trait_fear_failing_class)

    trait_fear_failing_tests = instance_manager.get(get_resource_key(TRAIT_FEAR_FAILING_TESTS, Types.TRAIT))
    if sim.has_trait(trait_fear_failing_tests):
        sim.remove_trait(trait_fear_failing_tests)

    trait_fear_failure = instance_manager.get(get_resource_key(TRAIT_FEAR_FAILURE, Types.TRAIT))
    if sim.has_trait(trait_fear_failure):
        sim.remove_trait(trait_fear_failure)

    trait_fear_fire = instance_manager.get(get_resource_key(TRAIT_FEAR_FIRE, Types.TRAIT))
    if sim.has_trait(trait_fear_fire):
        sim.remove_trait(trait_fear_fire)

    trait_fear_ghosts = instance_manager.get(get_resource_key(TRAIT_FEAR_GHOSTS, Types.TRAIT))
    if sim.has_trait(trait_fear_ghosts):
        sim.remove_trait(trait_fear_ghosts)

    trait_fear_homework = instance_manager.get(get_resource_key(TRAIT_FEAR_HOMEWORK, Types.TRAIT))
    if sim.has_trait(trait_fear_homework):
        sim.remove_trait(trait_fear_homework)

    trait_fear_swimming = instance_manager.get(get_resource_key(TRAIT_FEAR_SWIMMING, Types.TRAIT))
    if sim.has_trait(trait_fear_swimming):
        sim.remove_trait(trait_fear_swimming)

    trait_fear_unfulfilled = instance_manager.get(get_resource_key(TRAIT_FEAR_UNFULFILLED, Types.TRAIT))
    if sim.has_trait(trait_fear_unfulfilled):
        sim.remove_trait(trait_fear_unfulfilled)

    trait_filthdweller = instance_manager.get(get_resource_key(TRAIT_FILTHDWELLER, Types.TRAIT))
    if sim.has_trait(trait_filthdweller):
        sim.remove_trait(trait_filthdweller)

    trait_freeservices = instance_manager.get(get_resource_key(TRAIT_FREESERVICES, Types.TRAIT))
    if not sim.has_trait(trait_freeservices):
        sim.add_trait(trait_freeservices)

    trait_frugal = instance_manager.get(get_resource_key(TRAIT_FRUGAL, Types.TRAIT))
    if not sim.has_trait(trait_frugal):
        sim.add_trait(trait_frugal)

    trait_genderoptions_attractedto_notfemale = instance_manager.get(get_resource_key(TRAIT_GENDEROPTIONS_ATTRACTEDTO_NOTFEMALE, Types.TRAIT))
    if sim.has_trait(trait_genderoptions_attractedto_notfemale):
        sim.remove_trait(trait_genderoptions_attractedto_notfemale)

    trait_genderoptions_attractedto_notmale = instance_manager.get(get_resource_key(TRAIT_GENDEROPTIONS_ATTRACTEDTO_NOTMALE, Types.TRAIT))
    if sim.has_trait(trait_genderoptions_attractedto_notmale):
        sim.remove_trait(trait_genderoptions_attractedto_notmale)

    trait_genderoptions_sexuality_exploring = instance_manager.get(get_resource_key(TRAIT_GENDEROPTIONS_SEXUALITY_EXPLORING, Types.TRAIT))
    if not sim.has_trait(trait_genderoptions_sexuality_exploring):
        sim.add_trait(trait_genderoptions_sexuality_exploring)

    trait_genderoptions_sexuality_notexploring = instance_manager.get(get_resource_key(TRAIT_GENDEROPTIONS_SEXUALITY_NOTEXPLORING, Types.TRAIT))
    if sim.has_trait(trait_genderoptions_sexuality_notexploring):
        sim.remove_trait(trait_genderoptions_sexuality_notexploring)

    trait_glutton = instance_manager.get(get_resource_key(TRAIT_GLUTTON, Types.TRAIT))
    if sim.has_trait(trait_glutton):
        sim.remove_trait(trait_glutton)

    trait_gradeschool_a = instance_manager.get(get_resource_key(TRAIT_GRADESCHOOL_A, Types.TRAIT))
    if not sim.has_trait(trait_gradeschool_a):
        sim.add_trait(trait_gradeschool_a)

    trait_gradeschool_b = instance_manager.get(get_resource_key(TRAIT_GRADESCHOOL_B, Types.TRAIT))
    if sim.has_trait(trait_gradeschool_b):
        sim.remove_trait(trait_gradeschool_b)

    trait_gradeschool_c = instance_manager.get(get_resource_key(TRAIT_GRADESCHOOL_C, Types.TRAIT))
    if sim.has_trait(trait_gradeschool_c):
        sim.remove_trait(trait_gradeschool_c)

    trait_gradeschool_d = instance_manager.get(get_resource_key(TRAIT_GRADESCHOOL_D, Types.TRAIT))
    if sim.has_trait(trait_gradeschool_d):
        sim.remove_trait(trait_gradeschool_d)

    trait_gradeschool_f = instance_manager.get(get_resource_key(TRAIT_GRADESCHOOL_F, Types.TRAIT))
    if sim.has_trait(trait_gradeschool_f):
        sim.remove_trait(trait_gradeschool_f)

    trait_highschool_a = instance_manager.get(get_resource_key(TRAIT_HIGHSCHOOL_A, Types.TRAIT))
    if not sim.has_trait(trait_highschool_a):
        sim.add_trait(trait_highschool_a)

    trait_highschool_b = instance_manager.get(get_resource_key(TRAIT_HIGHSCHOOL_B, Types.TRAIT))
    if sim.has_trait(trait_highschool_b):
        sim.remove_trait(trait_highschool_b)

    trait_highschool_c = instance_manager.get(get_resource_key(TRAIT_HIGHSCHOOL_C, Types.TRAIT))
    if sim.has_trait(trait_highschool_c):
        sim.remove_trait(trait_highschool_c)

    trait_highschool_d = instance_manager.get(get_resource_key(TRAIT_HIGHSCHOOL_D, Types.TRAIT))
    if sim.has_trait(trait_highschool_d):
        sim.remove_trait(trait_highschool_d)

    trait_highschool_f = instance_manager.get(get_resource_key(TRAIT_HIGHSCHOOL_F, Types.TRAIT))
    if sim.has_trait(trait_highschool_f):
        sim.remove_trait(trait_highschool_f)

    trait_hotheaded = instance_manager.get(get_resource_key(TRAIT_HOTHEADED, Types.TRAIT))
    if sim.has_trait(trait_hotheaded):
        sim.remove_trait(trait_hotheaded)

    trait_hsexit_expelled = instance_manager.get(get_resource_key(TRAIT_HSEXIT_EXPELLED, Types.TRAIT))
    if sim.has_trait(trait_hsexit_expelled):
        sim.remove_trait(trait_hsexit_expelled)

    trait_insane = instance_manager.get(get_resource_key(TRAIT_INSANE, Types.TRAIT))
    if sim.has_trait(trait_insane):
        sim.remove_trait(trait_insane)

    trait_invested = instance_manager.get(get_resource_key(TRAIT_INVESTED, Types.TRAIT))
    if not sim.has_trait(trait_invested):
        sim.add_trait(trait_invested)

    trait_ispregnant = instance_manager.get(get_resource_key(TRAIT_ISPREGNANT, Types.TRAIT))
    if sim.has_trait(trait_ispregnant):
        sim.remove_trait(trait_ispregnant)

    trait_mechanicalsuit_hoverengaged = instance_manager.get(get_resource_key(TRAIT_MECHANICALSUIT_HOVERENGAGED, Types.TRAIT))
    if sim.has_trait(trait_mechanicalsuit_hoverengaged):
        sim.remove_trait(trait_mechanicalsuit_hoverengaged)

    trait_mechanicalsuit_wearing_body_beigewhite = instance_manager.get(get_resource_key(TRAIT_MECHANICALSUIT_WEARING_BODY_BEIGEWHITE, Types.TRAIT))
    if sim.has_trait(trait_mechanicalsuit_wearing_body_beigewhite):
        sim.remove_trait(trait_mechanicalsuit_wearing_body_beigewhite)

    trait_mechanicalsuit_wearing_body_blackblue = instance_manager.get(get_resource_key(TRAIT_MECHANICALSUIT_WEARING_BODY_BLACKBLUE, Types.TRAIT))
    if sim.has_trait(trait_mechanicalsuit_wearing_body_blackblue):
        sim.remove_trait(trait_mechanicalsuit_wearing_body_blackblue)

    trait_mechanicalsuit_wearing_body_bluered = instance_manager.get(get_resource_key(TRAIT_MECHANICALSUIT_WEARING_BODY_BLUERED, Types.TRAIT))
    if sim.has_trait(trait_mechanicalsuit_wearing_body_bluered):
        sim.remove_trait(trait_mechanicalsuit_wearing_body_bluered)

    trait_mechanicalsuit_wearing_body_graybrown = instance_manager.get(get_resource_key(TRAIT_MECHANICALSUIT_WEARING_BODY_GRAYBROWN, Types.TRAIT))
    if sim.has_trait(trait_mechanicalsuit_wearing_body_graybrown):
        sim.remove_trait(trait_mechanicalsuit_wearing_body_graybrown)

    trait_mechanicalsuit_wearing_body_greenbrown = instance_manager.get(get_resource_key(TRAIT_MECHANICALSUIT_WEARING_BODY_GREENBROWN, Types.TRAIT))
    if sim.has_trait(trait_mechanicalsuit_wearing_body_greenbrown):
        sim.remove_trait(trait_mechanicalsuit_wearing_body_greenbrown)

    trait_mechanicalsuit_wearing_body_redgreen = instance_manager.get(get_resource_key(TRAIT_MECHANICALSUIT_WEARING_BODY_REDGREEN, Types.TRAIT))
    if sim.has_trait(trait_mechanicalsuit_wearing_body_redgreen):
        sim.remove_trait(trait_mechanicalsuit_wearing_body_redgreen)

    trait_mechanicalsuit_wearing_body_whitecopper = instance_manager.get(get_resource_key(TRAIT_MECHANICALSUIT_WEARING_BODY_WHITECOPPER, Types.TRAIT))
    if sim.has_trait(trait_mechanicalsuit_wearing_body_whitecopper):
        sim.remove_trait(trait_mechanicalsuit_wearing_body_whitecopper)

    trait_mechanicalsuit_wearing_helmet_blackblue = instance_manager.get(get_resource_key(TRAIT_MECHANICALSUIT_WEARING_HELMET_BLACKBLUE, Types.TRAIT))
    if sim.has_trait(trait_mechanicalsuit_wearing_helmet_blackblue):
        sim.remove_trait(trait_mechanicalsuit_wearing_helmet_blackblue)

    trait_mechanicalsuit_wearing_helmet_blackcopper = instance_manager.get(get_resource_key(TRAIT_MECHANICALSUIT_WEARING_HELMET_BLACKCOPPER, Types.TRAIT))
    if sim.has_trait(trait_mechanicalsuit_wearing_helmet_blackcopper):
        sim.remove_trait(trait_mechanicalsuit_wearing_helmet_blackcopper)

    trait_mechanicalsuit_wearing_helmet_blackgold = instance_manager.get(get_resource_key(TRAIT_MECHANICALSUIT_WEARING_HELMET_BLACKGOLD, Types.TRAIT))
    if sim.has_trait(trait_mechanicalsuit_wearing_helmet_blackgold):
        sim.remove_trait(trait_mechanicalsuit_wearing_helmet_blackgold)

    trait_mechanicalsuit_wearing_helmet_blackgray = instance_manager.get(get_resource_key(TRAIT_MECHANICALSUIT_WEARING_HELMET_BLACKGRAY, Types.TRAIT))
    if sim.has_trait(trait_mechanicalsuit_wearing_helmet_blackgray):
        sim.remove_trait(trait_mechanicalsuit_wearing_helmet_blackgray)

    trait_mechanicalsuit_wearing_helmet_bluegray = instance_manager.get(get_resource_key(TRAIT_MECHANICALSUIT_WEARING_HELMET_BLUEGRAY, Types.TRAIT))
    if sim.has_trait(trait_mechanicalsuit_wearing_helmet_bluegray):
        sim.remove_trait(trait_mechanicalsuit_wearing_helmet_bluegray)

    trait_mechanicalsuit_wearing_helmet_grayblack = instance_manager.get(get_resource_key(TRAIT_MECHANICALSUIT_WEARING_HELMET_GRAYBLACK, Types.TRAIT))
    if sim.has_trait(trait_mechanicalsuit_wearing_helmet_grayblack):
        sim.remove_trait(trait_mechanicalsuit_wearing_helmet_grayblack)

    trait_mechanicalsuit_wearing_helmet_greenblack = instance_manager.get(get_resource_key(TRAIT_MECHANICALSUIT_WEARING_HELMET_GREENBLACK, Types.TRAIT))
    if sim.has_trait(trait_mechanicalsuit_wearing_helmet_greenblack):
        sim.remove_trait(trait_mechanicalsuit_wearing_helmet_greenblack)

    trait_nightowl_crystalhelmet = instance_manager.get(get_resource_key(TRAIT_NIGHTOWL_CRYSTALHELMET, Types.TRAIT))
    if sim.has_trait(trait_nightowl_crystalhelmet):
        sim.remove_trait(trait_nightowl_crystalhelmet)

    trait_roboticsarm_wearing_beigewhite = instance_manager.get(get_resource_key(TRAIT_ROBOTICSARM_WEARING_BEIGEWHITE, Types.TRAIT))
    if sim.has_trait(trait_roboticsarm_wearing_beigewhite):
        sim.remove_trait(trait_roboticsarm_wearing_beigewhite)

    trait_roboticsarm_wearing_blackblue = instance_manager.get(get_resource_key(TRAIT_ROBOTICSARM_WEARING_BLACKBLUE, Types.TRAIT))
    if sim.has_trait(trait_roboticsarm_wearing_blackblue):
        sim.remove_trait(trait_roboticsarm_wearing_blackblue)

    trait_roboticsarm_wearing_bluered = instance_manager.get(get_resource_key(TRAIT_ROBOTICSARM_WEARING_BLUERED, Types.TRAIT))
    if sim.has_trait(trait_roboticsarm_wearing_bluered):
        sim.remove_trait(trait_roboticsarm_wearing_bluered)

    trait_roboticsarm_wearing_graybrown = instance_manager.get(get_resource_key(TRAIT_ROBOTICSARM_WEARING_GRAYBROWN, Types.TRAIT))
    if sim.has_trait(trait_roboticsarm_wearing_graybrown):
        sim.remove_trait(trait_roboticsarm_wearing_graybrown)

    trait_roboticsarm_wearing_greenbrown = instance_manager.get(get_resource_key(TRAIT_ROBOTICSARM_WEARING_GREENBROWN, Types.TRAIT))
    if sim.has_trait(trait_roboticsarm_wearing_greenbrown):
        sim.remove_trait(trait_roboticsarm_wearing_greenbrown)

    trait_roboticsarm_wearing_redgreen = instance_manager.get(get_resource_key(TRAIT_ROBOTICSARM_WEARING_REDGREEN, Types.TRAIT))
    if sim.has_trait(trait_roboticsarm_wearing_redgreen):
        sim.remove_trait(trait_roboticsarm_wearing_redgreen)

    trait_roboticsarm_wearing_whitecopper = instance_manager.get(get_resource_key(TRAIT_ROBOTICSARM_WEARING_WHITECOPPER, Types.TRAIT))
    if sim.has_trait(trait_roboticsarm_wearing_whitecopper):
        sim.remove_trait(trait_roboticsarm_wearing_whitecopper)

    trait_selfassured = instance_manager.get(get_resource_key(TRAIT_SELFASSURED, Types.TRAIT))
    if not sim.has_trait(trait_selfassured):
        sim.add_trait(trait_selfassured)

    trait_sexualorientation_woohoointerests_female = instance_manager.get(get_resource_key(TRAIT_SEXUALORIENTATION_WOOHOOINTERESTS_FEMALE, Types.TRAIT))
    if not sim.has_trait(trait_sexualorientation_woohoointerests_female):
        sim.add_trait(trait_sexualorientation_woohoointerests_female)

    trait_sexualorientation_woohoointerests_male = instance_manager.get(get_resource_key(TRAIT_SEXUALORIENTATION_WOOHOOINTERESTS_MALE, Types.TRAIT))
    if not sim.has_trait(trait_sexualorientation_woohoointerests_male):
        sim.add_trait(trait_sexualorientation_woohoointerests_male)

    trait_sexualorientation_woohoointerests_notfemale = instance_manager.get(get_resource_key(TRAIT_SEXUALORIENTATION_WOOHOOINTERESTS_NOTFEMALE, Types.TRAIT))
    if sim.has_trait(trait_sexualorientation_woohoointerests_notfemale):
        sim.remove_trait(trait_sexualorientation_woohoointerests_notfemale)

    trait_simpreference_dislikes_activities_djmixing = instance_manager.get(get_resource_key(TRAIT_SIMPREFERENCE_DISLIKES_ACTIVITIES_DJMIXING, Types.TRAIT))
    if sim.has_trait(trait_simpreference_dislikes_activities_djmixing):
        sim.remove_trait(trait_simpreference_dislikes_activities_djmixing)

    trait_simpreference_dislikes_activities_fitness = instance_manager.get(get_resource_key(TRAIT_SIMPREFERENCE_DISLIKES_ACTIVITIES_FITNESS, Types.TRAIT))
    if sim.has_trait(trait_simpreference_dislikes_activities_fitness):
        sim.remove_trait(trait_simpreference_dislikes_activities_fitness)

    trait_simpreference_dislikes_activities_guitar = instance_manager.get(get_resource_key(TRAIT_SIMPREFERENCE_DISLIKES_ACTIVITIES_GUITAR, Types.TRAIT))
    if sim.has_trait(trait_simpreference_dislikes_activities_guitar):
        sim.remove_trait(trait_simpreference_dislikes_activities_guitar)

    trait_simpreference_dislikes_activities_piano = instance_manager.get(get_resource_key(TRAIT_SIMPREFERENCE_DISLIKES_ACTIVITIES_PIANO, Types.TRAIT))
    if sim.has_trait(trait_simpreference_dislikes_activities_piano):
        sim.remove_trait(trait_simpreference_dislikes_activities_piano)

    trait_simpreference_dislikes_activities_pipeorgan = instance_manager.get(get_resource_key(TRAIT_SIMPREFERENCE_DISLIKES_ACTIVITIES_PIPEORGAN, Types.TRAIT))
    if sim.has_trait(trait_simpreference_dislikes_activities_pipeorgan):
        sim.remove_trait(trait_simpreference_dislikes_activities_pipeorgan)

    trait_simpreference_dislikes_activities_programming = instance_manager.get(get_resource_key(TRAIT_SIMPREFERENCE_DISLIKES_ACTIVITIES_PROGRAMMING, Types.TRAIT))
    if sim.has_trait(trait_simpreference_dislikes_activities_programming):
        sim.remove_trait(trait_simpreference_dislikes_activities_programming)

    trait_simpreference_dislikes_activities_rockclimbing = instance_manager.get(get_resource_key(TRAIT_SIMPREFERENCE_DISLIKES_ACTIVITIES_ROCKCLIMBING, Types.TRAIT))
    if sim.has_trait(trait_simpreference_dislikes_activities_rockclimbing):
        sim.remove_trait(trait_simpreference_dislikes_activities_rockclimbing)

    trait_simpreference_dislikes_activities_singing = instance_manager.get(get_resource_key(TRAIT_SIMPREFERENCE_DISLIKES_ACTIVITIES_SINGING, Types.TRAIT))
    if sim.has_trait(trait_simpreference_dislikes_activities_singing):
        sim.remove_trait(trait_simpreference_dislikes_activities_singing)

    trait_simpreference_dislikes_activities_violin = instance_manager.get(get_resource_key(TRAIT_SIMPREFERENCE_DISLIKES_ACTIVITIES_VIOLIN, Types.TRAIT))
    if sim.has_trait(trait_simpreference_dislikes_activities_violin):
        sim.remove_trait(trait_simpreference_dislikes_activities_violin)

    trait_simpreference_dislikes_activities_wellness = instance_manager.get(get_resource_key(TRAIT_SIMPREFERENCE_DISLIKES_ACTIVITIES_WELLNESS, Types.TRAIT))
    if sim.has_trait(trait_simpreference_dislikes_activities_wellness):
        sim.remove_trait(trait_simpreference_dislikes_activities_wellness)

    trait_simpreference_dislikes_activities_writing = instance_manager.get(get_resource_key(TRAIT_SIMPREFERENCE_DISLIKES_ACTIVITIES_WRITING, Types.TRAIT))
    if sim.has_trait(trait_simpreference_dislikes_activities_writing):
        sim.remove_trait(trait_simpreference_dislikes_activities_writing)

    trait_simpreference_likes_activities_fitness = instance_manager.get(get_resource_key(TRAIT_SIMPREFERENCE_LIKES_ACTIVITIES_FITNESS, Types.TRAIT))
    if not sim.has_trait(trait_simpreference_likes_activities_fitness):
        sim.add_trait(trait_simpreference_likes_activities_fitness)

    trait_simpreference_likes_activities_wellness = instance_manager.get(get_resource_key(TRAIT_SIMPREFERENCE_LIKES_ACTIVITIES_WELLNESS, Types.TRAIT))
    if not sim.has_trait(trait_simpreference_likes_activities_wellness):
        sim.add_trait(trait_simpreference_likes_activities_wellness)

    trait_simpreference_noopinion_activities_fitness = instance_manager.get(get_resource_key(TRAIT_SIMPREFERENCE_NOOPINION_ACTIVITIES_FITNESS, Types.TRAIT))
    if sim.has_trait(trait_simpreference_noopinion_activities_fitness):
        sim.remove_trait(trait_simpreference_noopinion_activities_fitness)

    trait_simpreference_noopinion_activities_wellness = instance_manager.get(get_resource_key(TRAIT_SIMPREFERENCE_NOOPINION_ACTIVITIES_WELLNESS, Types.TRAIT))
    if sim.has_trait(trait_simpreference_noopinion_activities_wellness):
        sim.remove_trait(trait_simpreference_noopinion_activities_wellness)

    trait_slob = instance_manager.get(get_resource_key(TRAIT_SLOB, Types.TRAIT))
    if sim.has_trait(trait_slob):
        sim.remove_trait(trait_slob)

    trait_speedcleaner = instance_manager.get(get_resource_key(TRAIT_SPEEDCLEANER, Types.TRAIT))
    if not sim.has_trait(trait_speedcleaner):
        sim.add_trait(trait_speedcleaner)

    trait_speedreader = instance_manager.get(get_resource_key(TRAIT_SPEEDREADER, Types.TRAIT))
    if not sim.has_trait(trait_speedreader):
        sim.add_trait(trait_speedreader)

    trait_stormchaser = instance_manager.get(get_resource_key(TRAIT_STORMCHASER, Types.TRAIT))
    if not sim.has_trait(trait_stormchaser):
        sim.add_trait(trait_stormchaser)

    trait_temperature_burningman = instance_manager.get(get_resource_key(TRAIT_TEMPERATURE_BURNINGMAN, Types.TRAIT))
    if not sim.has_trait(trait_temperature_burningman):
        sim.add_trait(trait_temperature_burningman)

    trait_temperature_coldacclimation = instance_manager.get(get_resource_key(TRAIT_TEMPERATURE_COLDACCLIMATION, Types.TRAIT))
    if sim.has_trait(trait_temperature_coldacclimation):
        sim.remove_trait(trait_temperature_coldacclimation)

    trait_temperature_heatacclimation = instance_manager.get(get_resource_key(TRAIT_TEMPERATURE_HEATACCLIMATION, Types.TRAIT))
    if sim.has_trait(trait_temperature_heatacclimation):
        sim.remove_trait(trait_temperature_heatacclimation)

    trait_temperature_iceman = instance_manager.get(get_resource_key(TRAIT_TEMPERATURE_ICEMAN, Types.TRAIT))
    if not sim.has_trait(trait_temperature_iceman):
        sim.add_trait(trait_temperature_iceman)

    trait_theknack = instance_manager.get(get_resource_key(TRAIT_THEKNACK, Types.TRAIT))
    if not sim.has_trait(trait_theknack):
        sim.add_trait(trait_theknack)

    trait_university_arthistorydegreeba = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_ARTHISTORYDEGREEBA, Types.TRAIT))
    if sim.has_trait(trait_university_arthistorydegreeba):
        sim.remove_trait(trait_university_arthistorydegreeba)

    trait_university_arthistorydegreebs = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_ARTHISTORYDEGREEBS, Types.TRAIT))
    if sim.has_trait(trait_university_arthistorydegreebs):
        sim.remove_trait(trait_university_arthistorydegreebs)

    trait_university_biologydegreeba = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_BIOLOGYDEGREEBA, Types.TRAIT))
    if sim.has_trait(trait_university_biologydegreeba):
        sim.remove_trait(trait_university_biologydegreeba)

    trait_university_biologydegreebs = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_BIOLOGYDEGREEBS, Types.TRAIT))
    if sim.has_trait(trait_university_biologydegreebs):
        sim.remove_trait(trait_university_biologydegreebs)

    trait_university_communicationsdegreeba = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_COMMUNICATIONSDEGREEBA, Types.TRAIT))
    if sim.has_trait(trait_university_communicationsdegreeba):
        sim.remove_trait(trait_university_communicationsdegreeba)

    trait_university_communicationsdegreebs = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_COMMUNICATIONSDEGREEBS, Types.TRAIT))
    if sim.has_trait(trait_university_communicationsdegreebs):
        sim.remove_trait(trait_university_communicationsdegreebs)

    trait_university_computersciencedegreeba = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_COMPUTERSCIENCEDEGREEBA, Types.TRAIT))
    if sim.has_trait(trait_university_computersciencedegreeba):
        sim.remove_trait(trait_university_computersciencedegreeba)

    trait_university_computersciencedegreebs = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_COMPUTERSCIENCEDEGREEBS, Types.TRAIT))
    if sim.has_trait(trait_university_computersciencedegreebs):
        sim.remove_trait(trait_university_computersciencedegreebs)

    trait_university_culinaryartsdegreeba = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_CULINARYARTSDEGREEBA, Types.TRAIT))
    if sim.has_trait(trait_university_culinaryartsdegreeba):
        sim.remove_trait(trait_university_culinaryartsdegreeba)

    trait_university_culinaryartsdegreebs = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_CULINARYARTSDEGREEBS, Types.TRAIT))
    if sim.has_trait(trait_university_culinaryartsdegreebs):
        sim.remove_trait(trait_university_culinaryartsdegreebs)

    trait_university_dramadegreeba = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_DRAMADEGREEBA, Types.TRAIT))
    if sim.has_trait(trait_university_dramadegreeba):
        sim.remove_trait(trait_university_dramadegreeba)

    trait_university_dramadegreebs = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_DRAMADEGREEBS, Types.TRAIT))
    if sim.has_trait(trait_university_dramadegreebs):
        sim.remove_trait(trait_university_dramadegreebs)

    trait_university_economicsdegreeba = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_ECONOMICSDEGREEBA, Types.TRAIT))
    if sim.has_trait(trait_university_economicsdegreeba):
        sim.remove_trait(trait_university_economicsdegreeba)

    trait_university_economicsdegreebs = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_ECONOMICSDEGREEBS, Types.TRAIT))
    if sim.has_trait(trait_university_economicsdegreebs):
        sim.remove_trait(trait_university_economicsdegreebs)

    trait_university_fineartdegreeba = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_FINEARTDEGREEBA, Types.TRAIT))
    if sim.has_trait(trait_university_fineartdegreeba):
        sim.remove_trait(trait_university_fineartdegreeba)

    trait_university_fineartdegreebs = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_FINEARTDEGREEBS, Types.TRAIT))
    if sim.has_trait(trait_university_fineartdegreebs):
        sim.remove_trait(trait_university_fineartdegreebs)

    trait_university_historydegreeba = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_HISTORYDEGREEBA, Types.TRAIT))
    if sim.has_trait(trait_university_historydegreeba):
        sim.remove_trait(trait_university_historydegreeba)

    trait_university_historydegreebs = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_HISTORYDEGREEBS, Types.TRAIT))
    if sim.has_trait(trait_university_historydegreebs):
        sim.remove_trait(trait_university_historydegreebs)

    trait_university_languageandliteraturedegreeba = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_LANGUAGEANDLITERATUREDEGREEBA, Types.TRAIT))
    if sim.has_trait(trait_university_languageandliteraturedegreeba):
        sim.remove_trait(trait_university_languageandliteraturedegreeba)

    trait_university_languageandliteraturedegreebs = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_LANGUAGEANDLITERATUREDEGREEBS, Types.TRAIT))
    if sim.has_trait(trait_university_languageandliteraturedegreebs):
        sim.remove_trait(trait_university_languageandliteraturedegreebs)

    trait_university_physicsdegreeba = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_PHYSICSDEGREEBA, Types.TRAIT))
    if sim.has_trait(trait_university_physicsdegreeba):
        sim.remove_trait(trait_university_physicsdegreeba)

    trait_university_physicsdegreebs = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_PHYSICSDEGREEBS, Types.TRAIT))
    if sim.has_trait(trait_university_physicsdegreebs):
        sim.remove_trait(trait_university_physicsdegreebs)

    trait_university_psychologydegreeba = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_PSYCHOLOGYDEGREEBA, Types.TRAIT))
    if sim.has_trait(trait_university_psychologydegreeba):
        sim.remove_trait(trait_university_psychologydegreeba)

    trait_university_psychologydegreebs = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_PSYCHOLOGYDEGREEBS, Types.TRAIT))
    if sim.has_trait(trait_university_psychologydegreebs):
        sim.remove_trait(trait_university_psychologydegreebs)

    trait_university_villainydegreeba = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_VILLAINYDEGREEBA, Types.TRAIT))
    if sim.has_trait(trait_university_villainydegreeba):
        sim.remove_trait(trait_university_villainydegreeba)

    trait_university_villainydegreebs = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_VILLAINYDEGREEBS, Types.TRAIT))
    if sim.has_trait(trait_university_villainydegreebs):
        sim.remove_trait(trait_university_villainydegreebs)

    trait_walkstylecreepy = instance_manager.get(get_resource_key(TRAIT_WALKSTYLECREEPY, Types.TRAIT))
    if sim.has_trait(trait_walkstylecreepy):
        sim.remove_trait(trait_walkstylecreepy)

    trait_walkstyleenergetic = instance_manager.get(get_resource_key(TRAIT_WALKSTYLEENERGETIC, Types.TRAIT))
    if sim.has_trait(trait_walkstyleenergetic):
        sim.remove_trait(trait_walkstyleenergetic)

    trait_walkstyleenergetic = instance_manager.get(get_resource_key(TRAIT_WALKSTYLEENERGETIC, Types.TRAIT))
    if sim.has_trait(trait_walkstyleenergetic):
        sim.remove_trait(trait_walkstyleenergetic)

    trait_walkstylefeminine = instance_manager.get(get_resource_key(TRAIT_WALKSTYLEFEMININE, Types.TRAIT))
    if sim.has_trait(trait_walkstylefeminine):
        sim.remove_trait(trait_walkstylefeminine)

    trait_walkstylegoofy = instance_manager.get(get_resource_key(TRAIT_WALKSTYLEGOOFY, Types.TRAIT))
    if sim.has_trait(trait_walkstylegoofy):
        sim.remove_trait(trait_walkstylegoofy)

    trait_walkstyleperky = instance_manager.get(get_resource_key(TRAIT_WALKSTYLEPERKY, Types.TRAIT))
    if sim.has_trait(trait_walkstyleperky):
        sim.remove_trait(trait_walkstyleperky)

    trait_walkstylesleepy = instance_manager.get(get_resource_key(TRAIT_WALKSTYLESLEEPY, Types.TRAIT))
    if sim.has_trait(trait_walkstylesleepy):
        sim.remove_trait(trait_walkstylesleepy)

    trait_walkstylesnooty = instance_manager.get(get_resource_key(TRAIT_WALKSTYLESNOOTY, Types.TRAIT))
    if sim.has_trait(trait_walkstylesnooty):
        sim.remove_trait(trait_walkstylesnooty)

    trait_walkstyleswagger = instance_manager.get(get_resource_key(TRAIT_WALKSTYLESWAGGER, Types.TRAIT))
    if sim.has_trait(trait_walkstyleswagger):
        sim.remove_trait(trait_walkstyleswagger)

    trait_walkstyletough = instance_manager.get(get_resource_key(TRAIT_WALKSTYLETOUGH, Types.TRAIT))
    if sim.has_trait(trait_walkstyletough):
        sim.remove_trait(trait_walkstyletough)

    trait_waterproof = instance_manager.get(get_resource_key(TRAIT_WATERPROOF, Types.TRAIT))
    if not sim.has_trait(trait_waterproof):
        sim.add_trait(trait_waterproof)

    trait_webmaster = instance_manager.get(get_resource_key(TRAIT_WEBMASTER, Types.TRAIT))
    if not sim.has_trait(trait_webmaster):
        sim.add_trait(trait_webmaster)

    wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_breastslarge = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_BODYSHAPE_BREASTSLARGE, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_breastslarge):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_breastslarge)

    wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_breastssmall = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_BODYSHAPE_BREASTSSMALL, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_breastssmall):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_breastssmall)

    wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_buttlarge = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_BODYSHAPE_BUTTLARGE, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_buttlarge):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_buttlarge)

    wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_buttsmall = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_BODYSHAPE_BUTTSMALL, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_buttsmall):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_buttsmall)

    wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_heavy = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_BODYSHAPE_HEAVY, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_heavy):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_heavy)

    wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_high = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_BODYSHAPE_HIGH, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_high):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_high)

    wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_light = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_BODYSHAPE_LIGHT, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_light):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_light)

    wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_low = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_BODYSHAPE_LOW, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_low):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_low)

    wickedwhims_attractiveness_trait_simpreference_dislikes_detail_body_hair = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_DETAIL_BODY_HAIR, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_detail_body_hair):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_detail_body_hair)

    wickedwhims_attractiveness_trait_simpreference_dislikes_detail_freckles = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_DETAIL_FRECKLES, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_detail_freckles):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_detail_freckles)

    wickedwhims_attractiveness_trait_simpreference_dislikes_detail_glasses = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_DETAIL_GLASSES, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_detail_glasses):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_detail_glasses)

    wickedwhims_attractiveness_trait_simpreference_dislikes_detail_hats = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_DETAIL_HATS, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_detail_hats):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_detail_hats)

    wickedwhims_attractiveness_trait_simpreference_dislikes_detail_jewelery = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_DETAIL_JEWELERY, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_detail_jewelery):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_detail_jewelery)

    wickedwhims_attractiveness_trait_simpreference_dislikes_detail_makeup = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_DETAIL_MAKEUP, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_detail_makeup):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_detail_makeup)

    wickedwhims_attractiveness_trait_simpreference_dislikes_detail_piercing = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_DETAIL_PIERCING, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_detail_piercing):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_detail_piercing)

    wickedwhims_attractiveness_trait_simpreference_dislikes_detail_tattoos = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_DETAIL_TATTOOS, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_detail_tattoos):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_detail_tattoos)

    wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_blue = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_EYECOLOR_BLUE, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_blue):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_blue)

    wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_blue = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_EYECOLOR_BLUE, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_blue):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_blue)

    wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_brown = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_EYECOLOR_BROWN, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_brown):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_brown)

    wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_brown = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_EYECOLOR_BROWN, Types.TRAIT))
    if not sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_brown):
        sim.add_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_brown)

    wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_green = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_EYECOLOR_GREEN, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_green):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_green)

    wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_green = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_EYECOLOR_GREEN, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_green):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_green)

    wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_unnatural = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_EYECOLOR_UNNATURAL, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_unnatural):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_unnatural)

    wickedwhims_attractiveness_trait_simpreference_dislikes_facialhair_beard = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_FACIALHAIR_BEARD, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_facialhair_beard):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_facialhair_beard)

    wickedwhims_attractiveness_trait_simpreference_dislikes_facialhair_clean = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_FACIALHAIR_CLEAN, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_facialhair_clean):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_facialhair_clean)

    wickedwhims_attractiveness_trait_simpreference_dislikes_facialhair_goatee = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_FACIALHAIR_GOATEE, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_facialhair_goatee):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_facialhair_goatee)

    wickedwhims_attractiveness_trait_simpreference_dislikes_facialhair_mustache = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_FACIALHAIR_MUSTACHE, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_facialhair_mustache):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_facialhair_mustache)

    wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_black = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_HAIRCOLOR_BLACK, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_black):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_black)

    wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_blonde = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_HAIRCOLOR_BLONDE, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_blonde):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_blonde)

    wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_blonde = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_HAIRCOLOR_BLONDE, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_blonde):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_blonde)

    wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_blue = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_HAIRCOLOR_BLUE, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_blue):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_blue)

    wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_blue = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_HAIRCOLOR_BLUE, Types.TRAIT))
    if not sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_blue):
        sim.add_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_blue)

    wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_brown = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_HAIRCOLOR_BROWN, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_brown):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_brown)

    wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_brown = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_HAIRCOLOR_BROWN, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_brown):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_brown)

    wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_gray = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_HAIRCOLOR_GRAY, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_gray):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_gray)

    wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_green = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_HAIRCOLOR_GREEN, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_green):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_green)

    wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_green = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_HAIRCOLOR_GREEN, Types.TRAIT))
    if not sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_green):
        sim.add_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_green)

    wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_pink = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_HAIRCOLOR_PINK, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_pink):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_pink)

    wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_red = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_HAIRCOLOR_RED, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_red):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_red)

    wickedwhims_attractiveness_trait_simpreference_dislikes_hairlength_bald = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_HAIRLENGTH_BALD, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_hairlength_bald):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_hairlength_bald)

    wickedwhims_attractiveness_trait_simpreference_dislikes_hairlength_bald = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_HAIRLENGTH_BALD, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_hairlength_bald):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_hairlength_bald)

    wickedwhims_attractiveness_trait_simpreference_dislikes_hairlength_long = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_HAIRLENGTH_LONG, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_hairlength_long):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_hairlength_long)

    wickedwhims_attractiveness_trait_simpreference_dislikes_hairlength_medium = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_HAIRLENGTH_MEDIUM, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_hairlength_medium):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_hairlength_medium)

    wickedwhims_attractiveness_trait_simpreference_dislikes_hairlength_short = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_HAIRLENGTH_SHORT, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_hairlength_short):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_hairlength_short)

    wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_breastslarge = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_BODYSHAPE_BREASTSLARGE, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_breastslarge):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_breastslarge)

    wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_breastssmall = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_BODYSHAPE_BREASTSSMALL, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_breastssmall):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_breastssmall)

    wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_breastssmall = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_BODYSHAPE_BREASTSSMALL, Types.TRAIT))
    if not sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_breastssmall):
        sim.add_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_breastssmall)

    wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_buttlarge = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_BODYSHAPE_BUTTLARGE, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_buttlarge):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_buttlarge)

    wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_buttlarge = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_BODYSHAPE_BUTTLARGE, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_buttlarge):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_buttlarge)

    wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_buttsmall = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_BODYSHAPE_BUTTSMALL, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_buttsmall):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_buttsmall)

    wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_buttsmall = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_BODYSHAPE_BUTTSMALL, Types.TRAIT))
    if not sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_buttsmall):
        sim.add_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_buttsmall)

    wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_heavy = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_BODYSHAPE_HEAVY, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_heavy):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_heavy)

    wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_high = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_BODYSHAPE_HIGH, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_high):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_high)

    wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_light = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_BODYSHAPE_LIGHT, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_light):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_light)

    wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_low = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_BODYSHAPE_LOW, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_low):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_low)

    wickedwhims_attractiveness_trait_simpreference_likes_detail_body_hair = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_DETAIL_BODY_HAIR, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_body_hair):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_body_hair)

    wickedwhims_attractiveness_trait_simpreference_likes_detail_freckles = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_DETAIL_FRECKLES, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_freckles):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_freckles)

    wickedwhims_attractiveness_trait_simpreference_likes_detail_glasses = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_DETAIL_GLASSES, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_glasses):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_glasses)

    wickedwhims_attractiveness_trait_simpreference_likes_detail_glasses = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_DETAIL_GLASSES, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_glasses):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_glasses)

    wickedwhims_attractiveness_trait_simpreference_likes_detail_hats = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_DETAIL_HATS, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_hats):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_hats)

    wickedwhims_attractiveness_trait_simpreference_likes_detail_hats = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_DETAIL_HATS, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_hats):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_hats)

    wickedwhims_attractiveness_trait_simpreference_likes_detail_jewelery = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_DETAIL_JEWELERY, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_jewelery):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_jewelery)

    wickedwhims_attractiveness_trait_simpreference_likes_detail_makeup = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_DETAIL_MAKEUP, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_makeup):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_makeup)

    wickedwhims_attractiveness_trait_simpreference_likes_detail_piercing = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_DETAIL_PIERCING, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_piercing):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_piercing)

    wickedwhims_attractiveness_trait_simpreference_likes_detail_tattoos = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_DETAIL_TATTOOS, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_tattoos):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_tattoos)

    wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_blue = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_EYECOLOR_BLUE, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_blue):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_blue)

    wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_blue = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_EYECOLOR_BLUE, Types.TRAIT))
    if not sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_blue):
        sim.add_trait(wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_blue)

    wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_brown = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_EYECOLOR_BROWN, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_brown):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_brown)

    wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_brown = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_EYECOLOR_BROWN, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_brown):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_brown)

    wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_green = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_EYECOLOR_GREEN, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_green):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_green)

    wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_green = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_EYECOLOR_GREEN, Types.TRAIT))
    if not sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_green):
        sim.add_trait(wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_green)

    wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_unnatural = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_EYECOLOR_UNNATURAL, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_unnatural):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_unnatural)

    wickedwhims_attractiveness_trait_simpreference_likes_facialhair_beard = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_FACIALHAIR_BEARD, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_facialhair_beard):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_facialhair_beard)

    wickedwhims_attractiveness_trait_simpreference_likes_facialhair_clean = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_FACIALHAIR_CLEAN, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_facialhair_clean):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_facialhair_clean)

    wickedwhims_attractiveness_trait_simpreference_likes_facialhair_goatee = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_FACIALHAIR_GOATEE, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_facialhair_goatee):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_facialhair_goatee)

    wickedwhims_attractiveness_trait_simpreference_likes_facialhair_mustache = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_FACIALHAIR_MUSTACHE, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_facialhair_mustache):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_facialhair_mustache)

    wickedwhims_attractiveness_trait_simpreference_likes_haircolor_black = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_HAIRCOLOR_BLACK, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_black):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_black)

    wickedwhims_attractiveness_trait_simpreference_likes_haircolor_blonde = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_HAIRCOLOR_BLONDE, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_blonde):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_blonde)

    wickedwhims_attractiveness_trait_simpreference_likes_haircolor_blonde = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_HAIRCOLOR_BLONDE, Types.TRAIT))
    if not sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_blonde):
        sim.add_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_blonde)

    wickedwhims_attractiveness_trait_simpreference_likes_haircolor_blue = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_HAIRCOLOR_BLUE, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_blue):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_blue)

    wickedwhims_attractiveness_trait_simpreference_likes_haircolor_brown = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_HAIRCOLOR_BROWN, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_brown):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_brown)

    wickedwhims_attractiveness_trait_simpreference_likes_haircolor_brown = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_HAIRCOLOR_BROWN, Types.TRAIT))
    if not sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_brown):
        sim.add_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_brown)

    wickedwhims_attractiveness_trait_simpreference_likes_haircolor_gray = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_HAIRCOLOR_GRAY, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_gray):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_gray)

    wickedwhims_attractiveness_trait_simpreference_likes_haircolor_green = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_HAIRCOLOR_GREEN, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_green):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_green)

    wickedwhims_attractiveness_trait_simpreference_likes_haircolor_pink = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_HAIRCOLOR_PINK, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_pink):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_pink)

    wickedwhims_attractiveness_trait_simpreference_likes_haircolor_red = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_HAIRCOLOR_RED, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_red):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_red)

    wickedwhims_attractiveness_trait_simpreference_likes_hairlength_bald = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_HAIRLENGTH_BALD, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_hairlength_bald):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_hairlength_bald)

    wickedwhims_attractiveness_trait_simpreference_likes_hairlength_long = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_HAIRLENGTH_LONG, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_hairlength_long):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_hairlength_long)

    wickedwhims_attractiveness_trait_simpreference_likes_hairlength_medium = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_HAIRLENGTH_MEDIUM, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_hairlength_medium):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_hairlength_medium)

    wickedwhims_attractiveness_trait_simpreference_likes_hairlength_short = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_HAIRLENGTH_SHORT, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_hairlength_short):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_hairlength_short)

    wickedwhims_trait_attractivenessblacklist = instance_manager.get(get_resource_key(WICKEDWHIMS_TRAIT_ATTRACTIVENESSBLACKLIST, Types.TRAIT))
    if sim.has_trait(wickedwhims_trait_attractivenessblacklist):
        sim.remove_trait(wickedwhims_trait_attractivenessblacklist)

    wickedwhims_trait_bodyhair_pubichair_isdisabled = instance_manager.get(get_resource_key(WICKEDWHIMS_TRAIT_BODYHAIR_PUBICHAIR_ISDISABLED, Types.TRAIT))
    if not sim.has_trait(wickedwhims_trait_bodyhair_pubichair_isdisabled):
        sim.add_trait(wickedwhims_trait_bodyhair_pubichair_isdisabled)

    wickedwhims_trait_bodyhair_pubichair_isgrowthdisabled = instance_manager.get(get_resource_key(WICKEDWHIMS_TRAIT_BODYHAIR_PUBICHAIR_ISGROWTHDISABLED, Types.TRAIT))
    if not sim.has_trait(wickedwhims_trait_bodyhair_pubichair_isgrowthdisabled):
        sim.add_trait(wickedwhims_trait_bodyhair_pubichair_isgrowthdisabled)

    wickedwhims_trait_cumslut = instance_manager.get(get_resource_key(WICKEDWHIMS_TRAIT_CUMSLUT, Types.TRAIT))
    if not sim.has_trait(wickedwhims_trait_cumslut):
        sim.add_trait(wickedwhims_trait_cumslut)

    wickedwhims_trait_improved_absorbency = instance_manager.get(get_resource_key(WICKEDWHIMS_TRAIT_IMPROVED_ABSORBENCY, Types.TRAIT))
    if not sim.has_trait(wickedwhims_trait_improved_absorbency):
        sim.add_trait(wickedwhims_trait_improved_absorbency)

    wickedwhims_trait_postpubertyteen = instance_manager.get(get_resource_key(WICKEDWHIMS_TRAIT_POSTPUBERTYTEEN, Types.TRAIT))
    if not sim.has_trait(wickedwhims_trait_postpubertyteen):
        sim.add_trait(wickedwhims_trait_postpubertyteen)

    wickedwhims_trait_sex_attribute_badatsex = instance_manager.get(get_resource_key(WICKEDWHIMS_TRAIT_SEX_ATTRIBUTE_BADATSEX, Types.TRAIT))
    if sim.has_trait(wickedwhims_trait_sex_attribute_badatsex):
        sim.remove_trait(wickedwhims_trait_sex_attribute_badatsex)

    wickedwhims_trait_sex_sexuallyabstinent = instance_manager.get(get_resource_key(WICKEDWHIMS_TRAIT_SEX_SEXUALLYABSTINENT, Types.TRAIT))
    if sim.has_trait(wickedwhims_trait_sex_sexuallyabstinent):
        sim.remove_trait(wickedwhims_trait_sex_sexuallyabstinent)


    # Remove or add traits from ss sims
    trait_alluring = instance_manager.get(get_resource_key(TRAIT_ALLURING, Types.TRAIT))
    if not sim.has_trait(trait_alluring):
        sim.add_trait(trait_alluring)

    trait_dastardly = instance_manager.get(get_resource_key(TRAIT_DASTARDLY, Types.TRAIT))
    if sim.has_trait(trait_dastardly):
        sim.remove_trait(trait_dastardly)

    trait_evil = instance_manager.get(get_resource_key(TRAIT_EVIL, Types.TRAIT))
    if sim.has_trait(trait_evil):
        sim.remove_trait(trait_evil)

    trait_genderoptions_attractedto_female = instance_manager.get(get_resource_key(TRAIT_GENDEROPTIONS_ATTRACTEDTO_FEMALE, Types.TRAIT))
    if not sim.has_trait(trait_genderoptions_attractedto_female):
        sim.add_trait(trait_genderoptions_attractedto_female)

    trait_genderoptions_attractedto_male = instance_manager.get(get_resource_key(TRAIT_GENDEROPTIONS_ATTRACTEDTO_MALE, Types.TRAIT))
    if not sim.has_trait(trait_genderoptions_attractedto_male):
        sim.add_trait(trait_genderoptions_attractedto_male)

    trait_genderoptions_clothing_womenswear = instance_manager.get(get_resource_key(TRAIT_GENDEROPTIONS_CLOTHING_WOMENSWEAR, Types.TRAIT))
    if not sim.has_trait(trait_genderoptions_clothing_womenswear):
        sim.add_trait(trait_genderoptions_clothing_womenswear)

    trait_genderoptions_frame_feminine = instance_manager.get(get_resource_key(TRAIT_GENDEROPTIONS_FRAME_FEMININE, Types.TRAIT))
    if not sim.has_trait(trait_genderoptions_frame_feminine):
        sim.add_trait(trait_genderoptions_frame_feminine)

    trait_genderoptions_frame_masculine = instance_manager.get(get_resource_key(TRAIT_GENDEROPTIONS_FRAME_MASCULINE, Types.TRAIT))
    if sim.has_trait(trait_genderoptions_frame_masculine):
        sim.remove_trait(trait_genderoptions_frame_masculine)

    trait_genderoptions_pregnancy_canbeimpregnated = instance_manager.get(get_resource_key(TRAIT_GENDEROPTIONS_PREGNANCY_CANBEIMPREGNATED, Types.TRAIT))
    if not sim.has_trait(trait_genderoptions_pregnancy_canbeimpregnated):
        sim.add_trait(trait_genderoptions_pregnancy_canbeimpregnated)

    trait_genderoptions_pregnancy_cannotimpregnate = instance_manager.get(get_resource_key(TRAIT_GENDEROPTIONS_PREGNANCY_CANNOTIMPREGNATE, Types.TRAIT))
    if not sim.has_trait(trait_genderoptions_pregnancy_cannotimpregnate):
        sim.add_trait(trait_genderoptions_pregnancy_cannotimpregnate)

    trait_gloomy = instance_manager.get(get_resource_key(TRAIT_GLOOMY, Types.TRAIT))
    if sim.has_trait(trait_gloomy):
        sim.remove_trait(trait_gloomy)

    trait_greatkisser = instance_manager.get(get_resource_key(TRAIT_GREATKISSER, Types.TRAIT))
    if not sim.has_trait(trait_greatkisser):
        sim.add_trait(trait_greatkisser)

    trait_hsexit_earnedged = instance_manager.get(get_resource_key(TRAIT_HSEXIT_EARNEDGED, Types.TRAIT))
    if not sim.has_trait(trait_hsexit_earnedged):
        sim.add_trait(trait_hsexit_earnedged)

    trait_incrediblyfriendly = instance_manager.get(get_resource_key(TRAIT_INCREDIBLYFRIENDLY, Types.TRAIT))
    if not sim.has_trait(trait_incrediblyfriendly):
        sim.add_trait(trait_incrediblyfriendly)

    trait_jealous = instance_manager.get(get_resource_key(TRAIT_JEALOUS, Types.TRAIT))
    if sim.has_trait(trait_jealous):
        sim.remove_trait(trait_jealous)

    trait_kleptomaniac = instance_manager.get(get_resource_key(TRAIT_KLEPTOMANIAC, Types.TRAIT))
    if sim.has_trait(trait_kleptomaniac):
        sim.remove_trait(trait_kleptomaniac)

    trait_legendary = instance_manager.get(get_resource_key(TRAIT_LEGENDARY, Types.TRAIT))
    if not sim.has_trait(trait_legendary):
        sim.add_trait(trait_legendary)

    trait_mentor = instance_manager.get(get_resource_key(TRAIT_MENTOR, Types.TRAIT))
    if not sim.has_trait(trait_mentor):
        sim.add_trait(trait_mentor)

    trait_player = instance_manager.get(get_resource_key(TRAIT_PLAYER, Types.TRAIT))
    if not sim.has_trait(trait_player):
        sim.add_trait(trait_player)

    trait_shameless = instance_manager.get(get_resource_key(TRAIT_SHAMELESS, Types.TRAIT))
    if not sim.has_trait(trait_shameless):
        sim.add_trait(trait_shameless)

    trait_sicknessimmunity = instance_manager.get(get_resource_key(TRAIT_SICKNESSIMMUNITY, Types.TRAIT))
    if not sim.has_trait(trait_sicknessimmunity):
        sim.add_trait(trait_sicknessimmunity)

    trait_walkstylefeminine = instance_manager.get(get_resource_key(TRAIT_WALKSTYLEFEMININE, Types.TRAIT))
    if not sim.has_trait(trait_walkstylefeminine):
        sim.add_trait(trait_walkstylefeminine)

    wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_breastslarge = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_BODYSHAPE_BREASTSLARGE, Types.TRAIT))
    if not sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_breastslarge):
        sim.add_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_breastslarge)

    wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_buttlarge = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_BODYSHAPE_BUTTLARGE, Types.TRAIT))
    if not sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_buttlarge):
        sim.add_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_buttlarge)

    wickedwhims_attractiveness_trait_simpreference_dislikes_facialhair_beard = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_FACIALHAIR_BEARD, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_facialhair_beard):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_facialhair_beard)

    wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_black = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_HAIRCOLOR_BLACK, Types.TRAIT))
    if not sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_black):
        sim.add_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_black)

    wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_heavy = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_BODYSHAPE_HEAVY, Types.TRAIT))
    if not sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_heavy):
        sim.add_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_heavy)

    wickedwhims_attractiveness_trait_simpreference_likes_facialhair_beard = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_FACIALHAIR_BEARD, Types.TRAIT))
    if not sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_facialhair_beard):
        sim.add_trait(wickedwhims_attractiveness_trait_simpreference_likes_facialhair_beard)

    wickedwhims_trait_nudity_nosweat_reward = instance_manager.get(get_resource_key(WICKEDWHIMS_TRAIT_NUDITY_NOSWEAT_REWARD, Types.TRAIT))
    if not sim.has_trait(wickedwhims_trait_nudity_nosweat_reward):
        sim.add_trait(wickedwhims_trait_nudity_nosweat_reward)

    wickedwhims_trait_relationships_poly = instance_manager.get(get_resource_key(WICKEDWHIMS_TRAIT_RELATIONSHIPS_POLY, Types.TRAIT))
    if not sim.has_trait(wickedwhims_trait_relationships_poly):
        sim.add_trait(wickedwhims_trait_relationships_poly)

    wickedwhims_trait_relationships_sexcheater = instance_manager.get(get_resource_key(WICKEDWHIMS_TRAIT_RELATIONSHIPS_SEXCHEATER, Types.TRAIT))
    if not sim.has_trait(wickedwhims_trait_relationships_sexcheater):
        sim.add_trait(wickedwhims_trait_relationships_sexcheater)

    wickedwhims_trait_sex_attribute_generouslover = instance_manager.get(get_resource_key(WICKEDWHIMS_TRAIT_SEX_ATTRIBUTE_GENEROUSLOVER, Types.TRAIT))
    if not sim.has_trait(wickedwhims_trait_sex_attribute_generouslover):
        sim.add_trait(wickedwhims_trait_sex_attribute_generouslover)

    wickedwhims_trait_sex_cuckold = instance_manager.get(get_resource_key(WICKEDWHIMS_TRAIT_SEX_CUCKOLD, Types.TRAIT))
    if not sim.has_trait(wickedwhims_trait_sex_cuckold):
        sim.add_trait(wickedwhims_trait_sex_cuckold)

    wickedwhims_trait_sex_sexuallyalluring = instance_manager.get(get_resource_key(WICKEDWHIMS_TRAIT_SEX_SEXUALLYALLURING, Types.TRAIT))
    if not sim.has_trait(wickedwhims_trait_sex_sexuallyalluring):
        sim.add_trait(wickedwhims_trait_sex_sexuallyalluring)


@sims4.commands.Command('pbs_wwtrait', command_type=sims4.commands.CommandType.Live)
def pbs_wwtrait(_connection=None):
    # Get the console output
    output = sims4.commands.CheatOutput(_connection)

    # Get the sim_info for the active sim
    sim = services.client_manager().get(_connection).active_sim.sim_info

    # Get the tuned trait instance from the tuning instance manager
    instance_manager = services.get_instance_manager(Types.TRAIT)

    # Remove or add traits from sim
    trait_reward_incest = instance_manager.get(get_resource_key(TRAIT_REWARD_INCEST, Types.TRAIT))
    if not sim.has_trait(trait_reward_incest):
        sim.add_trait(trait_reward_incest)

    wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_breastslarge = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_BODYSHAPE_BREASTSLARGE, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_breastslarge):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_breastslarge)

    wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_breastslarge = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_BODYSHAPE_BREASTSLARGE, Types.TRAIT))
    if not sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_breastslarge):
        sim.add_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_breastslarge)

    wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_breastssmall = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_BODYSHAPE_BREASTSSMALL, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_breastssmall):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_breastssmall)

    wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_buttlarge = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_BODYSHAPE_BUTTLARGE, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_buttlarge):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_buttlarge)

    wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_buttlarge = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_BODYSHAPE_BUTTLARGE, Types.TRAIT))
    if not sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_buttlarge):
        sim.add_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_buttlarge)

    wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_buttsmall = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_BODYSHAPE_BUTTSMALL, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_buttsmall):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_buttsmall)

    wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_heavy = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_BODYSHAPE_HEAVY, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_heavy):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_heavy)

    wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_high = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_BODYSHAPE_HIGH, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_high):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_high)

    wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_light = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_BODYSHAPE_LIGHT, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_light):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_light)

    wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_low = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_BODYSHAPE_LOW, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_low):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_low)

    wickedwhims_attractiveness_trait_simpreference_dislikes_detail_body_hair = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_DETAIL_BODY_HAIR, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_detail_body_hair):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_detail_body_hair)

    wickedwhims_attractiveness_trait_simpreference_dislikes_detail_freckles = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_DETAIL_FRECKLES, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_detail_freckles):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_detail_freckles)

    wickedwhims_attractiveness_trait_simpreference_dislikes_detail_glasses = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_DETAIL_GLASSES, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_detail_glasses):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_detail_glasses)

    wickedwhims_attractiveness_trait_simpreference_dislikes_detail_hats = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_DETAIL_HATS, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_detail_hats):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_detail_hats)

    wickedwhims_attractiveness_trait_simpreference_dislikes_detail_jewelery = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_DETAIL_JEWELERY, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_detail_jewelery):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_detail_jewelery)

    wickedwhims_attractiveness_trait_simpreference_dislikes_detail_makeup = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_DETAIL_MAKEUP, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_detail_makeup):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_detail_makeup)

    wickedwhims_attractiveness_trait_simpreference_dislikes_detail_piercing = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_DETAIL_PIERCING, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_detail_piercing):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_detail_piercing)

    wickedwhims_attractiveness_trait_simpreference_dislikes_detail_tattoos = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_DETAIL_TATTOOS, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_detail_tattoos):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_detail_tattoos)

    wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_blue = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_EYECOLOR_BLUE, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_blue):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_blue)

    wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_blue = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_EYECOLOR_BLUE, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_blue):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_blue)

    wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_brown = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_EYECOLOR_BROWN, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_brown):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_brown)

    wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_brown = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_EYECOLOR_BROWN, Types.TRAIT))
    if not sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_brown):
        sim.add_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_brown)

    wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_green = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_EYECOLOR_GREEN, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_green):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_green)

    wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_green = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_EYECOLOR_GREEN, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_green):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_green)

    wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_unnatural = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_EYECOLOR_UNNATURAL, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_unnatural):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_unnatural)

    wickedwhims_attractiveness_trait_simpreference_dislikes_facialhair_beard = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_FACIALHAIR_BEARD, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_facialhair_beard):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_facialhair_beard)

    wickedwhims_attractiveness_trait_simpreference_dislikes_facialhair_beard = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_FACIALHAIR_BEARD, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_facialhair_beard):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_facialhair_beard)

    wickedwhims_attractiveness_trait_simpreference_dislikes_facialhair_clean = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_FACIALHAIR_CLEAN, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_facialhair_clean):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_facialhair_clean)

    wickedwhims_attractiveness_trait_simpreference_dislikes_facialhair_goatee = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_FACIALHAIR_GOATEE, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_facialhair_goatee):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_facialhair_goatee)

    wickedwhims_attractiveness_trait_simpreference_dislikes_facialhair_mustache = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_FACIALHAIR_MUSTACHE, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_facialhair_mustache):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_facialhair_mustache)

    wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_black = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_HAIRCOLOR_BLACK, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_black):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_black)

    wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_black = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_HAIRCOLOR_BLACK, Types.TRAIT))
    if not sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_black):
        sim.add_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_black)

    wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_blonde = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_HAIRCOLOR_BLONDE, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_blonde):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_blonde)

    wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_blonde = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_HAIRCOLOR_BLONDE, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_blonde):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_blonde)

    wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_blue = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_HAIRCOLOR_BLUE, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_blue):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_blue)

    wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_blue = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_HAIRCOLOR_BLUE, Types.TRAIT))
    if not sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_blue):
        sim.add_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_blue)

    wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_brown = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_HAIRCOLOR_BROWN, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_brown):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_brown)

    wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_brown = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_HAIRCOLOR_BROWN, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_brown):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_brown)

    wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_gray = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_HAIRCOLOR_GRAY, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_gray):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_gray)

    wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_green = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_HAIRCOLOR_GREEN, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_green):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_green)

    wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_green = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_HAIRCOLOR_GREEN, Types.TRAIT))
    if not sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_green):
        sim.add_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_green)

    wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_pink = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_HAIRCOLOR_PINK, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_pink):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_pink)

    wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_red = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_HAIRCOLOR_RED, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_red):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_red)

    wickedwhims_attractiveness_trait_simpreference_dislikes_hairlength_bald = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_HAIRLENGTH_BALD, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_hairlength_bald):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_hairlength_bald)

    wickedwhims_attractiveness_trait_simpreference_dislikes_hairlength_bald = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_HAIRLENGTH_BALD, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_hairlength_bald):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_hairlength_bald)

    wickedwhims_attractiveness_trait_simpreference_dislikes_hairlength_long = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_HAIRLENGTH_LONG, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_hairlength_long):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_hairlength_long)

    wickedwhims_attractiveness_trait_simpreference_dislikes_hairlength_medium = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_HAIRLENGTH_MEDIUM, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_hairlength_medium):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_hairlength_medium)

    wickedwhims_attractiveness_trait_simpreference_dislikes_hairlength_short = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_HAIRLENGTH_SHORT, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_hairlength_short):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_hairlength_short)

    wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_breastslarge = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_BODYSHAPE_BREASTSLARGE, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_breastslarge):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_breastslarge)

    wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_breastssmall = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_BODYSHAPE_BREASTSSMALL, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_breastssmall):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_breastssmall)

    wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_breastssmall = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_BODYSHAPE_BREASTSSMALL, Types.TRAIT))
    if not sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_breastssmall):
        sim.add_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_breastssmall)

    wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_buttlarge = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_BODYSHAPE_BUTTLARGE, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_buttlarge):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_buttlarge)

    wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_buttlarge = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_BODYSHAPE_BUTTLARGE, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_buttlarge):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_buttlarge)

    wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_buttsmall = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_BODYSHAPE_BUTTSMALL, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_buttsmall):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_buttsmall)

    wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_buttsmall = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_BODYSHAPE_BUTTSMALL, Types.TRAIT))
    if not sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_buttsmall):
        sim.add_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_buttsmall)

    wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_heavy = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_BODYSHAPE_HEAVY, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_heavy):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_heavy)

    wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_high = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_BODYSHAPE_HIGH, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_high):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_high)

    wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_light = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_BODYSHAPE_LIGHT, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_light):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_light)

    wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_low = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_BODYSHAPE_LOW, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_low):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_low)

    wickedwhims_attractiveness_trait_simpreference_likes_detail_body_hair = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_DETAIL_BODY_HAIR, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_body_hair):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_body_hair)

    wickedwhims_attractiveness_trait_simpreference_likes_detail_freckles = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_DETAIL_FRECKLES, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_freckles):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_freckles)

    wickedwhims_attractiveness_trait_simpreference_likes_detail_glasses = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_DETAIL_GLASSES, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_glasses):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_glasses)

    wickedwhims_attractiveness_trait_simpreference_likes_detail_glasses = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_DETAIL_GLASSES, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_glasses):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_glasses)

    wickedwhims_attractiveness_trait_simpreference_likes_detail_hats = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_DETAIL_HATS, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_hats):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_hats)

    wickedwhims_attractiveness_trait_simpreference_likes_detail_hats = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_DETAIL_HATS, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_hats):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_hats)

    wickedwhims_attractiveness_trait_simpreference_likes_detail_jewelery = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_DETAIL_JEWELERY, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_jewelery):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_jewelery)

    wickedwhims_attractiveness_trait_simpreference_likes_detail_makeup = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_DETAIL_MAKEUP, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_makeup):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_makeup)

    wickedwhims_attractiveness_trait_simpreference_likes_detail_piercing = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_DETAIL_PIERCING, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_piercing):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_piercing)

    wickedwhims_attractiveness_trait_simpreference_likes_detail_tattoos = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_DETAIL_TATTOOS, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_tattoos):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_tattoos)

    wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_blue = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_EYECOLOR_BLUE, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_blue):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_blue)

    wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_blue = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_EYECOLOR_BLUE, Types.TRAIT))
    if not sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_blue):
        sim.add_trait(wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_blue)

    wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_brown = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_EYECOLOR_BROWN, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_brown):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_brown)

    wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_brown = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_EYECOLOR_BROWN, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_brown):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_brown)

    wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_green = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_EYECOLOR_GREEN, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_green):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_green)

    wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_green = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_EYECOLOR_GREEN, Types.TRAIT))
    if not sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_green):
        sim.add_trait(wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_green)

    wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_unnatural = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_EYECOLOR_UNNATURAL, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_unnatural):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_unnatural)

    wickedwhims_attractiveness_trait_simpreference_likes_facialhair_beard = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_FACIALHAIR_BEARD, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_facialhair_beard):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_facialhair_beard)

    wickedwhims_attractiveness_trait_simpreference_likes_facialhair_clean = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_FACIALHAIR_CLEAN, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_facialhair_clean):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_facialhair_clean)

    wickedwhims_attractiveness_trait_simpreference_likes_facialhair_goatee = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_FACIALHAIR_GOATEE, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_facialhair_goatee):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_facialhair_goatee)

    wickedwhims_attractiveness_trait_simpreference_likes_facialhair_mustache = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_FACIALHAIR_MUSTACHE, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_facialhair_mustache):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_facialhair_mustache)

    wickedwhims_attractiveness_trait_simpreference_likes_haircolor_black = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_HAIRCOLOR_BLACK, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_black):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_black)

    wickedwhims_attractiveness_trait_simpreference_likes_haircolor_blonde = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_HAIRCOLOR_BLONDE, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_blonde):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_blonde)

    wickedwhims_attractiveness_trait_simpreference_likes_haircolor_blonde = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_HAIRCOLOR_BLONDE, Types.TRAIT))
    if not sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_blonde):
        sim.add_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_blonde)

    wickedwhims_attractiveness_trait_simpreference_likes_haircolor_blue = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_HAIRCOLOR_BLUE, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_blue):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_blue)

    wickedwhims_attractiveness_trait_simpreference_likes_haircolor_brown = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_HAIRCOLOR_BROWN, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_brown):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_brown)

    wickedwhims_attractiveness_trait_simpreference_likes_haircolor_brown = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_HAIRCOLOR_BROWN, Types.TRAIT))
    if not sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_brown):
        sim.add_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_brown)

    wickedwhims_attractiveness_trait_simpreference_likes_haircolor_gray = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_HAIRCOLOR_GRAY, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_gray):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_gray)

    wickedwhims_attractiveness_trait_simpreference_likes_haircolor_green = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_HAIRCOLOR_GREEN, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_green):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_green)

    wickedwhims_attractiveness_trait_simpreference_likes_haircolor_pink = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_HAIRCOLOR_PINK, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_pink):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_pink)

    wickedwhims_attractiveness_trait_simpreference_likes_haircolor_red = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_HAIRCOLOR_RED, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_red):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_red)

    wickedwhims_attractiveness_trait_simpreference_likes_hairlength_bald = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_HAIRLENGTH_BALD, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_hairlength_bald):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_hairlength_bald)

    wickedwhims_attractiveness_trait_simpreference_likes_hairlength_long = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_HAIRLENGTH_LONG, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_hairlength_long):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_hairlength_long)

    wickedwhims_attractiveness_trait_simpreference_likes_hairlength_medium = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_HAIRLENGTH_MEDIUM, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_hairlength_medium):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_hairlength_medium)

    wickedwhims_attractiveness_trait_simpreference_likes_hairlength_short = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_HAIRLENGTH_SHORT, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_hairlength_short):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_hairlength_short)

    wickedwhims_trait_attractivenessblacklist = instance_manager.get(get_resource_key(WICKEDWHIMS_TRAIT_ATTRACTIVENESSBLACKLIST, Types.TRAIT))
    if sim.has_trait(wickedwhims_trait_attractivenessblacklist):
        sim.remove_trait(wickedwhims_trait_attractivenessblacklist)

    wickedwhims_trait_bodyhair_pubichair_isdisabled = instance_manager.get(get_resource_key(WICKEDWHIMS_TRAIT_BODYHAIR_PUBICHAIR_ISDISABLED, Types.TRAIT))
    if not sim.has_trait(wickedwhims_trait_bodyhair_pubichair_isdisabled):
        sim.add_trait(wickedwhims_trait_bodyhair_pubichair_isdisabled)

    wickedwhims_trait_bodyhair_pubichair_isgrowthdisabled = instance_manager.get(get_resource_key(WICKEDWHIMS_TRAIT_BODYHAIR_PUBICHAIR_ISGROWTHDISABLED, Types.TRAIT))
    if not sim.has_trait(wickedwhims_trait_bodyhair_pubichair_isgrowthdisabled):
        sim.add_trait(wickedwhims_trait_bodyhair_pubichair_isgrowthdisabled)

    wickedwhims_trait_cumslut = instance_manager.get(get_resource_key(WICKEDWHIMS_TRAIT_CUMSLUT, Types.TRAIT))
    if not sim.has_trait(wickedwhims_trait_cumslut):
        sim.add_trait(wickedwhims_trait_cumslut)

    wickedwhims_trait_improved_absorbency = instance_manager.get(get_resource_key(WICKEDWHIMS_TRAIT_IMPROVED_ABSORBENCY, Types.TRAIT))
    if not sim.has_trait(wickedwhims_trait_improved_absorbency):
        sim.add_trait(wickedwhims_trait_improved_absorbency)

    wickedwhims_trait_postpubertyteen = instance_manager.get(get_resource_key(WICKEDWHIMS_TRAIT_POSTPUBERTYTEEN, Types.TRAIT))
    if not sim.has_trait(wickedwhims_trait_postpubertyteen):
        sim.add_trait(wickedwhims_trait_postpubertyteen)

    wickedwhims_trait_relationships_poly = instance_manager.get(get_resource_key(WICKEDWHIMS_TRAIT_RELATIONSHIPS_POLY, Types.TRAIT))
    if not sim.has_trait(wickedwhims_trait_relationships_poly):
        sim.add_trait(wickedwhims_trait_relationships_poly)

    wickedwhims_trait_relationships_sexcheater = instance_manager.get(get_resource_key(WICKEDWHIMS_TRAIT_RELATIONSHIPS_SEXCHEATER, Types.TRAIT))
    if not sim.has_trait(wickedwhims_trait_relationships_sexcheater):
        sim.add_trait(wickedwhims_trait_relationships_sexcheater)

    wickedwhims_trait_sex_attribute_badatsex = instance_manager.get(get_resource_key(WICKEDWHIMS_TRAIT_SEX_ATTRIBUTE_BADATSEX, Types.TRAIT))
    if sim.has_trait(wickedwhims_trait_sex_attribute_badatsex):
        sim.remove_trait(wickedwhims_trait_sex_attribute_badatsex)

    wickedwhims_trait_sex_attribute_generouslover = instance_manager.get(get_resource_key(WICKEDWHIMS_TRAIT_SEX_ATTRIBUTE_GENEROUSLOVER, Types.TRAIT))
    if not sim.has_trait(wickedwhims_trait_sex_attribute_generouslover):
        sim.add_trait(wickedwhims_trait_sex_attribute_generouslover)

    wickedwhims_trait_sex_cuckold = instance_manager.get(get_resource_key(WICKEDWHIMS_TRAIT_SEX_CUCKOLD, Types.TRAIT))
    if not sim.has_trait(wickedwhims_trait_sex_cuckold):
        sim.add_trait(wickedwhims_trait_sex_cuckold)

    wickedwhims_trait_sex_sexuallyabstinent = instance_manager.get(get_resource_key(WICKEDWHIMS_TRAIT_SEX_SEXUALLYABSTINENT, Types.TRAIT))
    if sim.has_trait(wickedwhims_trait_sex_sexuallyabstinent):
        sim.remove_trait(wickedwhims_trait_sex_sexuallyabstinent)

    wickedwhims_trait_sex_sexuallyalluring = instance_manager.get(get_resource_key(WICKEDWHIMS_TRAIT_SEX_SEXUALLYALLURING, Types.TRAIT))
    if not sim.has_trait(wickedwhims_trait_sex_sexuallyalluring):
        sim.add_trait(wickedwhims_trait_sex_sexuallyalluring)

    trait_genderfemale = instance_manager.get(get_resource_key(TRAIT_GENDERFEMALE, Types.TRAIT))
    trait_gendermale = instance_manager.get(get_resource_key(TRAIT_GENDERMALE, Types.TRAIT))
    # Add Female Traits
    if sim.has_trait(trait_genderfemale):
        wickedwhims_attractiveness_trait_simpreference_likes_facialhair_beard = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_FACIALHAIR_BEARD, Types.TRAIT))
        if not sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_facialhair_beard):
            sim.add_trait(wickedwhims_attractiveness_trait_simpreference_likes_facialhair_beard)


@sims4.commands.Command('pbs_service', command_type=sims4.commands.CommandType.Live)
def pbs_service(_connection=None):
    # Get the console output
    output = sims4.commands.CheatOutput(_connection)

    # Get the sim_info for the active sim
    sim = services.client_manager().get(_connection).active_sim.sim_info

    # Get the tuned trait instance from the tuning instance manager
    instance_manager = services.get_instance_manager(Types.TRAIT)

    # Remove or add traits from all sims
    archaeologyskill_giveauthenticationmail_prohibit = instance_manager.get(get_resource_key(ARCHAEOLOGYSKILL_GIVEAUTHENTICATIONMAIL_PROHIBIT, Types.TRAIT))
    if not sim.has_trait(archaeologyskill_giveauthenticationmail_prohibit):
        sim.add_trait(archaeologyskill_giveauthenticationmail_prohibit)

    fametraits_celebritywalk_on = instance_manager.get(get_resource_key(FAMETRAITS_CELEBRITYWALK_ON, Types.TRAIT))
    if sim.has_trait(fametraits_celebritywalk_on):
        sim.remove_trait(fametraits_celebritywalk_on)

    fametraits_shine_off = instance_manager.get(get_resource_key(FAMETRAITS_SHINE_OFF, Types.TRAIT))
    if not sim.has_trait(fametraits_shine_off):
        sim.add_trait(fametraits_shine_off)

    fametraits_shine_on_rank4 = instance_manager.get(get_resource_key(FAMETRAITS_SHINE_ON_RANK4, Types.TRAIT))
    if sim.has_trait(fametraits_shine_on_rank4):
        sim.remove_trait(fametraits_shine_on_rank4)

    fametraits_shine_on_rank5 = instance_manager.get(get_resource_key(FAMETRAITS_SHINE_ON_RANK5, Types.TRAIT))
    if sim.has_trait(fametraits_shine_on_rank5):
        sim.remove_trait(fametraits_shine_on_rank5)

    trait_computerglasses_wearing = instance_manager.get(get_resource_key(TRAIT_COMPUTERGLASSES_WEARING, Types.TRAIT))
    if sim.has_trait(trait_computerglasses_wearing):
        sim.remove_trait(trait_computerglasses_wearing)

    trait_computerglasses_wearing_blue = instance_manager.get(get_resource_key(TRAIT_COMPUTERGLASSES_WEARING_BLUE, Types.TRAIT))
    if sim.has_trait(trait_computerglasses_wearing_blue):
        sim.remove_trait(trait_computerglasses_wearing_blue)

    trait_computerglasses_wearing_green = instance_manager.get(get_resource_key(TRAIT_COMPUTERGLASSES_WEARING_GREEN, Types.TRAIT))
    if sim.has_trait(trait_computerglasses_wearing_green):
        sim.remove_trait(trait_computerglasses_wearing_green)

    trait_computerglasses_wearing_orange = instance_manager.get(get_resource_key(TRAIT_COMPUTERGLASSES_WEARING_ORANGE, Types.TRAIT))
    if sim.has_trait(trait_computerglasses_wearing_orange):
        sim.remove_trait(trait_computerglasses_wearing_orange)

    trait_computerglasses_wearing_pink = instance_manager.get(get_resource_key(TRAIT_COMPUTERGLASSES_WEARING_PINK, Types.TRAIT))
    if sim.has_trait(trait_computerglasses_wearing_pink):
        sim.remove_trait(trait_computerglasses_wearing_pink)

    trait_computerglasses_wearing_red = instance_manager.get(get_resource_key(TRAIT_COMPUTERGLASSES_WEARING_RED, Types.TRAIT))
    if sim.has_trait(trait_computerglasses_wearing_red):
        sim.remove_trait(trait_computerglasses_wearing_red)

    trait_computerglasses_wearing_yellow = instance_manager.get(get_resource_key(TRAIT_COMPUTERGLASSES_WEARING_YELLOW, Types.TRAIT))
    if sim.has_trait(trait_computerglasses_wearing_yellow):
        sim.remove_trait(trait_computerglasses_wearing_yellow)

    trait_crystalhelmet_alabaster = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_ALABASTER, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_alabaster):
        sim.remove_trait(trait_crystalhelmet_alabaster)

    trait_crystalhelmet_alexandrite_ep = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_ALEXANDRITE_EP, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_alexandrite_ep):
        sim.remove_trait(trait_crystalhelmet_alexandrite_ep)

    trait_crystalhelmet_amazonite_ep = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_AMAZONITE_EP, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_amazonite_ep):
        sim.remove_trait(trait_crystalhelmet_amazonite_ep)

    trait_crystalhelmet_amethyst = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_AMETHYST, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_amethyst):
        sim.remove_trait(trait_crystalhelmet_amethyst)

    trait_crystalhelmet_citrine = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_CITRINE, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_citrine):
        sim.remove_trait(trait_crystalhelmet_citrine)

    trait_crystalhelmet_crandestine_ep = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_CRANDESTINE_EP, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_crandestine_ep):
        sim.remove_trait(trait_crystalhelmet_crandestine_ep)

    trait_crystalhelmet_diamond = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_DIAMOND, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_diamond):
        sim.remove_trait(trait_crystalhelmet_diamond)

    trait_crystalhelmet_emerald = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_EMERALD, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_emerald):
        sim.remove_trait(trait_crystalhelmet_emerald)

    trait_crystalhelmet_fireopal = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_FIREOPAL, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_fireopal):
        sim.remove_trait(trait_crystalhelmet_fireopal)

    trait_crystalhelmet_hematite = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_HEMATITE, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_hematite):
        sim.remove_trait(trait_crystalhelmet_hematite)

    trait_crystalhelmet_jet = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_JET, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_jet):
        sim.remove_trait(trait_crystalhelmet_jet)

    trait_crystalhelmet_jonquilyst = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_JONQUILYST, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_jonquilyst):
        sim.remove_trait(trait_crystalhelmet_jonquilyst)

    trait_crystalhelmet_nitelite_ep = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_NITELITE_EP, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_nitelite_ep):
        sim.remove_trait(trait_crystalhelmet_nitelite_ep)

    trait_crystalhelmet_orangetopaz = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_ORANGETOPAZ, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_orangetopaz):
        sim.remove_trait(trait_crystalhelmet_orangetopaz)

    trait_crystalhelmet_peach = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_PEACH, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_peach):
        sim.remove_trait(trait_crystalhelmet_peach)

    trait_crystalhelmet_plumbite = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_PLUMBITE, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_plumbite):
        sim.remove_trait(trait_crystalhelmet_plumbite)

    trait_crystalhelmet_quartz = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_QUARTZ, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_quartz):
        sim.remove_trait(trait_crystalhelmet_quartz)

    trait_crystalhelmet_rainborz = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_RAINBORZ, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_rainborz):
        sim.remove_trait(trait_crystalhelmet_rainborz)

    trait_crystalhelmet_rose = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_ROSE, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_rose):
        sim.remove_trait(trait_crystalhelmet_rose)

    trait_crystalhelmet_ruby = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_RUBY, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_ruby):
        sim.remove_trait(trait_crystalhelmet_ruby)

    trait_crystalhelmet_sapphire = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_SAPPHIRE, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_sapphire):
        sim.remove_trait(trait_crystalhelmet_sapphire)

    trait_crystalhelmet_shinalite = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_SHINALITE, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_shinalite):
        sim.remove_trait(trait_crystalhelmet_shinalite)

    trait_crystalhelmet_simanite = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_SIMANITE, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_simanite):
        sim.remove_trait(trait_crystalhelmet_simanite)

    trait_crystalhelmet_turquoise = instance_manager.get(get_resource_key(TRAIT_CRYSTALHELMET_TURQUOISE, Types.TRAIT))
    if sim.has_trait(trait_crystalhelmet_turquoise):
        sim.remove_trait(trait_crystalhelmet_turquoise)

    trait_doctor_sicknessresistant = instance_manager.get(get_resource_key(TRAIT_DOCTOR_SICKNESSRESISTANT, Types.TRAIT))
    if not sim.has_trait(trait_doctor_sicknessresistant):
        sim.add_trait(trait_doctor_sicknessresistant)

    trait_essenceofflavor = instance_manager.get(get_resource_key(TRAIT_ESSENCEOFFLAVOR, Types.TRAIT))
    if sim.has_trait(trait_essenceofflavor):
        sim.remove_trait(trait_essenceofflavor)

    trait_fear_beingcheatedon = instance_manager.get(get_resource_key(TRAIT_FEAR_BEINGCHEATEDON, Types.TRAIT))
    if sim.has_trait(trait_fear_beingcheatedon):
        sim.remove_trait(trait_fear_beingcheatedon)

    trait_fear_beingjudged = instance_manager.get(get_resource_key(TRAIT_FEAR_BEINGJUDGED, Types.TRAIT))
    if sim.has_trait(trait_fear_beingjudged):
        sim.remove_trait(trait_fear_beingjudged)

    trait_fear_cowplant = instance_manager.get(get_resource_key(TRAIT_FEAR_COWPLANT, Types.TRAIT))
    if sim.has_trait(trait_fear_cowplant):
        sim.remove_trait(trait_fear_cowplant)

    trait_fear_crowdedplaces = instance_manager.get(get_resource_key(TRAIT_FEAR_CROWDEDPLACES, Types.TRAIT))
    if sim.has_trait(trait_fear_crowdedplaces):
        sim.remove_trait(trait_fear_crowdedplaces)

    trait_fear_dark = instance_manager.get(get_resource_key(TRAIT_FEAR_DARK, Types.TRAIT))
    if sim.has_trait(trait_fear_dark):
        sim.remove_trait(trait_fear_dark)

    trait_fear_deadendjob = instance_manager.get(get_resource_key(TRAIT_FEAR_DEADENDJOB, Types.TRAIT))
    if sim.has_trait(trait_fear_deadendjob):
        sim.remove_trait(trait_fear_deadendjob)

    trait_fear_death = instance_manager.get(get_resource_key(TRAIT_FEAR_DEATH, Types.TRAIT))
    if sim.has_trait(trait_fear_death):
        sim.remove_trait(trait_fear_death)

    trait_fear_disappointingparents = instance_manager.get(get_resource_key(TRAIT_FEAR_DISAPPOINTINGPARENTS, Types.TRAIT))
    if sim.has_trait(trait_fear_disappointingparents):
        sim.remove_trait(trait_fear_disappointingparents)

    trait_fear_disappointingparents_parentdeceasedflag = instance_manager.get(get_resource_key(TRAIT_FEAR_DISAPPOINTINGPARENTS_PARENTDECEASEDFLAG, Types.TRAIT))
    if sim.has_trait(trait_fear_disappointingparents_parentdeceasedflag):
        sim.remove_trait(trait_fear_disappointingparents_parentdeceasedflag)

    trait_fear_failing_afterschoolactivities = instance_manager.get(get_resource_key(TRAIT_FEAR_FAILING_AFTERSCHOOLACTIVITIES, Types.TRAIT))
    if sim.has_trait(trait_fear_failing_afterschoolactivities):
        sim.remove_trait(trait_fear_failing_afterschoolactivities)

    trait_fear_failing_class = instance_manager.get(get_resource_key(TRAIT_FEAR_FAILING_CLASS, Types.TRAIT))
    if sim.has_trait(trait_fear_failing_class):
        sim.remove_trait(trait_fear_failing_class)

    trait_fear_failing_tests = instance_manager.get(get_resource_key(TRAIT_FEAR_FAILING_TESTS, Types.TRAIT))
    if sim.has_trait(trait_fear_failing_tests):
        sim.remove_trait(trait_fear_failing_tests)

    trait_fear_failure = instance_manager.get(get_resource_key(TRAIT_FEAR_FAILURE, Types.TRAIT))
    if sim.has_trait(trait_fear_failure):
        sim.remove_trait(trait_fear_failure)

    trait_fear_fire = instance_manager.get(get_resource_key(TRAIT_FEAR_FIRE, Types.TRAIT))
    if sim.has_trait(trait_fear_fire):
        sim.remove_trait(trait_fear_fire)

    trait_fear_ghosts = instance_manager.get(get_resource_key(TRAIT_FEAR_GHOSTS, Types.TRAIT))
    if sim.has_trait(trait_fear_ghosts):
        sim.remove_trait(trait_fear_ghosts)

    trait_fear_homework = instance_manager.get(get_resource_key(TRAIT_FEAR_HOMEWORK, Types.TRAIT))
    if sim.has_trait(trait_fear_homework):
        sim.remove_trait(trait_fear_homework)

    trait_fear_swimming = instance_manager.get(get_resource_key(TRAIT_FEAR_SWIMMING, Types.TRAIT))
    if sim.has_trait(trait_fear_swimming):
        sim.remove_trait(trait_fear_swimming)

    trait_fear_unfulfilled = instance_manager.get(get_resource_key(TRAIT_FEAR_UNFULFILLED, Types.TRAIT))
    if sim.has_trait(trait_fear_unfulfilled):
        sim.remove_trait(trait_fear_unfulfilled)

    trait_filthdweller = instance_manager.get(get_resource_key(TRAIT_FILTHDWELLER, Types.TRAIT))
    if sim.has_trait(trait_filthdweller):
        sim.remove_trait(trait_filthdweller)

    trait_freeservices = instance_manager.get(get_resource_key(TRAIT_FREESERVICES, Types.TRAIT))
    if not sim.has_trait(trait_freeservices):
        sim.add_trait(trait_freeservices)

    trait_frugal = instance_manager.get(get_resource_key(TRAIT_FRUGAL, Types.TRAIT))
    if not sim.has_trait(trait_frugal):
        sim.add_trait(trait_frugal)

    trait_genderoptions_attractedto_notfemale = instance_manager.get(get_resource_key(TRAIT_GENDEROPTIONS_ATTRACTEDTO_NOTFEMALE, Types.TRAIT))
    if sim.has_trait(trait_genderoptions_attractedto_notfemale):
        sim.remove_trait(trait_genderoptions_attractedto_notfemale)

    trait_genderoptions_attractedto_notmale = instance_manager.get(get_resource_key(TRAIT_GENDEROPTIONS_ATTRACTEDTO_NOTMALE, Types.TRAIT))
    if sim.has_trait(trait_genderoptions_attractedto_notmale):
        sim.remove_trait(trait_genderoptions_attractedto_notmale)

    trait_genderoptions_sexuality_exploring = instance_manager.get(get_resource_key(TRAIT_GENDEROPTIONS_SEXUALITY_EXPLORING, Types.TRAIT))
    if not sim.has_trait(trait_genderoptions_sexuality_exploring):
        sim.add_trait(trait_genderoptions_sexuality_exploring)

    trait_genderoptions_sexuality_notexploring = instance_manager.get(get_resource_key(TRAIT_GENDEROPTIONS_SEXUALITY_NOTEXPLORING, Types.TRAIT))
    if sim.has_trait(trait_genderoptions_sexuality_notexploring):
        sim.remove_trait(trait_genderoptions_sexuality_notexploring)

    trait_glutton = instance_manager.get(get_resource_key(TRAIT_GLUTTON, Types.TRAIT))
    if sim.has_trait(trait_glutton):
        sim.remove_trait(trait_glutton)

    trait_gradeschool_a = instance_manager.get(get_resource_key(TRAIT_GRADESCHOOL_A, Types.TRAIT))
    if not sim.has_trait(trait_gradeschool_a):
        sim.add_trait(trait_gradeschool_a)

    trait_gradeschool_b = instance_manager.get(get_resource_key(TRAIT_GRADESCHOOL_B, Types.TRAIT))
    if sim.has_trait(trait_gradeschool_b):
        sim.remove_trait(trait_gradeschool_b)

    trait_gradeschool_c = instance_manager.get(get_resource_key(TRAIT_GRADESCHOOL_C, Types.TRAIT))
    if sim.has_trait(trait_gradeschool_c):
        sim.remove_trait(trait_gradeschool_c)

    trait_gradeschool_d = instance_manager.get(get_resource_key(TRAIT_GRADESCHOOL_D, Types.TRAIT))
    if sim.has_trait(trait_gradeschool_d):
        sim.remove_trait(trait_gradeschool_d)

    trait_gradeschool_f = instance_manager.get(get_resource_key(TRAIT_GRADESCHOOL_F, Types.TRAIT))
    if sim.has_trait(trait_gradeschool_f):
        sim.remove_trait(trait_gradeschool_f)

    trait_highschool_a = instance_manager.get(get_resource_key(TRAIT_HIGHSCHOOL_A, Types.TRAIT))
    if not sim.has_trait(trait_highschool_a):
        sim.add_trait(trait_highschool_a)

    trait_highschool_b = instance_manager.get(get_resource_key(TRAIT_HIGHSCHOOL_B, Types.TRAIT))
    if sim.has_trait(trait_highschool_b):
        sim.remove_trait(trait_highschool_b)

    trait_highschool_c = instance_manager.get(get_resource_key(TRAIT_HIGHSCHOOL_C, Types.TRAIT))
    if sim.has_trait(trait_highschool_c):
        sim.remove_trait(trait_highschool_c)

    trait_highschool_d = instance_manager.get(get_resource_key(TRAIT_HIGHSCHOOL_D, Types.TRAIT))
    if sim.has_trait(trait_highschool_d):
        sim.remove_trait(trait_highschool_d)

    trait_highschool_f = instance_manager.get(get_resource_key(TRAIT_HIGHSCHOOL_F, Types.TRAIT))
    if sim.has_trait(trait_highschool_f):
        sim.remove_trait(trait_highschool_f)

    trait_hotheaded = instance_manager.get(get_resource_key(TRAIT_HOTHEADED, Types.TRAIT))
    if sim.has_trait(trait_hotheaded):
        sim.remove_trait(trait_hotheaded)

    trait_hsexit_expelled = instance_manager.get(get_resource_key(TRAIT_HSEXIT_EXPELLED, Types.TRAIT))
    if sim.has_trait(trait_hsexit_expelled):
        sim.remove_trait(trait_hsexit_expelled)

    trait_insane = instance_manager.get(get_resource_key(TRAIT_INSANE, Types.TRAIT))
    if sim.has_trait(trait_insane):
        sim.remove_trait(trait_insane)

    trait_invested = instance_manager.get(get_resource_key(TRAIT_INVESTED, Types.TRAIT))
    if not sim.has_trait(trait_invested):
        sim.add_trait(trait_invested)

    trait_ispregnant = instance_manager.get(get_resource_key(TRAIT_ISPREGNANT, Types.TRAIT))
    if sim.has_trait(trait_ispregnant):
        sim.remove_trait(trait_ispregnant)

    trait_mechanicalsuit_hoverengaged = instance_manager.get(get_resource_key(TRAIT_MECHANICALSUIT_HOVERENGAGED, Types.TRAIT))
    if sim.has_trait(trait_mechanicalsuit_hoverengaged):
        sim.remove_trait(trait_mechanicalsuit_hoverengaged)

    trait_mechanicalsuit_wearing_body_beigewhite = instance_manager.get(get_resource_key(TRAIT_MECHANICALSUIT_WEARING_BODY_BEIGEWHITE, Types.TRAIT))
    if sim.has_trait(trait_mechanicalsuit_wearing_body_beigewhite):
        sim.remove_trait(trait_mechanicalsuit_wearing_body_beigewhite)

    trait_mechanicalsuit_wearing_body_blackblue = instance_manager.get(get_resource_key(TRAIT_MECHANICALSUIT_WEARING_BODY_BLACKBLUE, Types.TRAIT))
    if sim.has_trait(trait_mechanicalsuit_wearing_body_blackblue):
        sim.remove_trait(trait_mechanicalsuit_wearing_body_blackblue)

    trait_mechanicalsuit_wearing_body_bluered = instance_manager.get(get_resource_key(TRAIT_MECHANICALSUIT_WEARING_BODY_BLUERED, Types.TRAIT))
    if sim.has_trait(trait_mechanicalsuit_wearing_body_bluered):
        sim.remove_trait(trait_mechanicalsuit_wearing_body_bluered)

    trait_mechanicalsuit_wearing_body_graybrown = instance_manager.get(get_resource_key(TRAIT_MECHANICALSUIT_WEARING_BODY_GRAYBROWN, Types.TRAIT))
    if sim.has_trait(trait_mechanicalsuit_wearing_body_graybrown):
        sim.remove_trait(trait_mechanicalsuit_wearing_body_graybrown)

    trait_mechanicalsuit_wearing_body_greenbrown = instance_manager.get(get_resource_key(TRAIT_MECHANICALSUIT_WEARING_BODY_GREENBROWN, Types.TRAIT))
    if sim.has_trait(trait_mechanicalsuit_wearing_body_greenbrown):
        sim.remove_trait(trait_mechanicalsuit_wearing_body_greenbrown)

    trait_mechanicalsuit_wearing_body_redgreen = instance_manager.get(get_resource_key(TRAIT_MECHANICALSUIT_WEARING_BODY_REDGREEN, Types.TRAIT))
    if sim.has_trait(trait_mechanicalsuit_wearing_body_redgreen):
        sim.remove_trait(trait_mechanicalsuit_wearing_body_redgreen)

    trait_mechanicalsuit_wearing_body_whitecopper = instance_manager.get(get_resource_key(TRAIT_MECHANICALSUIT_WEARING_BODY_WHITECOPPER, Types.TRAIT))
    if sim.has_trait(trait_mechanicalsuit_wearing_body_whitecopper):
        sim.remove_trait(trait_mechanicalsuit_wearing_body_whitecopper)

    trait_mechanicalsuit_wearing_helmet_blackblue = instance_manager.get(get_resource_key(TRAIT_MECHANICALSUIT_WEARING_HELMET_BLACKBLUE, Types.TRAIT))
    if sim.has_trait(trait_mechanicalsuit_wearing_helmet_blackblue):
        sim.remove_trait(trait_mechanicalsuit_wearing_helmet_blackblue)

    trait_mechanicalsuit_wearing_helmet_blackcopper = instance_manager.get(get_resource_key(TRAIT_MECHANICALSUIT_WEARING_HELMET_BLACKCOPPER, Types.TRAIT))
    if sim.has_trait(trait_mechanicalsuit_wearing_helmet_blackcopper):
        sim.remove_trait(trait_mechanicalsuit_wearing_helmet_blackcopper)

    trait_mechanicalsuit_wearing_helmet_blackgold = instance_manager.get(get_resource_key(TRAIT_MECHANICALSUIT_WEARING_HELMET_BLACKGOLD, Types.TRAIT))
    if sim.has_trait(trait_mechanicalsuit_wearing_helmet_blackgold):
        sim.remove_trait(trait_mechanicalsuit_wearing_helmet_blackgold)

    trait_mechanicalsuit_wearing_helmet_blackgray = instance_manager.get(get_resource_key(TRAIT_MECHANICALSUIT_WEARING_HELMET_BLACKGRAY, Types.TRAIT))
    if sim.has_trait(trait_mechanicalsuit_wearing_helmet_blackgray):
        sim.remove_trait(trait_mechanicalsuit_wearing_helmet_blackgray)

    trait_mechanicalsuit_wearing_helmet_bluegray = instance_manager.get(get_resource_key(TRAIT_MECHANICALSUIT_WEARING_HELMET_BLUEGRAY, Types.TRAIT))
    if sim.has_trait(trait_mechanicalsuit_wearing_helmet_bluegray):
        sim.remove_trait(trait_mechanicalsuit_wearing_helmet_bluegray)

    trait_mechanicalsuit_wearing_helmet_grayblack = instance_manager.get(get_resource_key(TRAIT_MECHANICALSUIT_WEARING_HELMET_GRAYBLACK, Types.TRAIT))
    if sim.has_trait(trait_mechanicalsuit_wearing_helmet_grayblack):
        sim.remove_trait(trait_mechanicalsuit_wearing_helmet_grayblack)

    trait_mechanicalsuit_wearing_helmet_greenblack = instance_manager.get(get_resource_key(TRAIT_MECHANICALSUIT_WEARING_HELMET_GREENBLACK, Types.TRAIT))
    if sim.has_trait(trait_mechanicalsuit_wearing_helmet_greenblack):
        sim.remove_trait(trait_mechanicalsuit_wearing_helmet_greenblack)

    trait_nightowl_crystalhelmet = instance_manager.get(get_resource_key(TRAIT_NIGHTOWL_CRYSTALHELMET, Types.TRAIT))
    if sim.has_trait(trait_nightowl_crystalhelmet):
        sim.remove_trait(trait_nightowl_crystalhelmet)

    trait_roboticsarm_wearing_beigewhite = instance_manager.get(get_resource_key(TRAIT_ROBOTICSARM_WEARING_BEIGEWHITE, Types.TRAIT))
    if sim.has_trait(trait_roboticsarm_wearing_beigewhite):
        sim.remove_trait(trait_roboticsarm_wearing_beigewhite)

    trait_roboticsarm_wearing_blackblue = instance_manager.get(get_resource_key(TRAIT_ROBOTICSARM_WEARING_BLACKBLUE, Types.TRAIT))
    if sim.has_trait(trait_roboticsarm_wearing_blackblue):
        sim.remove_trait(trait_roboticsarm_wearing_blackblue)

    trait_roboticsarm_wearing_bluered = instance_manager.get(get_resource_key(TRAIT_ROBOTICSARM_WEARING_BLUERED, Types.TRAIT))
    if sim.has_trait(trait_roboticsarm_wearing_bluered):
        sim.remove_trait(trait_roboticsarm_wearing_bluered)

    trait_roboticsarm_wearing_graybrown = instance_manager.get(get_resource_key(TRAIT_ROBOTICSARM_WEARING_GRAYBROWN, Types.TRAIT))
    if sim.has_trait(trait_roboticsarm_wearing_graybrown):
        sim.remove_trait(trait_roboticsarm_wearing_graybrown)

    trait_roboticsarm_wearing_greenbrown = instance_manager.get(get_resource_key(TRAIT_ROBOTICSARM_WEARING_GREENBROWN, Types.TRAIT))
    if sim.has_trait(trait_roboticsarm_wearing_greenbrown):
        sim.remove_trait(trait_roboticsarm_wearing_greenbrown)

    trait_roboticsarm_wearing_redgreen = instance_manager.get(get_resource_key(TRAIT_ROBOTICSARM_WEARING_REDGREEN, Types.TRAIT))
    if sim.has_trait(trait_roboticsarm_wearing_redgreen):
        sim.remove_trait(trait_roboticsarm_wearing_redgreen)

    trait_roboticsarm_wearing_whitecopper = instance_manager.get(get_resource_key(TRAIT_ROBOTICSARM_WEARING_WHITECOPPER, Types.TRAIT))
    if sim.has_trait(trait_roboticsarm_wearing_whitecopper):
        sim.remove_trait(trait_roboticsarm_wearing_whitecopper)

    trait_selfassured = instance_manager.get(get_resource_key(TRAIT_SELFASSURED, Types.TRAIT))
    if not sim.has_trait(trait_selfassured):
        sim.add_trait(trait_selfassured)

    trait_sexualorientation_woohoointerests_female = instance_manager.get(get_resource_key(TRAIT_SEXUALORIENTATION_WOOHOOINTERESTS_FEMALE, Types.TRAIT))
    if not sim.has_trait(trait_sexualorientation_woohoointerests_female):
        sim.add_trait(trait_sexualorientation_woohoointerests_female)

    trait_sexualorientation_woohoointerests_male = instance_manager.get(get_resource_key(TRAIT_SEXUALORIENTATION_WOOHOOINTERESTS_MALE, Types.TRAIT))
    if not sim.has_trait(trait_sexualorientation_woohoointerests_male):
        sim.add_trait(trait_sexualorientation_woohoointerests_male)

    trait_sexualorientation_woohoointerests_notfemale = instance_manager.get(get_resource_key(TRAIT_SEXUALORIENTATION_WOOHOOINTERESTS_NOTFEMALE, Types.TRAIT))
    if sim.has_trait(trait_sexualorientation_woohoointerests_notfemale):
        sim.remove_trait(trait_sexualorientation_woohoointerests_notfemale)

    trait_simpreference_dislikes_activities_djmixing = instance_manager.get(get_resource_key(TRAIT_SIMPREFERENCE_DISLIKES_ACTIVITIES_DJMIXING, Types.TRAIT))
    if sim.has_trait(trait_simpreference_dislikes_activities_djmixing):
        sim.remove_trait(trait_simpreference_dislikes_activities_djmixing)

    trait_simpreference_dislikes_activities_fitness = instance_manager.get(get_resource_key(TRAIT_SIMPREFERENCE_DISLIKES_ACTIVITIES_FITNESS, Types.TRAIT))
    if sim.has_trait(trait_simpreference_dislikes_activities_fitness):
        sim.remove_trait(trait_simpreference_dislikes_activities_fitness)

    trait_simpreference_dislikes_activities_guitar = instance_manager.get(get_resource_key(TRAIT_SIMPREFERENCE_DISLIKES_ACTIVITIES_GUITAR, Types.TRAIT))
    if sim.has_trait(trait_simpreference_dislikes_activities_guitar):
        sim.remove_trait(trait_simpreference_dislikes_activities_guitar)

    trait_simpreference_dislikes_activities_piano = instance_manager.get(get_resource_key(TRAIT_SIMPREFERENCE_DISLIKES_ACTIVITIES_PIANO, Types.TRAIT))
    if sim.has_trait(trait_simpreference_dislikes_activities_piano):
        sim.remove_trait(trait_simpreference_dislikes_activities_piano)

    trait_simpreference_dislikes_activities_pipeorgan = instance_manager.get(get_resource_key(TRAIT_SIMPREFERENCE_DISLIKES_ACTIVITIES_PIPEORGAN, Types.TRAIT))
    if sim.has_trait(trait_simpreference_dislikes_activities_pipeorgan):
        sim.remove_trait(trait_simpreference_dislikes_activities_pipeorgan)

    trait_simpreference_dislikes_activities_programming = instance_manager.get(get_resource_key(TRAIT_SIMPREFERENCE_DISLIKES_ACTIVITIES_PROGRAMMING, Types.TRAIT))
    if sim.has_trait(trait_simpreference_dislikes_activities_programming):
        sim.remove_trait(trait_simpreference_dislikes_activities_programming)

    trait_simpreference_dislikes_activities_rockclimbing = instance_manager.get(get_resource_key(TRAIT_SIMPREFERENCE_DISLIKES_ACTIVITIES_ROCKCLIMBING, Types.TRAIT))
    if sim.has_trait(trait_simpreference_dislikes_activities_rockclimbing):
        sim.remove_trait(trait_simpreference_dislikes_activities_rockclimbing)

    trait_simpreference_dislikes_activities_singing = instance_manager.get(get_resource_key(TRAIT_SIMPREFERENCE_DISLIKES_ACTIVITIES_SINGING, Types.TRAIT))
    if sim.has_trait(trait_simpreference_dislikes_activities_singing):
        sim.remove_trait(trait_simpreference_dislikes_activities_singing)

    trait_simpreference_dislikes_activities_violin = instance_manager.get(get_resource_key(TRAIT_SIMPREFERENCE_DISLIKES_ACTIVITIES_VIOLIN, Types.TRAIT))
    if sim.has_trait(trait_simpreference_dislikes_activities_violin):
        sim.remove_trait(trait_simpreference_dislikes_activities_violin)

    trait_simpreference_dislikes_activities_wellness = instance_manager.get(get_resource_key(TRAIT_SIMPREFERENCE_DISLIKES_ACTIVITIES_WELLNESS, Types.TRAIT))
    if sim.has_trait(trait_simpreference_dislikes_activities_wellness):
        sim.remove_trait(trait_simpreference_dislikes_activities_wellness)

    trait_simpreference_dislikes_activities_writing = instance_manager.get(get_resource_key(TRAIT_SIMPREFERENCE_DISLIKES_ACTIVITIES_WRITING, Types.TRAIT))
    if sim.has_trait(trait_simpreference_dislikes_activities_writing):
        sim.remove_trait(trait_simpreference_dislikes_activities_writing)

    trait_simpreference_likes_activities_fitness = instance_manager.get(get_resource_key(TRAIT_SIMPREFERENCE_LIKES_ACTIVITIES_FITNESS, Types.TRAIT))
    if not sim.has_trait(trait_simpreference_likes_activities_fitness):
        sim.add_trait(trait_simpreference_likes_activities_fitness)

    trait_simpreference_likes_activities_wellness = instance_manager.get(get_resource_key(TRAIT_SIMPREFERENCE_LIKES_ACTIVITIES_WELLNESS, Types.TRAIT))
    if not sim.has_trait(trait_simpreference_likes_activities_wellness):
        sim.add_trait(trait_simpreference_likes_activities_wellness)

    trait_simpreference_noopinion_activities_fitness = instance_manager.get(get_resource_key(TRAIT_SIMPREFERENCE_NOOPINION_ACTIVITIES_FITNESS, Types.TRAIT))
    if sim.has_trait(trait_simpreference_noopinion_activities_fitness):
        sim.remove_trait(trait_simpreference_noopinion_activities_fitness)

    trait_simpreference_noopinion_activities_wellness = instance_manager.get(get_resource_key(TRAIT_SIMPREFERENCE_NOOPINION_ACTIVITIES_WELLNESS, Types.TRAIT))
    if sim.has_trait(trait_simpreference_noopinion_activities_wellness):
        sim.remove_trait(trait_simpreference_noopinion_activities_wellness)

    trait_slob = instance_manager.get(get_resource_key(TRAIT_SLOB, Types.TRAIT))
    if sim.has_trait(trait_slob):
        sim.remove_trait(trait_slob)

    trait_speedcleaner = instance_manager.get(get_resource_key(TRAIT_SPEEDCLEANER, Types.TRAIT))
    if not sim.has_trait(trait_speedcleaner):
        sim.add_trait(trait_speedcleaner)

    trait_speedreader = instance_manager.get(get_resource_key(TRAIT_SPEEDREADER, Types.TRAIT))
    if sim.has_trait(trait_speedreader):
        sim.remove_trait(trait_speedreader)

    trait_stormchaser = instance_manager.get(get_resource_key(TRAIT_STORMCHASER, Types.TRAIT))
    if not sim.has_trait(trait_stormchaser):
        sim.add_trait(trait_stormchaser)

    trait_temperature_burningman = instance_manager.get(get_resource_key(TRAIT_TEMPERATURE_BURNINGMAN, Types.TRAIT))
    if not sim.has_trait(trait_temperature_burningman):
        sim.add_trait(trait_temperature_burningman)

    trait_temperature_coldacclimation = instance_manager.get(get_resource_key(TRAIT_TEMPERATURE_COLDACCLIMATION, Types.TRAIT))
    if sim.has_trait(trait_temperature_coldacclimation):
        sim.remove_trait(trait_temperature_coldacclimation)

    trait_temperature_heatacclimation = instance_manager.get(get_resource_key(TRAIT_TEMPERATURE_HEATACCLIMATION, Types.TRAIT))
    if sim.has_trait(trait_temperature_heatacclimation):
        sim.remove_trait(trait_temperature_heatacclimation)

    trait_temperature_iceman = instance_manager.get(get_resource_key(TRAIT_TEMPERATURE_ICEMAN, Types.TRAIT))
    if not sim.has_trait(trait_temperature_iceman):
        sim.add_trait(trait_temperature_iceman)

    trait_theknack = instance_manager.get(get_resource_key(TRAIT_THEKNACK, Types.TRAIT))
    if not sim.has_trait(trait_theknack):
        sim.add_trait(trait_theknack)

    trait_university_arthistorydegreeba = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_ARTHISTORYDEGREEBA, Types.TRAIT))
    if sim.has_trait(trait_university_arthistorydegreeba):
        sim.remove_trait(trait_university_arthistorydegreeba)

    trait_university_arthistorydegreebs = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_ARTHISTORYDEGREEBS, Types.TRAIT))
    if sim.has_trait(trait_university_arthistorydegreebs):
        sim.remove_trait(trait_university_arthistorydegreebs)

    trait_university_biologydegreeba = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_BIOLOGYDEGREEBA, Types.TRAIT))
    if sim.has_trait(trait_university_biologydegreeba):
        sim.remove_trait(trait_university_biologydegreeba)

    trait_university_biologydegreebs = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_BIOLOGYDEGREEBS, Types.TRAIT))
    if sim.has_trait(trait_university_biologydegreebs):
        sim.remove_trait(trait_university_biologydegreebs)

    trait_university_communicationsdegreeba = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_COMMUNICATIONSDEGREEBA, Types.TRAIT))
    if sim.has_trait(trait_university_communicationsdegreeba):
        sim.remove_trait(trait_university_communicationsdegreeba)

    trait_university_communicationsdegreebs = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_COMMUNICATIONSDEGREEBS, Types.TRAIT))
    if sim.has_trait(trait_university_communicationsdegreebs):
        sim.remove_trait(trait_university_communicationsdegreebs)

    trait_university_computersciencedegreeba = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_COMPUTERSCIENCEDEGREEBA, Types.TRAIT))
    if sim.has_trait(trait_university_computersciencedegreeba):
        sim.remove_trait(trait_university_computersciencedegreeba)

    trait_university_computersciencedegreebs = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_COMPUTERSCIENCEDEGREEBS, Types.TRAIT))
    if sim.has_trait(trait_university_computersciencedegreebs):
        sim.remove_trait(trait_university_computersciencedegreebs)

    trait_university_culinaryartsdegreeba = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_CULINARYARTSDEGREEBA, Types.TRAIT))
    if sim.has_trait(trait_university_culinaryartsdegreeba):
        sim.remove_trait(trait_university_culinaryartsdegreeba)

    trait_university_culinaryartsdegreebs = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_CULINARYARTSDEGREEBS, Types.TRAIT))
    if sim.has_trait(trait_university_culinaryartsdegreebs):
        sim.remove_trait(trait_university_culinaryartsdegreebs)

    trait_university_dramadegreeba = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_DRAMADEGREEBA, Types.TRAIT))
    if sim.has_trait(trait_university_dramadegreeba):
        sim.remove_trait(trait_university_dramadegreeba)

    trait_university_dramadegreebs = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_DRAMADEGREEBS, Types.TRAIT))
    if sim.has_trait(trait_university_dramadegreebs):
        sim.remove_trait(trait_university_dramadegreebs)

    trait_university_economicsdegreeba = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_ECONOMICSDEGREEBA, Types.TRAIT))
    if sim.has_trait(trait_university_economicsdegreeba):
        sim.remove_trait(trait_university_economicsdegreeba)

    trait_university_economicsdegreebs = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_ECONOMICSDEGREEBS, Types.TRAIT))
    if sim.has_trait(trait_university_economicsdegreebs):
        sim.remove_trait(trait_university_economicsdegreebs)

    trait_university_fineartdegreeba = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_FINEARTDEGREEBA, Types.TRAIT))
    if sim.has_trait(trait_university_fineartdegreeba):
        sim.remove_trait(trait_university_fineartdegreeba)

    trait_university_fineartdegreebs = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_FINEARTDEGREEBS, Types.TRAIT))
    if sim.has_trait(trait_university_fineartdegreebs):
        sim.remove_trait(trait_university_fineartdegreebs)

    trait_university_historydegreeba = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_HISTORYDEGREEBA, Types.TRAIT))
    if sim.has_trait(trait_university_historydegreeba):
        sim.remove_trait(trait_university_historydegreeba)

    trait_university_historydegreebs = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_HISTORYDEGREEBS, Types.TRAIT))
    if sim.has_trait(trait_university_historydegreebs):
        sim.remove_trait(trait_university_historydegreebs)

    trait_university_languageandliteraturedegreeba = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_LANGUAGEANDLITERATUREDEGREEBA, Types.TRAIT))
    if sim.has_trait(trait_university_languageandliteraturedegreeba):
        sim.remove_trait(trait_university_languageandliteraturedegreeba)

    trait_university_languageandliteraturedegreebs = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_LANGUAGEANDLITERATUREDEGREEBS, Types.TRAIT))
    if sim.has_trait(trait_university_languageandliteraturedegreebs):
        sim.remove_trait(trait_university_languageandliteraturedegreebs)

    trait_university_physicsdegreeba = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_PHYSICSDEGREEBA, Types.TRAIT))
    if sim.has_trait(trait_university_physicsdegreeba):
        sim.remove_trait(trait_university_physicsdegreeba)

    trait_university_physicsdegreebs = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_PHYSICSDEGREEBS, Types.TRAIT))
    if sim.has_trait(trait_university_physicsdegreebs):
        sim.remove_trait(trait_university_physicsdegreebs)

    trait_university_psychologydegreeba = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_PSYCHOLOGYDEGREEBA, Types.TRAIT))
    if sim.has_trait(trait_university_psychologydegreeba):
        sim.remove_trait(trait_university_psychologydegreeba)

    trait_university_psychologydegreebs = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_PSYCHOLOGYDEGREEBS, Types.TRAIT))
    if sim.has_trait(trait_university_psychologydegreebs):
        sim.remove_trait(trait_university_psychologydegreebs)

    trait_university_villainydegreeba = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_VILLAINYDEGREEBA, Types.TRAIT))
    if sim.has_trait(trait_university_villainydegreeba):
        sim.remove_trait(trait_university_villainydegreeba)

    trait_university_villainydegreebs = instance_manager.get(get_resource_key(TRAIT_UNIVERSITY_VILLAINYDEGREEBS, Types.TRAIT))
    if sim.has_trait(trait_university_villainydegreebs):
        sim.remove_trait(trait_university_villainydegreebs)

    trait_walkstylecreepy = instance_manager.get(get_resource_key(TRAIT_WALKSTYLECREEPY, Types.TRAIT))
    if sim.has_trait(trait_walkstylecreepy):
        sim.remove_trait(trait_walkstylecreepy)

    trait_walkstyleenergetic = instance_manager.get(get_resource_key(TRAIT_WALKSTYLEENERGETIC, Types.TRAIT))
    if sim.has_trait(trait_walkstyleenergetic):
        sim.remove_trait(trait_walkstyleenergetic)

    trait_walkstyleenergetic = instance_manager.get(get_resource_key(TRAIT_WALKSTYLEENERGETIC, Types.TRAIT))
    if sim.has_trait(trait_walkstyleenergetic):
        sim.remove_trait(trait_walkstyleenergetic)

    trait_walkstylegoofy = instance_manager.get(get_resource_key(TRAIT_WALKSTYLEGOOFY, Types.TRAIT))
    if sim.has_trait(trait_walkstylegoofy):
        sim.remove_trait(trait_walkstylegoofy)

    trait_walkstyleperky = instance_manager.get(get_resource_key(TRAIT_WALKSTYLEPERKY, Types.TRAIT))
    if sim.has_trait(trait_walkstyleperky):
        sim.remove_trait(trait_walkstyleperky)

    trait_walkstylesleepy = instance_manager.get(get_resource_key(TRAIT_WALKSTYLESLEEPY, Types.TRAIT))
    if sim.has_trait(trait_walkstylesleepy):
        sim.remove_trait(trait_walkstylesleepy)

    trait_walkstylesnooty = instance_manager.get(get_resource_key(TRAIT_WALKSTYLESNOOTY, Types.TRAIT))
    if sim.has_trait(trait_walkstylesnooty):
        sim.remove_trait(trait_walkstylesnooty)

    trait_walkstyleswagger = instance_manager.get(get_resource_key(TRAIT_WALKSTYLESWAGGER, Types.TRAIT))
    if sim.has_trait(trait_walkstyleswagger):
        sim.remove_trait(trait_walkstyleswagger)

    trait_walkstyletough = instance_manager.get(get_resource_key(TRAIT_WALKSTYLETOUGH, Types.TRAIT))
    if sim.has_trait(trait_walkstyletough):
        sim.remove_trait(trait_walkstyletough)

    trait_waterproof = instance_manager.get(get_resource_key(TRAIT_WATERPROOF, Types.TRAIT))
    if not sim.has_trait(trait_waterproof):
        sim.add_trait(trait_waterproof)

    trait_webmaster = instance_manager.get(get_resource_key(TRAIT_WEBMASTER, Types.TRAIT))
    if not sim.has_trait(trait_webmaster):
        sim.add_trait(trait_webmaster)

    wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_breastslarge = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_BODYSHAPE_BREASTSLARGE, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_breastslarge):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_breastslarge)

    wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_breastssmall = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_BODYSHAPE_BREASTSSMALL, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_breastssmall):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_breastssmall)

    wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_buttlarge = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_BODYSHAPE_BUTTLARGE, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_buttlarge):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_buttlarge)

    wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_buttsmall = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_BODYSHAPE_BUTTSMALL, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_buttsmall):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_buttsmall)

    wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_heavy = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_BODYSHAPE_HEAVY, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_heavy):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_heavy)

    wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_high = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_BODYSHAPE_HIGH, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_high):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_high)

    wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_light = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_BODYSHAPE_LIGHT, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_light):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_light)

    wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_low = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_BODYSHAPE_LOW, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_low):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_low)

    wickedwhims_attractiveness_trait_simpreference_dislikes_detail_body_hair = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_DETAIL_BODY_HAIR, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_detail_body_hair):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_detail_body_hair)

    wickedwhims_attractiveness_trait_simpreference_dislikes_detail_freckles = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_DETAIL_FRECKLES, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_detail_freckles):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_detail_freckles)

    wickedwhims_attractiveness_trait_simpreference_dislikes_detail_glasses = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_DETAIL_GLASSES, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_detail_glasses):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_detail_glasses)

    wickedwhims_attractiveness_trait_simpreference_dislikes_detail_hats = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_DETAIL_HATS, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_detail_hats):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_detail_hats)

    wickedwhims_attractiveness_trait_simpreference_dislikes_detail_jewelery = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_DETAIL_JEWELERY, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_detail_jewelery):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_detail_jewelery)

    wickedwhims_attractiveness_trait_simpreference_dislikes_detail_makeup = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_DETAIL_MAKEUP, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_detail_makeup):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_detail_makeup)

    wickedwhims_attractiveness_trait_simpreference_dislikes_detail_piercing = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_DETAIL_PIERCING, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_detail_piercing):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_detail_piercing)

    wickedwhims_attractiveness_trait_simpreference_dislikes_detail_tattoos = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_DETAIL_TATTOOS, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_detail_tattoos):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_detail_tattoos)

    wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_blue = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_EYECOLOR_BLUE, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_blue):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_blue)

    wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_blue = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_EYECOLOR_BLUE, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_blue):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_blue)

    wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_brown = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_EYECOLOR_BROWN, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_brown):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_brown)

    wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_brown = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_EYECOLOR_BROWN, Types.TRAIT))
    if not sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_brown):
        sim.add_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_brown)

    wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_green = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_EYECOLOR_GREEN, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_green):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_green)

    wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_green = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_EYECOLOR_GREEN, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_green):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_green)

    wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_unnatural = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_EYECOLOR_UNNATURAL, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_unnatural):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_eyecolor_unnatural)

    wickedwhims_attractiveness_trait_simpreference_dislikes_facialhair_beard = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_FACIALHAIR_BEARD, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_facialhair_beard):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_facialhair_beard)

    wickedwhims_attractiveness_trait_simpreference_dislikes_facialhair_clean = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_FACIALHAIR_CLEAN, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_facialhair_clean):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_facialhair_clean)

    wickedwhims_attractiveness_trait_simpreference_dislikes_facialhair_goatee = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_FACIALHAIR_GOATEE, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_facialhair_goatee):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_facialhair_goatee)

    wickedwhims_attractiveness_trait_simpreference_dislikes_facialhair_mustache = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_FACIALHAIR_MUSTACHE, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_facialhair_mustache):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_facialhair_mustache)

    wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_black = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_HAIRCOLOR_BLACK, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_black):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_black)

    wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_blonde = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_HAIRCOLOR_BLONDE, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_blonde):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_blonde)

    wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_blonde = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_HAIRCOLOR_BLONDE, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_blonde):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_blonde)

    wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_blue = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_HAIRCOLOR_BLUE, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_blue):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_blue)

    wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_blue = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_HAIRCOLOR_BLUE, Types.TRAIT))
    if not sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_blue):
        sim.add_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_blue)

    wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_brown = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_HAIRCOLOR_BROWN, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_brown):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_brown)

    wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_brown = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_HAIRCOLOR_BROWN, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_brown):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_brown)

    wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_gray = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_HAIRCOLOR_GRAY, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_gray):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_gray)

    wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_green = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_HAIRCOLOR_GREEN, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_green):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_green)

    wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_green = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_HAIRCOLOR_GREEN, Types.TRAIT))
    if not sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_green):
        sim.add_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_green)

    wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_pink = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_HAIRCOLOR_PINK, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_pink):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_pink)

    wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_red = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_HAIRCOLOR_RED, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_red):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_red)

    wickedwhims_attractiveness_trait_simpreference_dislikes_hairlength_bald = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_HAIRLENGTH_BALD, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_hairlength_bald):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_hairlength_bald)

    wickedwhims_attractiveness_trait_simpreference_dislikes_hairlength_bald = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_HAIRLENGTH_BALD, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_hairlength_bald):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_hairlength_bald)

    wickedwhims_attractiveness_trait_simpreference_dislikes_hairlength_long = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_HAIRLENGTH_LONG, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_hairlength_long):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_hairlength_long)

    wickedwhims_attractiveness_trait_simpreference_dislikes_hairlength_medium = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_HAIRLENGTH_MEDIUM, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_hairlength_medium):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_hairlength_medium)

    wickedwhims_attractiveness_trait_simpreference_dislikes_hairlength_short = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_HAIRLENGTH_SHORT, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_hairlength_short):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_hairlength_short)

    wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_breastslarge = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_BODYSHAPE_BREASTSLARGE, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_breastslarge):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_breastslarge)

    wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_breastssmall = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_BODYSHAPE_BREASTSSMALL, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_breastssmall):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_breastssmall)

    wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_breastssmall = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_BODYSHAPE_BREASTSSMALL, Types.TRAIT))
    if not sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_breastssmall):
        sim.add_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_breastssmall)

    wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_buttlarge = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_BODYSHAPE_BUTTLARGE, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_buttlarge):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_buttlarge)

    wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_buttlarge = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_BODYSHAPE_BUTTLARGE, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_buttlarge):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_buttlarge)

    wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_buttsmall = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_BODYSHAPE_BUTTSMALL, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_buttsmall):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_buttsmall)

    wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_buttsmall = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_BODYSHAPE_BUTTSMALL, Types.TRAIT))
    if not sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_buttsmall):
        sim.add_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_buttsmall)

    wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_heavy = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_BODYSHAPE_HEAVY, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_heavy):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_heavy)

    wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_high = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_BODYSHAPE_HIGH, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_high):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_high)

    wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_light = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_BODYSHAPE_LIGHT, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_light):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_light)

    wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_low = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_BODYSHAPE_LOW, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_low):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_low)

    wickedwhims_attractiveness_trait_simpreference_likes_detail_body_hair = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_DETAIL_BODY_HAIR, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_body_hair):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_body_hair)

    wickedwhims_attractiveness_trait_simpreference_likes_detail_freckles = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_DETAIL_FRECKLES, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_freckles):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_freckles)

    wickedwhims_attractiveness_trait_simpreference_likes_detail_glasses = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_DETAIL_GLASSES, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_glasses):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_glasses)

    wickedwhims_attractiveness_trait_simpreference_likes_detail_glasses = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_DETAIL_GLASSES, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_glasses):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_glasses)

    wickedwhims_attractiveness_trait_simpreference_likes_detail_hats = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_DETAIL_HATS, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_hats):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_hats)

    wickedwhims_attractiveness_trait_simpreference_likes_detail_hats = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_DETAIL_HATS, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_hats):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_hats)

    wickedwhims_attractiveness_trait_simpreference_likes_detail_jewelery = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_DETAIL_JEWELERY, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_jewelery):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_jewelery)

    wickedwhims_attractiveness_trait_simpreference_likes_detail_makeup = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_DETAIL_MAKEUP, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_makeup):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_makeup)

    wickedwhims_attractiveness_trait_simpreference_likes_detail_piercing = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_DETAIL_PIERCING, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_piercing):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_piercing)

    wickedwhims_attractiveness_trait_simpreference_likes_detail_tattoos = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_DETAIL_TATTOOS, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_tattoos):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_tattoos)

    wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_blue = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_EYECOLOR_BLUE, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_blue):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_blue)

    wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_blue = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_EYECOLOR_BLUE, Types.TRAIT))
    if not sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_blue):
        sim.add_trait(wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_blue)

    wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_brown = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_EYECOLOR_BROWN, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_brown):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_brown)

    wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_brown = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_EYECOLOR_BROWN, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_brown):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_brown)

    wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_green = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_EYECOLOR_GREEN, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_green):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_green)

    wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_green = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_EYECOLOR_GREEN, Types.TRAIT))
    if not sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_green):
        sim.add_trait(wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_green)

    wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_unnatural = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_EYECOLOR_UNNATURAL, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_unnatural):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_eyecolor_unnatural)

    wickedwhims_attractiveness_trait_simpreference_likes_facialhair_beard = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_FACIALHAIR_BEARD, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_facialhair_beard):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_facialhair_beard)

    wickedwhims_attractiveness_trait_simpreference_likes_facialhair_clean = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_FACIALHAIR_CLEAN, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_facialhair_clean):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_facialhair_clean)

    wickedwhims_attractiveness_trait_simpreference_likes_facialhair_goatee = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_FACIALHAIR_GOATEE, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_facialhair_goatee):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_facialhair_goatee)

    wickedwhims_attractiveness_trait_simpreference_likes_facialhair_mustache = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_FACIALHAIR_MUSTACHE, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_facialhair_mustache):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_facialhair_mustache)

    wickedwhims_attractiveness_trait_simpreference_likes_haircolor_black = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_HAIRCOLOR_BLACK, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_black):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_black)

    wickedwhims_attractiveness_trait_simpreference_likes_haircolor_blonde = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_HAIRCOLOR_BLONDE, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_blonde):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_blonde)

    wickedwhims_attractiveness_trait_simpreference_likes_haircolor_blonde = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_HAIRCOLOR_BLONDE, Types.TRAIT))
    if not sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_blonde):
        sim.add_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_blonde)

    wickedwhims_attractiveness_trait_simpreference_likes_haircolor_blue = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_HAIRCOLOR_BLUE, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_blue):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_blue)

    wickedwhims_attractiveness_trait_simpreference_likes_haircolor_brown = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_HAIRCOLOR_BROWN, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_brown):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_brown)

    wickedwhims_attractiveness_trait_simpreference_likes_haircolor_brown = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_HAIRCOLOR_BROWN, Types.TRAIT))
    if not sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_brown):
        sim.add_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_brown)

    wickedwhims_attractiveness_trait_simpreference_likes_haircolor_gray = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_HAIRCOLOR_GRAY, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_gray):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_gray)

    wickedwhims_attractiveness_trait_simpreference_likes_haircolor_green = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_HAIRCOLOR_GREEN, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_green):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_green)

    wickedwhims_attractiveness_trait_simpreference_likes_haircolor_pink = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_HAIRCOLOR_PINK, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_pink):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_pink)

    wickedwhims_attractiveness_trait_simpreference_likes_haircolor_red = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_HAIRCOLOR_RED, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_red):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_haircolor_red)

    wickedwhims_attractiveness_trait_simpreference_likes_hairlength_bald = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_HAIRLENGTH_BALD, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_hairlength_bald):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_hairlength_bald)

    wickedwhims_attractiveness_trait_simpreference_likes_hairlength_long = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_HAIRLENGTH_LONG, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_hairlength_long):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_hairlength_long)

    wickedwhims_attractiveness_trait_simpreference_likes_hairlength_medium = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_HAIRLENGTH_MEDIUM, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_hairlength_medium):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_hairlength_medium)

    wickedwhims_attractiveness_trait_simpreference_likes_hairlength_short = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_HAIRLENGTH_SHORT, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_hairlength_short):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_likes_hairlength_short)

    wickedwhims_trait_attractivenessblacklist = instance_manager.get(get_resource_key(WICKEDWHIMS_TRAIT_ATTRACTIVENESSBLACKLIST, Types.TRAIT))
    if sim.has_trait(wickedwhims_trait_attractivenessblacklist):
        sim.remove_trait(wickedwhims_trait_attractivenessblacklist)

    wickedwhims_trait_bodyhair_pubichair_isdisabled = instance_manager.get(get_resource_key(WICKEDWHIMS_TRAIT_BODYHAIR_PUBICHAIR_ISDISABLED, Types.TRAIT))
    if not sim.has_trait(wickedwhims_trait_bodyhair_pubichair_isdisabled):
        sim.add_trait(wickedwhims_trait_bodyhair_pubichair_isdisabled)

    wickedwhims_trait_bodyhair_pubichair_isgrowthdisabled = instance_manager.get(get_resource_key(WICKEDWHIMS_TRAIT_BODYHAIR_PUBICHAIR_ISGROWTHDISABLED, Types.TRAIT))
    if not sim.has_trait(wickedwhims_trait_bodyhair_pubichair_isgrowthdisabled):
        sim.add_trait(wickedwhims_trait_bodyhair_pubichair_isgrowthdisabled)

    wickedwhims_trait_cumslut = instance_manager.get(get_resource_key(WICKEDWHIMS_TRAIT_CUMSLUT, Types.TRAIT))
    if not sim.has_trait(wickedwhims_trait_cumslut):
        sim.add_trait(wickedwhims_trait_cumslut)

    wickedwhims_trait_improved_absorbency = instance_manager.get(get_resource_key(WICKEDWHIMS_TRAIT_IMPROVED_ABSORBENCY, Types.TRAIT))
    if not sim.has_trait(wickedwhims_trait_improved_absorbency):
        sim.add_trait(wickedwhims_trait_improved_absorbency)

    wickedwhims_trait_postpubertyteen = instance_manager.get(get_resource_key(WICKEDWHIMS_TRAIT_POSTPUBERTYTEEN, Types.TRAIT))
    if not sim.has_trait(wickedwhims_trait_postpubertyteen):
        sim.add_trait(wickedwhims_trait_postpubertyteen)

    wickedwhims_trait_sex_attribute_badatsex = instance_manager.get(get_resource_key(WICKEDWHIMS_TRAIT_SEX_ATTRIBUTE_BADATSEX, Types.TRAIT))
    if sim.has_trait(wickedwhims_trait_sex_attribute_badatsex):
        sim.remove_trait(wickedwhims_trait_sex_attribute_badatsex)

    wickedwhims_trait_sex_sexuallyabstinent = instance_manager.get(get_resource_key(WICKEDWHIMS_TRAIT_SEX_SEXUALLYABSTINENT, Types.TRAIT))
    if sim.has_trait(wickedwhims_trait_sex_sexuallyabstinent):
        sim.remove_trait(wickedwhims_trait_sex_sexuallyabstinent)


    # Remove or add traits from service sims
    trait_dastardly = instance_manager.get(get_resource_key(TRAIT_DASTARDLY, Types.TRAIT))
    if sim.has_trait(trait_dastardly):
        sim.remove_trait(trait_dastardly)

    trait_evil = instance_manager.get(get_resource_key(TRAIT_EVIL, Types.TRAIT))
    if sim.has_trait(trait_evil):
        sim.remove_trait(trait_evil)

    trait_genderoptions_attractedto_female = instance_manager.get(get_resource_key(TRAIT_GENDEROPTIONS_ATTRACTEDTO_FEMALE, Types.TRAIT))
    if not sim.has_trait(trait_genderoptions_attractedto_female):
        sim.add_trait(trait_genderoptions_attractedto_female)

    trait_genderoptions_attractedto_male = instance_manager.get(get_resource_key(TRAIT_GENDEROPTIONS_ATTRACTEDTO_MALE, Types.TRAIT))
    if not sim.has_trait(trait_genderoptions_attractedto_male):
        sim.add_trait(trait_genderoptions_attractedto_male)

    trait_genderoptions_clothing_womenswear = instance_manager.get(get_resource_key(TRAIT_GENDEROPTIONS_CLOTHING_WOMENSWEAR, Types.TRAIT))
    if not sim.has_trait(trait_genderoptions_clothing_womenswear):
        sim.add_trait(trait_genderoptions_clothing_womenswear)

    trait_genderoptions_frame_feminine = instance_manager.get(get_resource_key(TRAIT_GENDEROPTIONS_FRAME_FEMININE, Types.TRAIT))
    if not sim.has_trait(trait_genderoptions_frame_feminine):
        sim.add_trait(trait_genderoptions_frame_feminine)

    trait_genderoptions_frame_masculine = instance_manager.get(get_resource_key(TRAIT_GENDEROPTIONS_FRAME_MASCULINE, Types.TRAIT))
    if sim.has_trait(trait_genderoptions_frame_masculine):
        sim.remove_trait(trait_genderoptions_frame_masculine)

    trait_genderoptions_pregnancy_canbeimpregnated = instance_manager.get(get_resource_key(TRAIT_GENDEROPTIONS_PREGNANCY_CANBEIMPREGNATED, Types.TRAIT))
    if not sim.has_trait(trait_genderoptions_pregnancy_canbeimpregnated):
        sim.add_trait(trait_genderoptions_pregnancy_canbeimpregnated)

    trait_genderoptions_pregnancy_cannotimpregnate = instance_manager.get(get_resource_key(TRAIT_GENDEROPTIONS_PREGNANCY_CANNOTIMPREGNATE, Types.TRAIT))
    if not sim.has_trait(trait_genderoptions_pregnancy_cannotimpregnate):
        sim.add_trait(trait_genderoptions_pregnancy_cannotimpregnate)

    trait_gloomy = instance_manager.get(get_resource_key(TRAIT_GLOOMY, Types.TRAIT))
    if sim.has_trait(trait_gloomy):
        sim.remove_trait(trait_gloomy)

    trait_hsexit_earnedged = instance_manager.get(get_resource_key(TRAIT_HSEXIT_EARNEDGED, Types.TRAIT))
    if not sim.has_trait(trait_hsexit_earnedged):
        sim.add_trait(trait_hsexit_earnedged)

    trait_jealous = instance_manager.get(get_resource_key(TRAIT_JEALOUS, Types.TRAIT))
    if sim.has_trait(trait_jealous):
        sim.remove_trait(trait_jealous)

    trait_kleptomaniac = instance_manager.get(get_resource_key(TRAIT_KLEPTOMANIAC, Types.TRAIT))
    if sim.has_trait(trait_kleptomaniac):
        sim.remove_trait(trait_kleptomaniac)

    trait_neat = instance_manager.get(get_resource_key(TRAIT_NEAT, Types.TRAIT))
    if not sim.has_trait(trait_neat):
        sim.add_trait(trait_neat)

    trait_proper = instance_manager.get(get_resource_key(TRAIT_PROPER, Types.TRAIT))
    if not sim.has_trait(trait_proper):
        sim.add_trait(trait_proper)

    trait_shameless = instance_manager.get(get_resource_key(TRAIT_SHAMELESS, Types.TRAIT))
    if not sim.has_trait(trait_shameless):
        sim.add_trait(trait_shameless)

    trait_sicknessimmunity = instance_manager.get(get_resource_key(TRAIT_SICKNESSIMMUNITY, Types.TRAIT))
    if not sim.has_trait(trait_sicknessimmunity):
        sim.add_trait(trait_sicknessimmunity)

    wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_breastslarge = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_BODYSHAPE_BREASTSLARGE, Types.TRAIT))
    if not sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_breastslarge):
        sim.add_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_breastslarge)

    wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_buttlarge = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_BODYSHAPE_BUTTLARGE, Types.TRAIT))
    if not sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_buttlarge):
        sim.add_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_bodyshape_buttlarge)

    wickedwhims_attractiveness_trait_simpreference_dislikes_facialhair_beard = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_FACIALHAIR_BEARD, Types.TRAIT))
    if sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_facialhair_beard):
        sim.remove_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_facialhair_beard)

    wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_black = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_DISLIKES_HAIRCOLOR_BLACK, Types.TRAIT))
    if not sim.has_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_black):
        sim.add_trait(wickedwhims_attractiveness_trait_simpreference_dislikes_haircolor_black)

    wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_heavy = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_BODYSHAPE_HEAVY, Types.TRAIT))
    if not sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_heavy):
        sim.add_trait(wickedwhims_attractiveness_trait_simpreference_likes_bodyshape_heavy)

    wickedwhims_attractiveness_trait_simpreference_likes_detail_body_hair = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_DETAIL_BODY_HAIR, Types.TRAIT))
    if not sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_body_hair):
        sim.add_trait(wickedwhims_attractiveness_trait_simpreference_likes_detail_body_hair)

    wickedwhims_attractiveness_trait_simpreference_likes_facialhair_beard = instance_manager.get(get_resource_key(WICKEDWHIMS_ATTRACTIVENESS_TRAIT_SIMPREFERENCE_LIKES_FACIALHAIR_BEARD, Types.TRAIT))
    if not sim.has_trait(wickedwhims_attractiveness_trait_simpreference_likes_facialhair_beard):
        sim.add_trait(wickedwhims_attractiveness_trait_simpreference_likes_facialhair_beard)

    wickedwhims_trait_relationships_poly = instance_manager.get(get_resource_key(WICKEDWHIMS_TRAIT_RELATIONSHIPS_POLY, Types.TRAIT))
    if not sim.has_trait(wickedwhims_trait_relationships_poly):
        sim.add_trait(wickedwhims_trait_relationships_poly)

    wickedwhims_trait_relationships_sexcheater = instance_manager.get(get_resource_key(WICKEDWHIMS_TRAIT_RELATIONSHIPS_SEXCHEATER, Types.TRAIT))
    if not sim.has_trait(wickedwhims_trait_relationships_sexcheater):
        sim.add_trait(wickedwhims_trait_relationships_sexcheater)

    wickedwhims_trait_sex_attribute_generouslover = instance_manager.get(get_resource_key(WICKEDWHIMS_TRAIT_SEX_ATTRIBUTE_GENEROUSLOVER, Types.TRAIT))
    if not sim.has_trait(wickedwhims_trait_sex_attribute_generouslover):
        sim.add_trait(wickedwhims_trait_sex_attribute_generouslover)

    wickedwhims_trait_sex_cuckold = instance_manager.get(get_resource_key(WICKEDWHIMS_TRAIT_SEX_CUCKOLD, Types.TRAIT))
    if not sim.has_trait(wickedwhims_trait_sex_cuckold):
        sim.add_trait(wickedwhims_trait_sex_cuckold)

    wickedwhims_trait_sex_sexuallyalluring = instance_manager.get(get_resource_key(WICKEDWHIMS_TRAIT_SEX_SEXUALLYALLURING, Types.TRAIT))
    if not sim.has_trait(wickedwhims_trait_sex_sexuallyalluring):
        sim.add_trait(wickedwhims_trait_sex_sexuallyalluring)
