from PhysicsTools.SelectorUtils.centralIDRegistry import central_id_registry

import FWCore.ParameterSet.Config as cms

# This MVA ID is the same as 25ns V2 except it uses quantities embedded 
# in the objects rather than value maps.
#
# In this file we define the locations of the MVA weights, cuts on the MVA values
# for specific working points, and configure those cuts in VID
#

#
# The following MVA is derived for Spring15 MC samples for non-triggering photons.
# See more documentation in this presentation:
#    
#    https://indico.cern.ch/event/369241/contribution/1/attachments/1140148/1632879/egamma-Aug14-2015.pdf
#

# This MVA implementation class name
mvaTLEFall15ClassName = "TLEMVAEstimatorRun2Fall15"#"mvaTLEID_Fall15"
# The tag is an extra string attached to the names of the products
# such as ValueMaps that needs to distinguish cases when the same MVA estimator
# class is used with different tuning/weights
mvaTag = "V1"

# There are 2 categories in this MVA. They have to be configured in this strict order
# (cuts and weight files order):
#   0    barrel photons
#   1    endcap photons

mvaTLEID_Fall15V1 = cms.vstring(
    "RecoEgamma/PhotonIdentification/data/Fall15/EIDmva_EB1_10_oldtle_v1_noSpec_BDT.weights.xml",
    "RecoEgamma/PhotonIdentification/data/Fall15/EIDmva_EB2_10_oldtle_v1_noSpec_BDT.weights.xml",
    "RecoEgamma/PhotonIdentification/data/Fall15/EIDmva_EE_10_oldtle_v1_noSpec_BDT.weights.xml"

    )

# Load some common definitions for MVA machinery
from RecoEgamma.PhotonIdentification.Identification.mvaPhotonID_tools import *

# The locatoins of value maps with the actual MVA values and categories
# for all particles.
# The names for the maps are "<module name>:<MVA class name>Values" 
# and "<module name>:<MVA class name>Categories"
mvaProducerModuleLabel = "photonMVAValueMapProducer"
mvaValueMapName        = mvaProducerModuleLabel + ":" + mvaTLEFall15ClassName + mvaTag + "Values"
mvaCategoriesMapName   = mvaProducerModuleLabel + ":" + mvaTLEFall15ClassName + mvaTag + "Categories"

# The working point for this MVA that is expected to have about 90% signal
# efficiency in each category for photons with pt>30 GeV (somewhat lower
# for lower pt photons).
#idName = "mvaTLEID-Fall15-V1-wp90"
#MVA_WP90 = PhoMVA_3Categories_WP(
#    idName = idName,
#    mvaValueMapName = mvaValueMapName,           # map with MVA values for all particles
#    mvaCategoriesMapName = mvaCategoriesMapName, # map with category index for all particles
#    cutCategory0 = 0.374, # EB
#    cutCategory1 = 0.336,  # EE
#    cutCategory2 = 0.336  # EE
#
#    )

#
# Finally, set up VID configuration for all cuts
#

# Create the PSet that will be fed to the MVA value map producer
mvaTLEID_Fall15_V1_producer_config = cms.PSet( 
    mvaName            = cms.string(mvaTLEFall15ClassName),
    mvaTag             = cms.string(mvaTag),
    weightFileNames    = mvaTLEID_Fall15V1,
    #
    # All the event content needed for this MVA implementation follows
    #
    # All the value maps: these are expected to be produced by the
    # PhotonIDValueMapProducer running upstream
    #
    useValueMaps = cms.bool(False),
    full5x5SigmaIEtaIEtaMap   = cms.InputTag("photonIDValueMapProducer:phoFull5x5SigmaIEtaIEta"),
    full5x5SigmaIEtaIPhiMap   = cms.InputTag("photonIDValueMapProducer:phoFull5x5SigmaIEtaIPhi"),
    full5x5E1x3Map      = cms.InputTag("photonIDValueMapProducer:phoFull5x5E1x3"),
    full5x5E2x2Map      = cms.InputTag("photonIDValueMapProducer:phoFull5x5E2x2"),
    full5x5E2x5MaxMap   = cms.InputTag("photonIDValueMapProducer:phoFull5x5E2x5Max"),
    full5x5E5x5Map      = cms.InputTag("photonIDValueMapProducer:phoFull5x5E5x5"),
    esEffSigmaRRMap     = cms.InputTag("photonIDValueMapProducer:phoESEffSigmaRR"),
    phoChargedIsolation = cms.InputTag("photonIDValueMapProducer:phoChargedIsolation"),
    phoPhotonIsolation  = cms.InputTag("photonIDValueMapProducer:phoPhotonIsolation"),
    phoWorstChargedIsolation = cms.InputTag("photonIDValueMapProducer:phoWorstChargedIsolation"),
    #
    # Original event content: pileup in this case
    # 
    rho                       = cms.InputTag("fixedGridRhoFastjetAll") 
    )
# Create the VPset's for VID cuts
#mvaTLEID_Fall15_V1_wp90 = configureVIDMVAPhoID_V1( MVA_WP90 )

# The MD5 sum numbers below reflect the exact set of cut variables
# and values above. If anything changes, one has to 
# 1) comment out the lines below about the registry, 
# 2) run "calculateMD5 <this file name> <one of the VID config names just above>
# 3) update the MD5 sum strings below and uncomment the lines again.
#

#central_id_registry.register( mvaTLEID_Fall15g_V1_wp90.idName,
#                              'replace_me')

#mvaTLEID_Fall15_V1_wp90.isPOGApproved = cms.untracked.bool(False)
