import FWCore.ParameterSet.Config as cms

from L1Trigger.L1TNtuples.l1CaloTowerTree_cfi import *
from L1Trigger.L1TNtuples.l1UpgradeTree_cfi import *
from L1Trigger.L1TNtuples.l1EventTree_cfi import *

l1CaloTowerEmuTree = l1CaloTowerTree.clone()

# Edit by SIddhesh: Following Andrew's suggestion to resolve error of unpacked HCAL TPs (instead of emulated) getting produced 
#l1CaloTowerEmuTree.ecalToken = cms.untracked.InputTag("ecalDigis:EcalTriggerPrimitives")
#l1CaloTowerEmuTree.hcalToken = cms.untracked.InputTag("hcalDigis:")
l1CaloTowerEmuTree.ecalToken = cms.untracked.InputTag("simEcalTriggerPrimitiveDigis")
l1CaloTowerEmuTree.hcalToken = cms.untracked.InputTag("simHcalTriggerPrimitiveDigis")

l1CaloTowerEmuTree.l1TowerToken = cms.untracked.InputTag("simCaloStage2Layer1Digis")
l1CaloTowerEmuTree.l1ClusterToken = cms.untracked.InputTag("simCaloStage2Digis", "MP")

l1UpgradeEmuTree = l1UpgradeTree.clone()
l1UpgradeEmuTree.egToken = cms.untracked.InputTag("simCaloStage2Digis")
l1UpgradeEmuTree.tauTokens = cms.untracked.VInputTag("simCaloStage2Digis")
l1UpgradeEmuTree.jetToken = cms.untracked.InputTag("simCaloStage2Digis")
l1UpgradeEmuTree.sumToken = cms.untracked.InputTag("simCaloStage2Digis")

L1NtupleEMUCalo = cms.Sequence(
  l1EventTree
  +l1CaloTowerEmuTree
  +l1UpgradeEmuTree
)
