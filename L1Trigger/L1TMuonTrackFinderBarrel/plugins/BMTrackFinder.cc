//-------------------------------------------------
//
//   Class: BMTrackFinder
//
//   L1 BM Track Finder EDProducer
//
//
//
//   Author :
//   J. Troconiz              UAM Madrid
//   Modified :
//   G. Flouris               U Ioannina
//--------------------------------------------------

#include "BMTrackFinder.h"

#include "DataFormats/Common/interface/Handle.h"
#include "FWCore/Framework/interface/Event.h"

#include "DataFormats/L1DTTrackFinder/interface/L1MuDTChambPhContainer.h"
#include "DataFormats/L1DTTrackFinder/interface/L1MuDTChambThContainer.h"
#include "FWCore/Utilities/interface/EDGetToken.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "DataFormats/L1CSCTrackFinder/interface/TrackStub.h"
#include <FWCore/Framework/interface/ConsumesCollector.h>


#include "L1Trigger/L1TMuonTrackFinderBarrel/src/L1MuBMTFConfig.h"
#include "L1Trigger/L1TMuonTrackFinderBarrel/interface/L1MuBMTFSetup.h"
#include "L1Trigger/L1TMuonTrackFinderBarrel/interface/L1MuBMTrackFinder.h"

#include <iostream>
#include <iomanip>

using namespace std;

BMTrackFinder::BMTrackFinder(const edm::ParameterSet & pset) {
  m_ps = &pset;

  //produces<BMTrackContainer>("BMTF");
  produces<l1t::RegionalMuonCandBxCollection>("BM");
  produces<l1t::RegionalMuonCandBxCollection>("BMTF");
  usesResource("BMTrackFinder");
  setup1 = new L1MuBMTFSetup(*m_ps,consumesCollector());

}

BMTrackFinder::~BMTrackFinder() {

  delete setup1;
}

void BMTrackFinder::produce(edm::Event& e, const edm::EventSetup& c) {


  if ( L1MuBMTFConfig::Debug(1) ) cout << endl;
  if ( L1MuBMTFConfig::Debug(1) ) cout << "**** L1MuonBMTFTrigger processing event  ****" << endl;

  L1MuBMTrackFinder* dtbx = setup1->TrackFinder();
  dtbx->clear();

  dtbx->run(e,c);

  int ndt = dtbx->numberOfTracks();
  if ( L1MuBMTFConfig::Debug(1) ) cout << "Number of muons found by the L1 BBMX TRIGGER : "
                                       << ndt << endl;

  std::auto_ptr<l1t::RegionalMuonCandBxCollection> tra_product(new l1t::RegionalMuonCandBxCollection);
  std::auto_ptr<l1t::RegionalMuonCandBxCollection> vec_product(new l1t::RegionalMuonCandBxCollection);

  ///Muons before muon sorter
  l1t::RegionalMuonCandBxCollection  dtTracks = dtbx->getcache0();
  *tra_product = dtTracks;

  ///Muons after muon sorter, for uGMT
  l1t::RegionalMuonCandBxCollection BMTracks = dtbx->getcache();
  *vec_product = BMTracks;

  e.put(tra_product,"BMTF");
  e.put(vec_product,"BM");

}


#include "FWCore/Framework/interface/MakerMacros.h"
DEFINE_FWK_MODULE(BMTrackFinder);

