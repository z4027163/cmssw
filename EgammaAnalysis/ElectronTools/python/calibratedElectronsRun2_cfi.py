import FWCore.ParameterSet.Config as cms

correctionType = "80Xapproval"
files = {"Prompt2015":"EgammaAnalysis/ElectronTools/data/ScalesSmearings/74X_Prompt_2015",
         "76XReReco" :"EgammaAnalysis/ElectronTools/data/ScalesSmearings/76X_16DecRereco_2015_Etunc",
         "80Xapproval" : "EgammaAnalysis/ElectronTools/data/ScalesSmearings/80X_ichepV1_2016_ele"}

calibratedElectrons = cms.EDProducer("CalibratedElectronProducerRun2",

                                     # input collections
                                     electrons = cms.InputTag('gedGsfElectrons'),
                                     gbrForestName = cms.vstring('electron_eb_ECALTRK_lowpt', 'electron_eb_ECALTRK',
                                                                 'electron_ee_ECALTRK_lowpt', 'electron_ee_ECALTRK',
                                                                 'electron_eb_ECALTRK_lowpt_var', 'electron_eb_ECALTRK_var',
                                                                 'electron_ee_ECALTRK_lowpt_var', 'electron_ee_ECALTRK_var'),

                                     # data or MC corrections
                                     # if isMC is false, data corrections are applied
                                     isMC = cms.bool(False),
                                     autoDataType = cms.bool(True),
    
                                     # set to True to get special "fake" smearing for synchronization. Use JUST in case of synchronization
                                     isSynchronization = cms.bool(False),
                                     
                                     correctionFile = cms.string(files[correctionType]),
                                     recHitCollectionEB = cms.InputTag('reducedEcalRecHitsEB'),
                                     recHitCollectionEE = cms.InputTag('reducedEcalRecHitsEE')
                                     
                                     )

