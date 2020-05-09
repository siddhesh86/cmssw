#! /usr/bin/env python

## *************************************************************************** ##
##  Look at scale and resolution of L1T jets and MET with different input TPs  ##
## *************************************************************************** ##

import os

import ROOT as R
R.gROOT.SetBatch(False)  ## Don't print histograms to screen while processing

PRT_EVT  = 100    ## Print every Nth event
MAX_EVT  = -1     ## Number of events to process
VERBOSE  = False  ## Verbose print-out

PT_MIN = 30   ## Minimum offline jet pT to consider
DR_MAX = 0.3  ## Maximum dR between L1T and offline jets for matching


def main():

    print '\nInside L1T_JetMET_Res\n'

    in_file_names = []
    in_file_names.append('output/L1Ntuple_HCAL_Original_nVtxMax_12_100k.root')
    in_file_names.append('output/L1Ntuple_HCAL_TP_OOT_PUS_nVtxMax_12_nSamp_1_nPresamp_0_HB_1p0_HE1_1p0_HE2_1p0_100k.root')
    in_file_names.append('output/L1Ntuple_HCAL_TP_OOT_PUS_nVtxMax_12_nSamp_2_nPresamp_0_HB_1p0_1p0_HE1_1p0_1p0_HE2_1p0_1p0_100k.root')

    if not os.path.exists('plots'): os.makedirs('plots')

    out_file_str = 'L1T_JetMET_Res'
    out_file_str += ('_%dk' % (MAX_EVT / 1000))
    out_file = R.TFile('plots/'+out_file_str+'.root','recreate')

    chains = {}
    chains['Evt'] = []  ## Event info
    chains['Vtx'] = []  ## RECO vertex info
    chains['Jet'] = []  ## RECO jet info
    chains['Unp'] = []  ## Unpacked Layer-2 info
    chains['Emu'] = []  ## Emulated Layer-2 info
    for i in range(len(in_file_names)):
        print 'Adding file %s' % in_file_names[i]
        chains['Evt'].append( R.TChain('l1EventTree/L1EventTree') )
        chains['Vtx'].append( R.TChain('l1RecoTree/RecoTree') )
        chains['Jet'].append( R.TChain('l1JetRecoTree/JetRecoTree') )
        chains['Unp'].append( R.TChain('l1UpgradeTree/L1UpgradeTree') )
        chains['Emu'].append( R.TChain('l1UpgradeEmuTree/L1UpgradeTree') )
        chains['Evt'][i].Add( in_file_names[i] )
        chains['Vtx'][i].Add( in_file_names[i] )
        chains['Jet'][i].Add( in_file_names[i] )
        chains['Unp'][i].Add( in_file_names[i] )
        chains['Emu'][i].Add( in_file_names[i] )


    ###################
    ### Book histograms
    ###################

    res_bins = [100, -1.5, 3.5]
    dR_bins  = [ 35,  0.0, 0.35]

    h_jet_res_unp = {}
    h_jet_res_emu = {}
    h_jet_dR_unp  = {}
    h_jet_dR_emu  = {}

    for iEta in ['HB','HE1','HE2','HF']:
        h_jet_res_unp[iEta] = {}
        h_jet_res_emu[iEta] = {}
        h_jet_dR_unp [iEta] = {}
        h_jet_dR_emu [iEta] = {}

        for iPt in ['lowPt', 'medPt', 'hiPt']:
            h_jet_res_unp[iEta][iPt] = []
            h_jet_res_emu[iEta][iPt] = []
            h_jet_dR_unp [iEta][iPt] = []
            h_jet_dR_emu [iEta][iPt] = []

            ## Separate histogram for each input file (different TP reconstructions)
            for iTP in range(len(in_file_names)):

                h_jet_res_unp[iEta][iPt].append( R.TH1D( 'h_jet_res_%s_%s_%d_unp' % (iEta, iPt, iTP),
                                                         'L1T Unp jet resolution in %s for %s' % (iEta, iPt),
                                                         res_bins[0], res_bins[1], res_bins[2] ) )
                h_jet_res_emu[iEta][iPt].append( R.TH1D( 'h_jet_res_%s_%s_%d_emu' % (iEta, iPt, iTP),
                                                         'L1T Emu jet resolution in %s for %s' % (iEta, iPt),
                                                         res_bins[0], res_bins[1], res_bins[2] ) )

                h_jet_dR_unp[iEta][iPt].append( R.TH1D( 'h_jet_dR_%s_%s_%d_unp' % (iEta, iPt, iTP),
                                                        'dR(RECO, Unp L1T) jet in %s for %s' % (iEta, iPt),
                                                        dR_bins[0], dR_bins[1], dR_bins[2] ) )
                h_jet_dR_emu[iEta][iPt].append( R.TH1D( 'h_jet_dR_%s_%s_%d_emu' % (iEta, iPt, iTP),
                                                        'dR(RECO, Emu L1T) jet in %s for %s' % (iEta, iPt),
                                                        dR_bins[0], dR_bins[1], dR_bins[2] ) )

    iEvt = 0
    print '\nEntering loop over chains'
    for iCh in range(len(chains['Unp'])):

        if iEvt > MAX_EVT and MAX_EVT > 0: break

        ## Faster tecnhique, inspired by https://github.com/thomreis/l1tMuonTools/blob/master/L1Analysis.py
        Evt_br = R.L1Analysis.L1AnalysisEventDataFormat()
        Vtx_br = R.L1Analysis.L1AnalysisRecoVertexDataFormat()
        Jet_br = R.L1Analysis.L1AnalysisRecoJetDataFormat()
        Unp_br = R.L1Analysis.L1AnalysisL1UpgradeDataFormat()
        Emu_br = R.L1Analysis.L1AnalysisL1UpgradeDataFormat()

        chains['Evt'][iCh].SetBranchAddress('Event',     R.AddressOf(Evt_br))
        chains['Vtx'][iCh].SetBranchAddress('Vertex',    R.AddressOf(Vtx_br))
        chains['Jet'][iCh].SetBranchAddress('Jet',       R.AddressOf(Jet_br))
        chains['Unp'][iCh].SetBranchAddress('L1Upgrade', R.AddressOf(Unp_br))
        chains['Emu'][iCh].SetBranchAddress('L1Upgrade', R.AddressOf(Emu_br))

        print '\nEntering loop over events for chain %d' % iCh
        for jEvt in range(chains['Unp'][iCh].GetEntries()):

            iEvt += 1
            if iEvt > MAX_EVT and MAX_EVT > 0: break
            if iEvt % PRT_EVT is 0: print '\nEvent # %d (%dth in chain)' % (iEvt, jEvt+1)

            chains['Evt'][iCh].GetEntry(jEvt)
            chains['Vtx'][iCh].GetEntry(jEvt)
            chains['Jet'][iCh].GetEntry(jEvt)
            chains['Unp'][iCh].GetEntry(jEvt)
            chains['Emu'][iCh].GetEntry(jEvt)

            # ## Use these lines if you don't explicitly define the DataFormat and then do SetBranchAddress above
            # Evt_br = chains['Evt'][iCh].Event
            # Vtx_br = chains['Vtx'][iCh].Vertex
            # Jet_br = chains['Jet'][iCh].Vertex
            # Unp_br = chains['Unp'][iCh].L1Upgrade
            # Emu_br = chains['Emu'][iCh].L1Upgrade

            if iEvt % PRT_EVT is 0: print '  * Run %d, LS %d, event %d, nVtx %d' % (int(Evt_br.run), int(Evt_br.lumi), int(Evt_br.event), int(Vtx_br.nVtx))

            nOffJets = int(Jet_br.nJets)
            nUnpJets = int(Unp_br.nJets)
            nEmuJets = int(Emu_br.nJets)


            if VERBOSE:
                print 'Number of jets: RECO = %d, L1T Unpacked = %d, Emulated = %d' % (nOffJets, nUnpJets, nEmuJets)


            ## Loop over all offline RECO jets
            for iOff in range(nOffJets):
                
                vOff = R.TLorentzVector()
                vOff.SetPtEtaPhiM(Jet_br.et[iOff], Jet_br.eta[iOff], Jet_br.phi[iOff], 0)

                ## Apply selection cut(s) to offline jet
                if vOff.Pt() < PT_MIN: continue

                ## Pick the |eta| and pT bin
                if   abs(vOff.Eta()) < 1.5: iEta = 'HB'
                elif abs(vOff.Eta()) < 2.4: iEta = 'HE1'
                elif abs(vOff.Eta()) < 3.0: iEta = 'HE2'
                else:                       iEta = 'HF'

                if   vOff.Pt() <  60: iPt = 'lowPt'
                elif vOff.Pt() < 120: iPt = 'medPt'
                else:                 iPt = 'hiPt'

                ## Find jet with minimum dR to unpacked jet
                min_dR_unp = DR_MAX
                min_dR_emu = DR_MAX
                iMinUnp = -1
                iMinEmu = -1
                vMinUnp = R.TLorentzVector()
                vMinEmu = R.TLorentzVector()

                ## Loop over all L1T unpacked jets
                for iUnp in range(nUnpJets):

                    vUnp = R.TLorentzVector()
                    vUnp.SetPtEtaPhiM(Unp_br.jetEt[iUnp], Unp_br.jetEta[iUnp], Unp_br.jetPhi[iUnp], 0)

                    if vOff.DeltaR(vUnp) < min_dR_unp:
                        min_dR_unp = vOff.DeltaR(vUnp)
                        iMinUnp = iUnp
                        vMinUnp = vUnp
                ## End loop: for iUnp in range(nUnpJets)

                ## Loop over all L1T emulated jets
                for iEmu in range(nEmuJets):

                    vEmu = R.TLorentzVector()
                    vEmu.SetPtEtaPhiM(Emu_br.jetEt[iEmu], Emu_br.jetEta[iEmu], Emu_br.jetPhi[iEmu], 0)

                    if vOff.DeltaR(vEmu) < min_dR_emu:
                        min_dR_emu = vOff.DeltaR(vEmu)
                        iMinEmu = iEmu
                        vMinEmu = vEmu
                ## End loop: for iEmu in range(nEmuJets)

                if iMinUnp >= 0:
                    h_jet_res_unp[iEta][iPt][iCh].Fill( (vMinUnp.Pt() - vOff.Pt()) / vOff.Pt() )
                    h_jet_dR_unp[iEta][iPt][iCh].Fill( vOff.DeltaR(vMinUnp) )
                else:
                    h_jet_res_unp[iEta][iPt][iCh].Fill( res_bins[1] + 0.01 )
                    h_jet_dR_unp[iEta][iPt][iCh].Fill( dR_bins[2] - 0.01 )

                if iMinEmu >= 0:
                    h_jet_res_emu[iEta][iPt][iCh].Fill( (vMinEmu.Pt() - vOff.Pt()) / vOff.Pt() )
                    h_jet_dR_emu[iEta][iPt][iCh].Fill( vOff.DeltaR(vMinEmu) )
                else:
                    h_jet_res_emu[iEta][iPt][iCh].Fill( res_bins[1] + 0.01 )
                    h_jet_dR_emu[iEta][iPt][iCh].Fill( dR_bins[2] - 0.01 )

            ## End loop: for iOff in range(nOffJets):

        ## End loop: for jEvt in range(chains['Unp'][iCh].GetEntries()):
    ## End loop: for iCh in range(len(chains['Unp'])):

    print '\nFinished loop over chains'

    out_file.cd()

    colors = [R.kViolet, R.kBlue, R.kGreen, R.kRed]

    for iEta in ['HB','HE1','HE2','HF']:
        for iPt in ['lowPt', 'medPt', 'hiPt']:
            for iTP in range(len(in_file_names)):

                h_jet_res_unp[iEta][iPt][iTP].SetLineWidth(2)
                h_jet_res_emu[iEta][iPt][iTP].SetLineWidth(2)
                h_jet_dR_unp [iEta][iPt][iTP].SetLineWidth(2)
                h_jet_dR_emu [iEta][iPt][iTP].SetLineWidth(2)

                h_jet_res_unp[iEta][iPt][iTP].SetLineColor(R.kBlack)
                h_jet_res_emu[iEta][iPt][iTP].SetLineColor(colors[iTP])
                h_jet_dR_unp [iEta][iPt][iTP].SetLineColor(R.kBlack)
                h_jet_dR_emu [iEta][iPt][iTP].SetLineColor(colors[iTP])

                h_jet_res_unp[iEta][iPt][iTP].Write()
                h_jet_res_emu[iEta][iPt][iTP].Write()
                h_jet_dR_unp [iEta][iPt][iTP].Write()
                h_jet_dR_emu [iEta][iPt][iTP].Write()
    
    out_file.Close()
    del chains

    print '\nWrote out file:  plots/'+out_file_str+'.root'


if __name__ == '__main__':
    main()
