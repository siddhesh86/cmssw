
## Run with different PUS options, starting from here:
## https://twiki.cern.ch/twiki/bin/viewauth/CMS/HcalPileupMitigation

dir1=$CMSSW_BASE/src/L1Trigger/L1TNtuples
 
echo "dir1: ${dir1}"


## Original, default scheme
printf '\n\ncmsRun test/test_HCAL_Original_data.py maxEvt=10 prtEvt=10000 nVtxMin=50 \n\n'
cmsRun ${dir1}/test/test_HCAL_Original_data.py maxEvt=10 prtEvt=10000 nVtxMin=50 

: <<'END_COMMENT'
## PFA1 scheme
printf '\n\ncmsRun test/test_HCAL_OOT_PUS_data.py maxEvt=10000 prtEvt=1000 nVtxMin=50 samples=1 presamps=0 wgtHB=1.0 wgtHE1=1.0 wgtHE2=1.0\n\n'
cmsRun ${dir1}/test/test_HCAL_OOT_PUS_data.py maxEvt=10000 prtEvt=1000 nVtxMin=50 samples=1 presamps=0 wgtHB=1.0 wgtHE1=1.0 wgtHE2=1.0
## PFA2 scheme
printf '\n\ncmsRun test/test_HCAL_OOT_PUS_data.py maxEvt=10000 prtEvt=1000 nVtxMin=50 samples=2 presamps=0 wgtHB=1.0,1.0 wgtHE1=1.0,1.0 wgtHE2=1.0,1.0\n\n'
cmsRun ${dir1}/test/test_HCAL_OOT_PUS_data.py maxEvt=10000 prtEvt=1000 nVtxMin=50 samples=2 presamps=0 wgtHB=1.0,1.0 wgtHE1=1.0,1.0 wgtHE2=1.0,1.0
END_COMMENT

## PFA1' scheme
printf '\n\ncmsRun test/test_HCAL_OOT_PUS_data.py maxEvt=10000 prtEvt=10000 nVtxMin=50 samples=2 presamps=1 wgtHB=-0.51,1.0 wgtHE1=-0.49,1.0 wgtHE2=-0.45,1.0\n\n'
cmsRun ${dir1}/test/test_HCAL_OOT_PUS_data.py maxEvt=10 prtEvt=10000 nVtxMin=50 samples=2 presamps=1 wgtHB=-0.51,1.0 wgtHE1=-0.49,1.0 wgtHE2=-0.45,1.0
 
: <<'END_COMMENT'
## PFA2' scheme
printf '\n\ncmsRun test/test_HCAL_OOT_PUS_data.py maxEvt=10000 prtEvt=1000 nVtxMin=50 samples=3 presamps=1 wgtHB=-0.71,1.0,1.0 wgtHE1=-0.71,1.0,1.0 wgtHE2=-1.17,1.0,1.0\n\n'
#cmsRun test/test_HCAL_OOT_PUS_data.py maxEvt=10000 prtEvt=1000 nVtxMin=50 samples=3 presamps=1 wgtHB=-0.69,1.0,1.0 wgtHE1=-0.70,1.0,1.0 wgtHE2=-1.16,1.0,1.0 # old
cmsRun ${dir1}/test/test_HCAL_OOT_PUS_data.py maxEvt=10000 prtEvt=1000 nVtxMin=50 samples=3 presamps=1 wgtHB=-0.71,1.0,1.0 wgtHE1=-0.71,1.0,1.0 wgtHE2=-1.17,1.0,1.0



## PFA1 naive PUS, 1 pre-sample
printf '\n\ncmsRun test/test_HCAL_OOT_PUS_data.py maxEvt=10000 prtEvt=1000 nVtxMin=50 samples=2 presamps=1 wgtHB=-1.0,1.0 wgtHE1=-1.0,1.0 wgtHE2=-1.0,1.0\n\n'
cmsRun ${dir1}/test/test_HCAL_OOT_PUS_data.py maxEvt=10000 prtEvt=1000 nVtxMin=50 samples=2 presamps=1 wgtHB=-1.0,1.0 wgtHE1=-1.0,1.0 wgtHE2=-1.0,1.0
## PFA1 naive PUS, 2 pre-samples
printf '\n\ncmsRun test/test_HCAL_OOT_PUS_data.py maxEvt=10000 prtEvt=1000 nVtxMin=50 samples=3 presamps=2 wgtHB=-0.5,-0.5,1.0 wgtHE1=-0.5,-0.5,1.0 wgtHE2=-0.5,-0.5,1.0\n\n'
cmsRun ${dir1}/test/test_HCAL_OOT_PUS_data.py maxEvt=10000 prtEvt=1000 nVtxMin=50 samples=3 presamps=2 wgtHB=-0.5,-0.5,1.0 wgtHE1=-0.5,-0.5,1.0 wgtHE2=-0.5,-0.5,1.0
## PFA2 naive PUS, 1 pre-sample
printf '\n\ncmsRun test/test_HCAL_OOT_PUS_data.py maxEvt=10000 prtEvt=1000 nVtxMin=50 samples=3 presamps=1 wgtHB=-2.0,1.0,1.0 wgtHE1=-2.0,1.0,1.0 wgtHE2=-2.0,1.0,1.0\n\n'
cmsRun ${dir1}/test/test_HCAL_OOT_PUS_data.py maxEvt=10000 prtEvt=1000 nVtxMin=50 samples=3 presamps=1 wgtHB=-2.0,1.0,1.0 wgtHE1=-2.0,1.0,1.0 wgtHE2=-2.0,1.0,1.0
## PFA2 naive OOT PUS, 1 pre-sample
printf '\n\ncmsRun test/test_HCAL_OOT_PUS_data.py maxEvt=10000 prtEvt=1000 nVtxMin=50 samples=3 presamps=1 wgtHB=-1.0,1.0,1.0 wgtHE1=-1.0,1.0,1.0 wgtHE2=-1.0,1.0,1.0\n\n'
cmsRun ${dir1}/test/test_HCAL_OOT_PUS_data.py maxEvt=10000 prtEvt=1000 nVtxMin=50 samples=3 presamps=1 wgtHB=-1.0,1.0,1.0 wgtHE1=-1.0,1.0,1.0 wgtHE2=-1.0,1.0,1.0
## PFA2 naive PUS, 2 pre-samples
printf '\n\ncmsRun test/test_HCAL_OOT_PUS_data.py maxEvt=10000 prtEvt=1000 nVtxMin=50 samples=4 presamps=2 wgtHB=-1.0,-1.0,1.0,1.0 wgtHE1=-1.0,-1.0,1.0,1.0 wgtHE2=-1.0,-1.0,1.0,1.0\n\n'
cmsRun ${dir1}/test/test_HCAL_OOT_PUS_data.py maxEvt=10000 prtEvt=1000 nVtxMin=50 samples=4 presamps=2 wgtHB=-1.0,-1.0,1.0,1.0 wgtHE1=-1.0,-1.0,1.0,1.0 wgtHE2=-1.0,-1.0,1.0,1.0
## PFA2 naive OOT PUS, 2 pre-samples
printf '\n\ncmsRun test/test_HCAL_OOT_PUS_data.py maxEvt=10000 prtEvt=1000 nVtxMin=50 samples=4 presamps=2 wgtHB=-0.5,-0.5,1.0,1.0 wgtHE1=-0.5,-0.5,1.0,1.0 wgtHE2=-0.5,-0.5,1.0,1.0\n\n'
cmsRun ${dir1}/test/test_HCAL_OOT_PUS_data.py maxEvt=10000 prtEvt=1000 nVtxMin=50 samples=4 presamps=2 wgtHB=-0.5,-0.5,1.0,1.0 wgtHE1=-0.5,-0.5,1.0,1.0 wgtHE2=-0.5,-0.5,1.0,1.0

END_COMMENT
