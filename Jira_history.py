
ffmpeg -i test.wav -filter:a loudnorm -ar 8000 -c:a pcm_s16le test2.wav
ffmpeg -i test.wav -filter:a loudnorm -ar 8000 -c:a pcm_s16le -b:a 128k -ac 2 test2.wav
ffmpeg -i test2.wav -af "volume=3.5" test3.wav
ffmpeg -i test3.wav -filter:a "atempo=0.95" test4.wav


ffmpeg -i input.wav -ar 16000 output.wav
ffmpeg -i output.wav -af "highpass=f=300, lowpass=f=3000" output1.wav
ffmpeg -i output1.wav -af "volume=1.5" output2.wav
ffmpeg -i output2.wav -af "equalizer=f=1000:width_type=h:w=200:g=5" output3.wav
ffmpeg -i output3.wav -af "crystalizer" output4.wav
=ЕСЛИОШИБКА((((@Agents($AH$2;$AI$2;I18;I68)/30)*22,5)/0,85)/I166;2)
ffmpeg -i audio.wav -f ffmetadata -i metadata.xml -map_metadata 1 -c:v copy output.wav

<?xml version="1.0" encoding="UTF-8"?>

-<x:recording x:version="11.2" x:ref="240004044498673" xmlns:x="http://www.verint.com/xmlns/recording20080320">


-<x:segment x:version="1">

<x:complete>true</x:complete>

<x:master>true</x:master>

<x:keepcontent>true</x:keepcontent>

<x:keepxml>true</x:keepxml>

<x:rollbackrequired>false</x:rollbackrequired>

<x:rollbacktime>15</x:rollbacktime>

<x:compressiontype>4</x:compressiontype>

<x:compressed>true</x:compressed>

<x:rollbackid>2348</x:rollbackid>

<x:tenant_id>0</x:tenant_id>

<x:dualmarking>false</x:dualmarking>

<x:primary>true</x:primary>

<x:errorpriority>0</x:errorpriority>

<x:contenttype>audio/vnd.verint.wav</x:contenttype>

<x:capturetype>IP</x:capturetype>

<x:starttime>2023-11-01T17:55:13.269+03:00</x:starttime>

<x:readytoarchive>true</x:readytoarchive>

<x:switch_id>240000001</x:switch_id>

<x:captureversion>15.2.10.867</x:captureversion>

<x:minumumrecordingdurationforaqs>15</x:minumumrecordingdurationforaqs>

<x:systemtype>sipproxy</x:systemtype>


-<x:tags>


-<x:tag x:timestamp="2023-11-01T19:55:13.702+05:00" x:taggedbyhost="Verint2-Rec-B" x:taggedbycomponent="IPCapture">

<x:attribute x:key="callref">SIP/AUDIO/63980078@SEPF4BD9EF2F3A3</x:attribute>

</x:tag>


-<x:tag x:timestamp="2023-11-01T19:55:13.703+05:00" x:taggedbyhost="Verint2-Rec-B" x:taggedbycomponent="IPCapture">

<x:attribute x:key="datasourcename">Cisco</x:attribute>

</x:tag>


-<x:tag x:timestamp="2023-11-01T19:55:13.703+05:00" x:taggedbyhost="Verint2-Rec-B" x:taggedbycomponent="IPCapture">

<x:attribute x:key="datasource">1</x:attribute>

</x:tag>


-<x:tag x:timestamp="2023-11-01T19:55:13.704+05:00" x:taggedbyhost="Verint2-Rec-B" x:taggedbycomponent="IPCapture">

<x:attribute x:key="sipcallid">a7d32400-1ef196c9-242a08e-79eb40a@10.180.158.7</x:attribute>

</x:tag>


-<x:tag x:timestamp="2023-11-01T19:55:13.704+05:00" x:taggedbyhost="Verint2-Rec-B" x:taggedbycomponent="IPCapture">

<x:attribute x:key="dataportid">2348</x:attribute>

</x:tag>


-<x:tag x:timestamp="2023-11-01T19:55:13.705+05:00" x:taggedbyhost="Verint2-Rec-B" x:taggedbycomponent="IPCapture">

<x:attribute x:key="extension">7668</x:attribute>

</x:tag>


-<x:tag x:timestamp="2023-11-01T19:55:13.706+05:00" x:taggedbyhost="Verint2-Rec-B" x:taggedbycomponent="IFServices" x:forwardtosession="false">

<x:attribute x:key="calltype">In</x:attribute>

<x:attribute x:key="extension">7668</x:attribute>

<x:attribute x:key="signallingcalledparty">984985201092</x:attribute>

<x:attribute x:key="signallingcalledpartyname">MSK1-EXTRGW-CUBE-03</x:attribute>

<x:attribute x:key="signallingcallingparty">7668</x:attribute>

<x:attribute x:key="signallingcallingpartyname">SEPF4BD9EF2F3A3</x:attribute>

<x:attribute x:key="x-farendrefci">63978067</x:attribute>

</x:tag>


-<x:tag x:timestamp="2023-11-01T19:55:13.708+05:00" x:taggedbyhost="Verint2-Rec-B" x:taggedbycomponent="IFServices" x:forwardtosession="false">

<x:attribute x:key="calltype">In</x:attribute>

<x:attribute x:key="extension">7668</x:attribute>

<x:attribute x:key="signallingcalledparty">984985201092</x:attribute>

<x:attribute x:key="signallingcalledpartyname">MSK1-EXTRGW-CUBE-03</x:attribute>

<x:attribute x:key="signallingcallingparty">7668</x:attribute>

<x:attribute x:key="signallingcallingpartyname">SEPF4BD9EF2F3A3</x:attribute>

<x:attribute x:key="x-farendrefci">63978067</x:attribute>

</x:tag>


-<x:tag x:timestamp="2023-11-01T19:55:13.709+05:00" x:taggedbyhost="Verint2-Rec-B" x:taggedbycomponent="IPCapture">

<x:attribute x:key="audiostarttime">2023-11-01T17:55:13.269+03:00</x:attribute>

</x:tag>


-<x:tag x:timestamp="2023-11-01T19:55:13.714+05:00" x:taggedbyhost="Verint2-Rec-B" x:taggedbycomponent="IFServices" x:forwardtosession="false">

<x:attribute x:key="verint2-rec-b_latency">0</x:attribute>

<x:attribute x:key="verint2-rec-b_offset">Lost</x:attribute>

</x:tag>


-<x:tag x:timestamp="2023-11-01T19:55:13.714+05:00" x:taggedbyhost="Verint2-Rec-A" x:taggedbycomponent="IFServices" x:forwardtosession="false">

<x:attribute x:key="verint2-rec-a_latency">0</x:attribute>

<x:attribute x:key="verint2-rec-a_offset">41</x:attribute>

</x:tag>


-<x:tag x:timestamp="2023-11-01T18:01:28.424+03:00" x:taggedbyhost="Verint2-Rec-B" x:taggedbycomponent="IFServices" x:forwardtosession="false">

<x:attribute x:key="otherpartychannel">EXTERNAL</x:attribute>

</x:tag>


-<x:tag x:timestamp="2023-11-01T20:01:28.479+05:00" x:taggedbyhost="Verint2-Rec-B" x:taggedbycomponent="IPCapture">

<x:attribute x:key="endtime">2023-11-01T18:01:28.397+03:00</x:attribute>

</x:tag>


-<x:tag x:timestamp="2023-11-01T20:01:28.479+05:00" x:taggedbyhost="Verint2-Rec-B" x:taggedbycomponent="IPCapture">

<x:attribute x:key="stopreason">CallEnd</x:attribute>

</x:tag>

</x:tags>

<x:shared_key>audio_1_7668</x:shared_key>

<x:duration>375</x:duration>


-<x:streams>


-<x:stream>

<x:audiodurationinms>374080</x:audiodurationinms>

<x:audioendtime>2023-11-01T18:01:28.395+03:00</x:audioendtime>

<x:decodingerrors>0</x:decodingerrors>

<x:decryptionerrors>0</x:decryptionerrors>

<x:dstip>10.10.180.38:50222</x:dstip>

<x:durationinms>374877</x:durationinms>

<x:firstpackettime>2023-11-01T19:55:13.489+05:00</x:firstpackettime>

<x:lastpackettime>2023-11-01T20:01:28.395+05:00</x:lastpackettime>

<x:missedrtppackets>41</x:missedrtppackets>

<x:mixingerrors>0</x:mixingerrors>

<x:rtptype>0</x:rtptype>

<x:rtptypename>PCMU</x:rtptypename>

<x:silencedurationinms>820</x:silencedurationinms>

<x:srcip>10.178.21.205:18776</x:srcip>

<x:ssrc>0x8f9a9449</x:ssrc>

<x:totaldecodings>209</x:totaldecodings>

<x:totaldecryptions>0</x:totaldecryptions>

<x:totalmixings>209</x:totalmixings>

<x:totalrtppackets>18704</x:totalrtppackets>

</x:stream>


-<x:stream>

<x:audiodurationinms>375220</x:audiodurationinms>

<x:audioendtime>2023-11-01T18:01:28.397+03:00</x:audioendtime>

<x:decodingerrors>0</x:decodingerrors>

<x:decryptionerrors>0</x:decryptionerrors>

<x:dstip>10.10.180.38:50336</x:dstip>

<x:durationinms>375147</x:durationinms>

<x:firstpackettime>2023-11-01T19:55:13.269+05:00</x:firstpackettime>

<x:lastpackettime>2023-11-01T20:01:28.397+05:00</x:lastpackettime>

<x:missedrtppackets>0</x:missedrtppackets>

<x:mixingerrors>0</x:mixingerrors>

<x:rtptype>0</x:rtptype>

<x:rtptypename>PCMU</x:rtptypename>

<x:silencedurationinms>0</x:silencedurationinms>

<x:srcip>10.178.21.205:31380</x:srcip>

<x:ssrc>0x741ebdfd</x:ssrc>

<x:totaldecodings>209</x:totaldecodings>

<x:totaldecryptions>0</x:totaldecryptions>

<x:totalmixings>209</x:totalmixings>

<x:totalrtppackets>18761</x:totalrtppackets>

</x:stream>

</x:streams>

<x:contentfilesize>500404</x:contentfilesize>

</x:segment>


-<x:contacts>


-<x:contact x:version="3" x:taggedbyhost="Verint2-Rec-B" x:taggedbycomponent="IFServices" x:parent="true" x:id="9149970490930000181">


-<x:sessions>


-<x:session x:version="2" x:taggedbyhost="Verint2-Rec-B" x:taggedbycomponent="IFServices" x:parent="true" x:id="2023110119550939709720211424001801" x:parentinum="240004044498673" x:lastupdated="2023-11-01T20:02:33.438+05:00" x:ctiseen="true">

<x:complete>true</x:complete>

<x:agent_id>240008119</x:agent_id>

<x:ani>984985201092</x:ani>

<x:datasource>1</x:datasource>

<x:direction>Inbound</x:direction>

<x:dnis>7668</x:dnis>

<x:duration>379</x:duration>

<x:employeename>Руслан Р. Канбеков</x:employeename>

<x:errorpriority>0</x:errorpriority>

<x:extension>7668</x:extension>

<x:extension_datasource>1</x:extension_datasource>

<x:number_of_holds>0</x:number_of_holds>

<x:total_hold_time>0</x:total_hold_time>

<x:interactiontype>Phone</x:interactiontype>

<x:is_mute/>

<x:mark>true</x:mark>

<x:organization_id>240001862</x:organization_id>

<x:pbx_login_id>10972</x:pbx_login_id>

<x:starttime>2023-11-01T17:55:09.397+03:00</x:starttime>

<x:switch_call_id>66008442</x:switch_call_id>

<x:switch_id>240000001</x:switch_id>

<x:tenant_id>0</x:tenant_id>

<x:time_offset>180</x:time_offset>

<x:wrapup_time>60</x:wrapup_time>


-<x:inums>

<x:inum x:starttime="2023-11-01T17:55:13.269+03:00" x:endtime="2023-11-01T18:01:28.397+03:00" x:contenttype="audio/vnd.verint.wav">240004044498673</x:inum>

<x:inum x:starttime="2023-11-01T17:55:11.457+03:00" x:endtime="2023-11-01T18:02:28.432+03:00" x:contenttype="screen/vnd.verint.capb">240002041638225</x:inum>

</x:inums>


-<x:tags>


-<x:tag x:timestamp="2023-11-01T17:55:09.397+03:00" x:taggedbyhost="Verint2-Rec-B" x:taggedbycomponent="IFServices">

<x:attribute x:key="agentid">10972</x:attribute>

<x:attribute x:key="agentname">Руслан Р. Канбеков</x:attribute>

<x:attribute x:key="agentpk">8119</x:attribute>

<x:attribute x:key="calledparty">7668</x:attribute>

<x:attribute x:key="calledpartyname">Канбеков Р.Р.</x:attribute>

<x:attribute x:key="callid">66008442</x:attribute>

<x:attribute x:key="callingparty">984985201092</x:attribute>

<x:attribute x:key="datasourcename">Cisco</x:attribute>

<x:attribute x:key="devicename">SEPF4BD9EF2F3A3</x:attribute>

<x:attribute x:key="eventtype">Alerting</x:attribute>

<x:attribute x:key="extendedcallhistory">Unknown</x:attribute>

<x:attribute x:key="extension">7668</x:attribute>

<x:attribute x:key="globalcallid">3/15676794/66008442</x:attribute>

<x:attribute x:key="interactiontype">Phone</x:attribute>

<x:attribute x:key="loggedonduration">8082</x:attribute>

<x:attribute x:key="networkid">KANBEKOVRR</x:attribute>

<x:attribute x:key="numberofholds">0</x:attribute>

<x:attribute x:key="numberoftimesconference">0</x:attribute>

<x:attribute x:key="numberoftimestransferred">0</x:attribute>

<x:attribute x:key="organization">Группа по работе с ключевыми клиентами</x:attribute>

<x:attribute x:key="parties">7668 (Канбеков Р.Р.), 984985201092</x:attribute>

<x:attribute x:key="pauseduration">0</x:attribute>

<x:attribute x:key="skill">5000</x:attribute>

<x:attribute x:key="timeonhold">0</x:attribute>

<x:attribute x:key="ultraagentid">240008119</x:attribute>

<x:attribute x:key="workstation">UFA01-S07978.fc.uralsibbank.ru</x:attribute>

</x:tag>


-<x:tag x:timestamp="2023-11-01T17:55:09.637+03:00" x:taggedbyhost="Verint2-Rec-B" x:taggedbycomponent="IFServices">

<x:attribute x:key="ani">984985201092</x:attribute>

<x:attribute x:key="dnis">7668</x:attribute>

<x:attribute x:key="eventtype">Data_Changed</x:attribute>

<x:attribute x:key="tematika">64377</x:attribute>

</x:tag>


-<x:tag x:timestamp="2023-11-01T17:55:09.637+03:00" x:taggedbyhost="Verint2-Rec-B" x:taggedbycomponent="IFServices">

<x:attribute x:key="eventtype">Data_Changed</x:attribute>

<x:attribute x:key="firedbusinessruleids">51</x:attribute>

<x:attribute x:key="firedbusinessrules">Record Screens</x:attribute>

<x:attribute x:key="mimemediatype">Screen</x:attribute>

<x:attribute x:key="modulenumber">240002</x:attribute>

<x:attribute x:key="screenunit">240002</x:attribute>

<x:attribute x:key="skill">5004</x:attribute>

</x:tag>


-<x:tag x:timestamp="2023-11-01T17:55:12.577+03:00" x:taggedbyhost="Verint2-Rec-B" x:taggedbycomponent="IFServices">

<x:attribute x:key="calldirection">Inbound</x:attribute>

<x:attribute x:key="callingpartyname">984985201092</x:attribute>

<x:attribute x:key="eventtype">Connected</x:attribute>

<x:attribute x:key="extendedcallhistory">Inbound</x:attribute>

<x:attribute x:key="mimemediatype">Audio</x:attribute>

<x:attribute x:key="modulenumber">240004</x:attribute>

<x:attribute x:key="numberdialed">7668</x:attribute>

<x:attribute x:key="serialnumber">240004</x:attribute>

</x:tag>


-<x:tag x:timestamp="2023-11-01T17:55:13.707+03:00" x:taggedbyhost="Verint2-Rec-B" x:taggedbycomponent="IFServices">

<x:attribute x:key="calltype">In</x:attribute>

<x:attribute x:key="eventtype">Data_Changed</x:attribute>

</x:tag>


-<x:tag x:timestamp="2023-11-01T18:01:28.424+03:00" x:taggedbyhost="Verint2-Rec-B" x:taggedbycomponent="IFServices">

<x:attribute x:key="eventtype">Disconnected</x:attribute>

<x:attribute x:key="otherpartychannelhistory">EXTERNAL</x:attribute>

</x:tag>


-<x:tag x:timestamp="2023-11-01T18:01:28.424+03:00" x:taggedbyhost="Verint2-Rec-B" x:taggedbycomponent="IFServices">

<x:attribute x:key="eventtype">Disconnected</x:attribute>

</x:tag>


-<x:tag x:timestamp="2023-11-01T18:02:28.435+03:00" x:taggedbyhost="Verint2-Rec-B" x:taggedbycomponent="IFServices">

<x:attribute x:key="eventtype">Data_Changed</x:attribute>

<x:attribute x:key="wrapuptime">60</x:attribute>

</x:tag>

</x:tags>

</x:session>

</x:sessions>

<x:complete>true</x:complete>

<x:ani>984985201092</x:ani>

<x:number_of_conferences>0</x:number_of_conferences>

<x:dnis>7668</x:dnis>

<x:duration>439</x:duration>

<x:number_of_holds>0</x:number_of_holds>

<x:total_hold_time>0</x:total_hold_time>

<x:is_exception>false</x:is_exception>

<x:starttime>2023-11-01T17:55:09.397+03:00</x:starttime>

<x:tenant_id>0</x:tenant_id>

<x:time_offset>180</x:time_offset>

<x:number_of_transfers>0</x:number_of_transfers>

</x:contact>

</x:contacts>

</x:recording>
