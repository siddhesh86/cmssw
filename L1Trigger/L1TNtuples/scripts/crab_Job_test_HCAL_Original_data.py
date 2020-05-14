from WMCore.Configuration import Configuration
config = Configuration()

# tested and proven

config.section_("General")
config.General.requestName = 'L1TNtuple_HCal_Original'
#config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = True

config.section_("JobType")
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'test_HCAL_Original_data.py'
config.JobType.pyCfgParams = ['maxEvt=-1', 'prtEvt=10000', 'nVtxMin=50']
#config.JobType.outputFiles = ['L1Ntuple_HCAL.root']

config.section_("Data")
config.Data.inputDataset = '/SingleMuon/Run2018A-ZMu-12Nov2019_UL2018-v2/RAW-RECO'
config.Data.inputDBS = 'global'
config.Data.splitting = 'Automatic' #'LumiBased'
#config.Data.unitsPerJob = 20
#config.Data.lumiMask = 'https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions12/8TeV/Prompt/Cert_190456-208686_8TeV_PromptReco_Collisions12_JSON.txt'
#config.Data.runRange = '193093-193999' # '193093-194075'
config.Data.publication = True
config.Data.outputDatasetTag = 'L1TNtuple_HCal_Original'
config.Data.outLFNDirBase = '/store/user/ssawant/'

config.section_("Site")
config.Site.storageSite = 'T2_IN_TIFR'
