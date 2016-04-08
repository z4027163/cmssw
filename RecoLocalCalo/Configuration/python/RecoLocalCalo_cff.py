import FWCore.ParameterSet.Config as cms

#
# Ecal part
#
from RecoLocalCalo.Configuration.ecalLocalRecoSequence_cff import *
from RecoLocalCalo.EcalRecAlgos.EcalSeverityLevelESProducer_cfi import *

#defines a sequence ecalLocalRecoSequence
#
# Hcal part
#
# calo geometry
#
# changed by tommaso. now the calibrations are read from Configuration/StaqndardSequences/data/*Conditions.cff
#
#HCAL reconstruction
from RecoLocalCalo.Configuration.hcalLocalReco_cff import *
from RecoLocalCalo.Configuration.hcalGlobalReco_cff import *
#
# sequence CaloLocalReco and CaloGlobalReco
#
calolocalreco = cms.Sequence(ecalLocalRecoSequence+hcalLocalRecoSequence)
caloglobalreco = cms.Sequence(hcalGlobalRecoSequence)

from RecoLocalCalo.HcalRecProducers.HcalHitSelection_cfi import *
reducedHcalRecHitsSequence = cms.Sequence( reducedHcalRecHits )

#
# R.Ofierzynski (29.Oct.2009): add NZS sequence
#
from RecoLocalCalo.Configuration.hcalLocalRecoNZS_cff import *
calolocalrecoNZS = cms.Sequence(ecalLocalRecoSequence+hcalLocalRecoSequence+hcalLocalRecoSequenceNZS) 

def _modifyRecoLocalCaloForHGCal( theProcess ):
    theProcess.load("RecoLocalCalo.HGCalRecProducers.HGCalUncalibRecHit_cfi")
    theProcess.load("RecoLocalCalo.HGCalRecProducers.HGCalRecHit_cfi")
    theProcess.calolocalreco += theProcess.HGCalUncalibRecHit
    theProcess.calolocalreco += theProcess.HGCalRecHit

from Configuration.StandardSequences.Eras import eras
modifyConfigurationStandardSequencesRecoLocalCaloForHGCal_ = eras.phase2_hgcal.makeProcessModifier( _modifyRecoLocalCaloForHGCal )

