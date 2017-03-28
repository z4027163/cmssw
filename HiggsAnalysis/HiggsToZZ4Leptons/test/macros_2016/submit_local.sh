#!/bin/bash


mkdir -p /eos/uscms/store/user/wangz/ntuple/jobdir
mkdir -p /eos/uscms/store/user/wangz/ntuple/histodir

workdir=${PWD}
echo "Running Mono-HtoZZto4Leptons Analysis with executables RunHZZ4LeptonsAnalysis"


savedir=`echo /eos/uscms/store/user/wangz/ntuple/histodir`

echo "Path is" $PATH
echo "Search Path is" $CMSSW_SEARCH_PATH

echo "Working dir is $workdir"
echo "Saving dir is $savedir"


./RunReference4mu_dustin FNAL Spring2016 mc >& ${workdir}/HZZ4LeptonsAnalysis_log

mv ${workdir}/HZZ4LeptonsAnalysis_log ${savedir}/.
mv ${workdir}/output*.root    ${savedir}/.
mv ${workdir}/output_bnn.txt ${savedir}/.
mv ${workdir}/output_bnn.root ${savedir}/.
mv ${workdir}/output_txt.txt ${savedir}/.



