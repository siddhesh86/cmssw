# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: l1Ntuple -s RAW2DIGI --python_filename=HCAL_OOT_PUS_data.py -n 100 --no_output --era=Run2_2018 --data --conditions=110X_dataRun2_v12 --customise=L1Trigger/Configuration/customiseReEmul.L1TReEmulFromRAWsimHcalTP --customise=L1Trigger/L1TNtuples/customiseL1Ntuple.L1NtupleAODRAWEMU --customise=L1Trigger/Configuration/customiseSettings.L1TSettingsToCaloParams_2018_v1_3

import sys
import FWCore.ParameterSet.Config as cms

from Configuration.Eras.Era_Run2_2018_cff import Run2_2018

process = cms.Process('RAW2DIGI',Run2_2018)

# use command-line options
import FWCore.ParameterSet.VarParsing as VP
args = VP.VarParsing('analysis')

args.register('maxEvt',  100,  VP.VarParsing.multiplicity.singleton, VP.VarParsing.varType.int,   'Number of events to process (-1 for all)')
args.register('prtEvt',   10,  VP.VarParsing.multiplicity.singleton, VP.VarParsing.varType.int,   'Print out every Nth event')
args.register('samples',   2,  VP.VarParsing.multiplicity.singleton, VP.VarParsing.varType.int,   'Number of samples in TP pulse')
args.register('presamps',  0,  VP.VarParsing.multiplicity.singleton, VP.VarParsing.varType.int,   'Number of pre-samples to subtract')
args.register('wgtHB',  [1.0, 1.0], VP.VarParsing.multiplicity.list, VP.VarParsing.varType.float, 'HCAL barrel TP sample weights')
args.register('wgtHE1', [1.0, 1.0], VP.VarParsing.multiplicity.list, VP.VarParsing.varType.float, 'HCAL central endcap TP sample weights')
args.register('wgtHE2', [1.0, 1.0], VP.VarParsing.multiplicity.list, VP.VarParsing.varType.float, 'HCAL forward endcap  TP sample weights')
args.parseArguments()

# fix bug where default wgt array is stored as a list inside a list
WGT_HB  = args.wgtHB [0] if isinstance(args.wgtHB [0], list) else args.wgtHB
WGT_HE1 = args.wgtHE1[0] if isinstance(args.wgtHE1[0], list) else args.wgtHE1
WGT_HE2 = args.wgtHE2[0] if isinstance(args.wgtHE2[0], list) else args.wgtHE2

# check that number of weights matches number of samples
if len(WGT_HB) != args.samples or len(WGT_HE1) != args.samples or len(WGT_HE2) != args.samples:
    print 'MAJOR PROBLEM!!! At least one of our weight arrays does not have length %d!  Exiting.' % args.samples
    print WGT_HB
    print WGT_HE1
    print WGT_HE2
    sys.exit()

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff')
process.load('Configuration.StandardSequences.RawToDigi_Data_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(args.maxEvt),
    output = cms.optional.untracked.allowed(cms.int32,cms.PSet)
)
process.MessageLogger.cerr.FwkReport.reportEvery = args.prtEvt

print '\nProcessing up to %d events, will report once per %d' % (args.maxEvt, args.prtEvt)


# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        'file:/eos/cms/store/data/Run2018D/SingleMuon/RAW-RECO/ZMu-PromptReco-v2/000/321/457/00000/0C03F56B-BEA5-E811-AE45-FA163E96C3EF.root',
        'file:/eos/cms/store/data/Run2018D/SingleMuon/RAW-RECO/ZMu-PromptReco-v2/000/321/457/00000/0CF5EF0C-D1A5-E811-ADD7-FA163ED7B2EC.root',
        'file:/eos/cms/store/data/Run2018D/SingleMuon/RAW-RECO/ZMu-PromptReco-v2/000/321/457/00000/1EED6C56-BFA5-E811-A076-FA163E7D67F9.root',
        'file:/eos/cms/store/data/Run2018D/SingleMuon/RAW-RECO/ZMu-PromptReco-v2/000/321/457/00000/446F21CD-E6A5-E811-A980-FA163EEA4F9F.root',
        'file:/eos/cms/store/data/Run2018D/SingleMuon/RAW-RECO/ZMu-PromptReco-v2/000/321/457/00000/4ECA77CB-D2A5-E811-8183-02163E012D8E.root',
        'file:/eos/cms/store/data/Run2018D/SingleMuon/RAW-RECO/ZMu-PromptReco-v2/000/321/457/00000/507FDA3B-C1A5-E811-8C49-FA163E071950.root',
        'file:/eos/cms/store/data/Run2018D/SingleMuon/RAW-RECO/ZMu-PromptReco-v2/000/321/457/00000/60D23B7B-C7A5-E811-B14B-FA163EF4F4A1.root',
        'file:/eos/cms/store/data/Run2018D/SingleMuon/RAW-RECO/ZMu-PromptReco-v2/000/321/457/00000/72A5272C-BEA5-E811-B16C-FA163E35CC86.root',
        'file:/eos/cms/store/data/Run2018D/SingleMuon/RAW-RECO/ZMu-PromptReco-v2/000/321/457/00000/92A87B6C-C0A5-E811-B99D-02163E010F5C.root',
        'file:/eos/cms/store/data/Run2018D/SingleMuon/RAW-RECO/ZMu-PromptReco-v2/000/321/457/00000/9E6AD29E-BEA5-E811-BD40-FA163E73968C.root',
        'file:/eos/cms/store/data/Run2018D/SingleMuon/RAW-RECO/ZMu-PromptReco-v2/000/321/457/00000/BEBEAF84-BEA5-E811-9E57-02163E01A076.root',
        'file:/eos/cms/store/data/Run2018D/SingleMuon/RAW-RECO/ZMu-PromptReco-v2/000/321/457/00000/DABB5524-BFA5-E811-9A27-FA163E5E460D.root',
        'file:/eos/cms/store/data/Run2018D/SingleMuon/RAW-RECO/ZMu-PromptReco-v2/000/321/457/00000/E873F832-CFA5-E811-9D00-FA163EFDD21B.root',
        'file:/eos/cms/store/data/Run2018D/SingleMuon/RAW-RECO/ZMu-PromptReco-v2/000/321/457/00000/EC0F3940-C3A5-E811-9736-02163E01A00E.root'
    ),
    secondaryFileNames = cms.untracked.vstring()
)

## HCAL OOT PU subtraction
process.load("SimCalorimetry.HcalTrigPrimProducers.hcaltpdigi_cff")

process.simHcalTriggerPrimitiveDigis.numberOfSamplesQIE11    = args.samples
process.simHcalTriggerPrimitiveDigis.numberOfPresamplesQIE11 = args.presamps
process.simHcalTriggerPrimitiveDigis.weightsQIE11HB  = WGT_HB
process.simHcalTriggerPrimitiveDigis.weightsQIE11HE1 = WGT_HE1
process.simHcalTriggerPrimitiveDigis.weightsQIE11HE2 = WGT_HE2

print '\nConfiguring HCAL TP out-of-time pileup subtraction:'
print '  * numberOfSamplesQIE11    = %d' % args.samples
print '  * numberOfPresamplesQIE11 = %d' % args.presamps
print '  * weightsQIE11HB  = ['+str(WGT_HB )[1:-1]+']'
print '  * weightsQIE11HE1 = ['+str(WGT_HE1)[1:-1]+']'
print '  * weightsQIE11HE2 = ['+str(WGT_HE2)[1:-1]+']'
print ''


process.options = cms.untracked.PSet(
    FailPath = cms.untracked.vstring(),
    IgnoreCompletely = cms.untracked.vstring(),
    Rethrow = cms.untracked.vstring(),
    SkipEvent = cms.untracked.vstring(),
    allowUnscheduled = cms.obsolete.untracked.bool,
    canDeleteEarly = cms.untracked.vstring(),
    emptyRunLumiMode = cms.obsolete.untracked.string,
    eventSetup = cms.untracked.PSet(
        forceNumberOfConcurrentIOVs = cms.untracked.PSet(

        ),
        numberOfConcurrentIOVs = cms.untracked.uint32(1)
    ),
    fileMode = cms.untracked.string('FULLMERGE'),
    forceEventSetupCacheClearOnNewRun = cms.untracked.bool(False),
    makeTriggerResults = cms.obsolete.untracked.bool,
    numberOfConcurrentLuminosityBlocks = cms.untracked.uint32(1),
    numberOfConcurrentRuns = cms.untracked.uint32(1),
    numberOfStreams = cms.untracked.uint32(0),
    numberOfThreads = cms.untracked.uint32(1),
    printDependencies = cms.untracked.bool(False),
    sizeOfStackForThreadsInKB = cms.optional.untracked.uint32,
    throwIfIllegalParameter = cms.untracked.bool(True),
    wantSummary = cms.untracked.bool(False)
)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('l1Ntuple nevts:10'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

# Additional output definition

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '110X_dataRun2_v12', '')

# Path and EndPath definitions
process.raw2digi_step = cms.Path(process.RawToDigi)
process.endjob_step = cms.EndPath(process.endOfProcess)

# Schedule definition
process.schedule = cms.Schedule(process.raw2digi_step,process.endjob_step)
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)

# customisation of the process.

# Automatic addition of the customisation function from L1Trigger.Configuration.customiseReEmul
from L1Trigger.Configuration.customiseReEmul import L1TReEmulFromRAWsimHcalTP 

#call to customisation function L1TReEmulFromRAWsimHcalTP imported from L1Trigger.Configuration.customiseReEmul
process = L1TReEmulFromRAWsimHcalTP(process)

# Automatic addition of the customisation function from L1Trigger.L1TNtuples.customiseL1Ntuple
from L1Trigger.L1TNtuples.customiseL1Ntuple import L1NtupleAODRAWEMUCalo 

#call to customisation function L1NtupleAODRAWEMUCalo imported from L1Trigger.L1TNtuples.customiseL1Ntuple
process = L1NtupleAODRAWEMUCalo(process)

# Automatic addition of the customisation function from L1Trigger.Configuration.customiseSettings
from L1Trigger.Configuration.customiseSettings import L1TSettingsToCaloParams_2018_v1_3 

#call to customisation function L1TSettingsToCaloParams_2018_v1_3 imported from L1Trigger.Configuration.customiseSettings
process = L1TSettingsToCaloParams_2018_v1_3(process)

# End of customisation functions

# Customisation from command line

#Have logErrorHarvester wait for the same EDProducers to finish as those providing data for the OutputModule
from FWCore.Modules.logErrorHarvester_cff import customiseLogErrorHarvesterUsingOutputCommands
process = customiseLogErrorHarvesterUsingOutputCommands(process)

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion

## Customize output ROOT file name
out_name = 'output/L1Ntuple_HCAL_TP_OOT_PUS'
out_name += '_%d_Samp' % args.samples
out_name += '_%d_Presamp' % args.presamps
out_name += '_HB_' +(str(WGT_HB )[1:-1]).replace(', ', '_').replace('-','n').replace('.','p')
out_name += '_HE1_'+(str(WGT_HE1)[1:-1]).replace(', ', '_').replace('-','n').replace('.','p')
out_name += '_HE2_'+(str(WGT_HE2)[1:-1]).replace(', ','_').replace('-','n').replace('.','p')
out_name += '_%dk.root' % (args.maxEvt/1000)
print '\nWill output root file %s' % out_name

process.TFileService = cms.Service(
    "TFileService",
    fileName = cms.string(out_name)
)
