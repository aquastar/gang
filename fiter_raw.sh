#!/usr/bin/env bash

# cp
for i in `find /media/danny/Elements/TwitterDataset/decahose/ -name '*.bz2'`
#for i in `find /home/danny/Downloads/test/ -name '*.bz2'`
do
    target=`basename $i`
    filename_wo_ext="${target%.*}"
    echo $target, $filename_wo_ext
    echo 'copy starts'
    cp $i ./$target
    echo 'unzip starts'
    bunzip2 $target
    echo 'grep starts'
    grep -E '@thejacka|#FreeDaGuys|#FreeTheGuys|#FreeMyNigga|#RIPTheGuys|#RIPDaGuys|#FuckTheOpps|#Fuckdaopps|#OsoarrogantENT|@OsoArrogantJoJo|#22bandcrew|@moneyman_tatted|@Meechie2212|@callmesmokes|@TeAm039|@ChinxMusic|@PappyNotPapi|@A309Vision|@bigkutthroat_dasmoker|@elcappgguod|@GirbaudTx|@hicitydirt|@seann_ikon|@nazty_jones|@lvtrtoinne|@Wolf_DaBoss|@100STACKSFAT|@dreisdope_DGB|#freerellomixtape|@spikecorleoneg|@@JAEHIGH|@DirtySwipey|@DBO_YMM|@KollegeKidd|@ChiefKeef|@jgreenohb863|@Youngaffishal|@ramsay_tha_great|@LilMarc_YM051|@higherent|@Nunu_Otf|@JuggMoney24|@Young_Affishal|@YungKaptin92' $filename_wo_ext >> gang.twitter
    echo 'remove starts'
    rm $filename_wo_ext
done