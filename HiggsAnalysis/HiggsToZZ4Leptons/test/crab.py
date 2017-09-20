from CRABClient.UserUtilities import config
from CRABClient.UserUtilities import getUsernameFromSiteDB

config = config()
config.General.requestName = 'DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8_sm_new_noMuCal_v2'
#'TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_SingleMuon_noMuCal_v1'
#'DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_new_noMuCal_v1'
#'TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8_MuCal-v1'
#'DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8_MuCal_v1'
#'TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_v1'
#'ZZTo4L_13TeV_amcatnloFXFX_pythia8_v1_part1'
#'ZZTo4L_13TeV_powheg_pythia8_RunIISpring16MiniAODv2-PUSpring16_part1'#'DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_test'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = True



config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'HiggsTozz_MiniAOD.py'
config.JobType.outputFiles = ['roottree_leptons.root']

config.Data.inputDataset = '/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/MINIAODSIM'
#'/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/MINIAODSIM'
# '/DYJetsToLL_M-10to50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/MINIAODSIM'
#'/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/MINIAODSIM' 
#'/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext3-v1/MINIAODSIM' 
#'/DYBBJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM'
#'/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/MINIAODSIM'
#'/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/MINIAODSIM' 
#'/ZZTo4L_13TeV-amcatnloFXFX-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/MINIAODSIM' 
#'/ZZTo4L_13TeV_powheg_pythia8/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM'

config.JobType.allowUndistributedCMSSW = True


config.Data.inputDBS = 'global'
config.Data.ignoreLocality = False
config.Data.splitting = 'LumiBased'
config.Data.unitsPerJob = 10
config.Data.totalUnits = 99000
config.Data.outLFNDirBase = '/store/user/wangz/' # or '/store/group/<subdir>'
config.Data.publication = False
config.Data.outputDatasetTag = 'DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8_sm_new_noMuCal_v2'
#config.Data.outputPrimaryDataset = 'CRAB_UserFiles'

config.Site.storageSite = 'T3_US_FNALLPC'

#config.Site.ignoreGlobalBlacklist = True
