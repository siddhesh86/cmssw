# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: l1Ntuple -s RAW2DIGI --python_filename=l1ntuple_maker_run3_mc_rates.py -n 100 --no_output --era=Run3 --mc --conditions=110X_mcRun3_2021_realistic_v6 --customise=L1Trigger/Configuration/customiseReEmul.L1TReEmulFromRAWsimHcalTP --customise=L1Trigger/L1TNtuples/customiseL1Ntuple.L1NtupleRAWEMU --customise=L1Trigger/Configuration/customiseSettings.L1TSettingsToCaloParams_2018_v1_3 --customise_commands=process.HcalTPGCoderULUT.LUTGenerationMode=cms.bool(False) --filein=root://cms-xrd-global.cern.ch//store/mc/Run3Winter20DRPremixMiniAOD/Neutrino_Pt-2to20_gun/GEN-SIM-RAW/SNB_110X_mcRun3_2021_realistic_v6-v1/10000/0010F588-EA5D-1D42-88A0-B1C5FAFC2B28.root --no_exec

import sys
import subprocess

import FWCore.ParameterSet.Config as cms

from Configuration.Eras.Era_Run3_cff import Run3

process = cms.Process('RAW2DIGI',Run3)


# use command-line options
import FWCore.ParameterSet.VarParsing as VP
args = VP.VarParsing('analysis')

args.register('maxEvt',  100,  VP.VarParsing.multiplicity.singleton, VP.VarParsing.varType.int,   'Number of events to process (-1 for all)')
args.register('prtEvt', 1000,  VP.VarParsing.multiplicity.singleton, VP.VarParsing.varType.int,   'Print out every Nth event')
args.register('nVtxMin',   0,  VP.VarParsing.multiplicity.singleton, VP.VarParsing.varType.int,   'Minimum # of reconstructed vertices (pileup)')
args.register('nVtxMax', 999,  VP.VarParsing.multiplicity.singleton, VP.VarParsing.varType.int,   'Maximum # of reconstructed vertices (pileup)')
args.register('samples',   2,  VP.VarParsing.multiplicity.singleton, VP.VarParsing.varType.int,   'Number of samples in TP pulse')
args.register('presamps',  0,  VP.VarParsing.multiplicity.singleton, VP.VarParsing.varType.int,   'Number of pre-samples to subtract')
args.register('wgtHB',  [1.0, 1.0], VP.VarParsing.multiplicity.list, VP.VarParsing.varType.float, 'HCAL barrel TP sample weights')
args.register('wgtHE1', [1.0, 1.0], VP.VarParsing.multiplicity.list, VP.VarParsing.varType.float, 'HCAL central endcap TP sample weights')
args.register('wgtHE2', [1.0, 1.0], VP.VarParsing.multiplicity.list, VP.VarParsing.varType.float, 'HCAL forward endcap  TP sample weights')
args.parseArguments()

print '\n\nProcessing test_HCAL_OOT_PUS_data.py: maxEvt: %d, prtEvt: %d, nVtsMin: %d, nVtsMax: %d, samples: %d, presamps: %d \n' % (args.maxEvt, args.prtEvt,args.nVtxMin,args.nVtxMax,args.samples,args.presamps)

# fix bug where default wgt array is stored as a list inside a list
WGT_HB  = args.wgtHB [0] if isinstance(args.wgtHB [0], list) else args.wgtHB
WGT_HE1 = args.wgtHE1[0] if isinstance(args.wgtHE1[0], list) else args.wgtHE1
WGT_HE2 = args.wgtHE2[0] if isinstance(args.wgtHE2[0], list) else args.wgtHE2

print "WGT_HB: ", WGT_HB, ", WGT_HE1:  ",WGT_HE1, ", WGT_HE2: ",WGT_HE2


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
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.RawToDigi_cff')
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
    fileNames = cms.untracked.vstring('root://cms-xrd-global.cern.ch//store/mc/Run3Winter20DRPremixMiniAOD/Neutrino_Pt-2to20_gun/GEN-SIM-RAW/SNB_110X_mcRun3_2021_realistic_v6-v1/10000/0010F588-EA5D-1D42-88A0-B1C5FAFC2B28.root'),
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
    annotation = cms.untracked.string('l1Ntuple nevts:100'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

# Additional output definition

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '110X_mcRun3_2021_realistic_v6', '')

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
from L1Trigger.L1TNtuples.customiseL1Ntuple import L1NtupleRAWEMU 

#call to customisation function L1NtupleRAWEMU imported from L1Trigger.L1TNtuples.customiseL1Ntuple
process = L1NtupleRAWEMU(process)

# Automatic addition of the customisation function from L1Trigger.Configuration.customiseSettings
from L1Trigger.Configuration.customiseSettings import L1TSettingsToCaloParams_2018_v1_3 

#call to customisation function L1TSettingsToCaloParams_2018_v1_3 imported from L1Trigger.Configuration.customiseSettings
process = L1TSettingsToCaloParams_2018_v1_3(process)

'''
# Add filter on number of reconstructed vertices (pileup)
process.goodVertex = cms.EDFilter("VertexSelector",
    src = cms.InputTag("offlinePrimaryVertices"),
    cut = cms.string("isValid & !isFake"),
    filter = cms.bool(True)
)
process.countVertices = cms.EDFilter("VertexCountFilter",
    src = cms.InputTag("goodVertex"),
    minNumber = cms.uint32(args.nVtxMin),
    maxNumber = cms.uint32(args.nVtxMax)
)
process.nGoodVerticesFilterSequence = cms.Sequence(process.goodVertex*process.countVertices)


## Add primary vertex filter to *EVERY* path in schedule
## Imitating PrefireVetoFilter in L1TNtuples/python/customiseL1Ntuple.py
for path in process.schedule:
    if str(path) == str(process.endjob_step): continue  ## Don't add filter to endjob_step
    path.insert(0,process.nGoodVerticesFilterSequence)
'''
# End of customisation functions


print("\n# Final L1TReEmul sequence:  ")
print("# {0}".format(process.L1TReEmul))
print("# {0}".format(process.schedule))
# for path in process.schedule:
#     print ''
#     print("# {0}".format(path))


# Customisation from command line


#Have logErrorHarvester wait for the same EDProducers to finish as those providing data for the OutputModule
from FWCore.Modules.logErrorHarvester_cff import customiseLogErrorHarvesterUsingOutputCommands
process = customiseLogErrorHarvesterUsingOutputCommands(process)


process.HcalTPGCoderULUT.LUTGenerationMode=cms.bool(False)
# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion



## Customize output ROOT file name
#subprocess.call(['mkdir', 'output'])
out_name = 'L1Ntuple_HCAL_TP_OOT_PUS'
#if args.nVtxMin > 0:   out_name += '_nVtxMin_%d' % args.nVtxMin
#if args.nVtxMax < 999: out_name += '_nVtxMax_%d' % args.nVtxMax
out_name += '_nSamp_%d' % args.samples
out_name += '_nPresamp_%d' % args.presamps
out_name += '_HB_' +(str(WGT_HB )[1:-1]).replace(', ', '_').replace('-','n').replace('.','p')
out_name += '_HE1_'+(str(WGT_HE1)[1:-1]).replace(', ', '_').replace('-','n').replace('.','p')
out_name += '_HE2_'+(str(WGT_HE2)[1:-1]).replace(', ','_').replace('-','n').replace('.','p')
if args.maxEvt == -1:
    out_name += '_all'
else:
    out_name += '_%dk' % (args.maxEvt/1000)
out_name += '.root'
print '\nWill output root file %s' % out_name
 
process.TFileService = cms.Service(
    "TFileService",
    fileName = cms.string(out_name)
)
