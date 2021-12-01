<map version="freeplane 1.7.0">
<!--To view this file, download free mind mapping software Freeplane from http://freeplane.sourceforge.net -->
<node TEXT="Bases" FOLDED="false" ID="ID_1401552682" CREATED="1610489656296" MODIFIED="1617290147081" STYLE="oval">
<font SIZE="18"/>
<hook NAME="MapStyle">
    <properties edgeColorConfiguration="#808080ff,#ff0000ff,#0000ffff,#00ff00ff,#ff00ffff,#00ffffff,#7c0000ff,#00007cff,#007c00ff,#7c007cff,#007c7cff,#7c7c00ff" fit_to_viewport="false"/>

<map_styles>
<stylenode LOCALIZED_TEXT="styles.root_node" STYLE="oval" UNIFORM_SHAPE="true" VGAP_QUANTITY="24.0 pt">
<font SIZE="24"/>
<stylenode LOCALIZED_TEXT="styles.predefined" POSITION="right" STYLE="bubble">
<stylenode LOCALIZED_TEXT="default" ICON_SIZE="12.0 pt" COLOR="#000000" STYLE="fork">
<font NAME="SansSerif" SIZE="10" BOLD="false" ITALIC="false"/>
</stylenode>
<stylenode LOCALIZED_TEXT="defaultstyle.details"/>
<stylenode LOCALIZED_TEXT="defaultstyle.attributes">
<font SIZE="9"/>
</stylenode>
<stylenode LOCALIZED_TEXT="defaultstyle.note" COLOR="#000000" BACKGROUND_COLOR="#ffffff" TEXT_ALIGN="LEFT"/>
<stylenode LOCALIZED_TEXT="defaultstyle.floating">
<edge STYLE="hide_edge"/>
<cloud COLOR="#f0f0f0" SHAPE="ROUND_RECT"/>
</stylenode>
</stylenode>
<stylenode LOCALIZED_TEXT="styles.user-defined" POSITION="right" STYLE="bubble">
<stylenode LOCALIZED_TEXT="styles.topic" COLOR="#18898b" STYLE="fork">
<font NAME="Liberation Sans" SIZE="10" BOLD="true"/>
</stylenode>
<stylenode LOCALIZED_TEXT="styles.subtopic" COLOR="#cc3300" STYLE="fork">
<font NAME="Liberation Sans" SIZE="10" BOLD="true"/>
</stylenode>
<stylenode LOCALIZED_TEXT="styles.subsubtopic" COLOR="#669900">
<font NAME="Liberation Sans" SIZE="10" BOLD="true"/>
</stylenode>
<stylenode LOCALIZED_TEXT="styles.important">
<icon BUILTIN="yes"/>
</stylenode>
</stylenode>
<stylenode LOCALIZED_TEXT="styles.AutomaticLayout" POSITION="right" STYLE="bubble">
<stylenode LOCALIZED_TEXT="AutomaticLayout.level.root" COLOR="#000000" STYLE="oval" SHAPE_HORIZONTAL_MARGIN="10.0 pt" SHAPE_VERTICAL_MARGIN="10.0 pt">
<font SIZE="18"/>
</stylenode>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,1" COLOR="#0033ff">
<font SIZE="16"/>
</stylenode>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,2" COLOR="#00b439">
<font SIZE="14"/>
</stylenode>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,3" COLOR="#990000">
<font SIZE="12"/>
</stylenode>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,4" COLOR="#111111">
<font SIZE="10"/>
</stylenode>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,5"/>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,6"/>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,7"/>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,8"/>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,9"/>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,10"/>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,11"/>
</stylenode>
</stylenode>
</map_styles>
</hook>
<hook NAME="AutomaticEdgeColor" COUNTER="7" RULE="ON_BRANCH_CREATION"/>
<node TEXT="Distances et OD" POSITION="right" ID="ID_371214265" CREATED="1618412628438" MODIFIED="1618413415843">
<edge COLOR="#7c0000"/>
<node TEXT="Notes" ID="ID_1061702139" CREATED="1617288831255" MODIFIED="1618412653050"/>
<node TEXT="Bases dispos dans les docs :" ID="ID_546918436" CREATED="1617289821671" MODIFIED="1618412653066">
<node TEXT="les fichiers bruts" ID="ID_213567073" CREATED="1617304358896" MODIFIED="1617304368904">
<node TEXT="l&apos;enqu&#xea;te OD initiale au format pkl" ID="ID_124899019" CREATED="1617289841968" MODIFIED="1617304255077"/>
<node TEXT="La base des jonctions en csv" ID="ID_1331148747" CREATED="1617290742011" MODIFIED="1617300946025"/>
</node>
<node TEXT="Les bouts de bases cr&#xe9;&#xe9;es par la fction cree_base" ID="ID_250229912" CREATED="1617289868226" MODIFIED="1617289909339">
<node TEXT="ids" ID="ID_1412955317" CREATED="1617289916875" MODIFIED="1617290077234">
<node TEXT="ipere" ID="ID_1860084426" CREATED="1617304303000" MODIFIED="1617304308415"/>
<node TEXT="feuillet" ID="ID_1735948353" CREATED="1617304308971" MODIFIED="1617304316007"/>
<node TEXT="rang" ID="ID_2722704" CREATED="1617304316555" MODIFIED="1617304323577"/>
<node TEXT="nodeplac" ID="ID_1557859771" CREATED="1617304323711" MODIFIED="1617304329060"/>
</node>
<node TEXT="coordonn&#xe9;es" ID="ID_305324439" CREATED="1617290077360" MODIFIED="1617290105770"/>
</node>
<node TEXT="Les ad de chaque d&#xe9;placement" ID="ID_1610507816" CREATED="1617289909868" MODIFIED="1617289972792">
<node TEXT="seulement id et adidu" ID="ID_115543389" CREATED="1617289972802" MODIFIED="1617289996751"/>
</node>
<node TEXT="les bouts de base + distance + une colonne probleme" ID="ID_1014398222" CREATED="1617290002803" MODIFIED="1617290022843"/>
<node TEXT="la base finale avec toutes les distances" ID="ID_116634969" CREATED="1617290031404" MODIFIED="1617290066062"/>
<node TEXT="la base des distances par ad" ID="ID_736645515" CREATED="1617290130149" MODIFIED="1617290139265"/>
</node>
<node TEXT="D&#xe9;roulement des calculs" ID="ID_1792402054" CREATED="1617288837342" MODIFIED="1618412653069">
<node TEXT="Base initiale avec un type de mode seulement" FOLDED="true" ID="ID_1652466359" CREATED="1617288845086" MODIFIED="1617288884941">
<node TEXT="" ID="ID_862996327" CREATED="1617307181223" MODIFIED="1617307181223">
<node TEXT="&apos;17&apos; not in modes and (&apos;1&apos; in modes or &apos;2&apos; in modes or &apos;11&apos; in modes or &apos;12&apos; in modes) and &apos;13&apos; not in modes" ID="ID_938556467" CREATED="1617307203500" MODIFIED="1617468106648"/>
</node>
<node TEXT="longueur 247753&#xa;&#xa;[1]           201213&#xa;[2]            44636&#xa;[11]            1456&#xa;[12]             292&#xa;[9, 2]            45&#xa;[2, 9]            44&#xa;[1, 2]            11&#xa;[18, 1]            9&#xa;[1, 18]            8&#xa;[11, 1]            6&#xa;[1, 11]            4&#xa;[2, 15]            3&#xa;[20, 1]            3&#xa;[2, 1]             3&#xa;[2, 2]             3&#xa;[15, 2]            2&#xa;[1, 18, 1]         2&#xa;[11, 2]            2&#xa;[11, 9]            2&#xa;[2, 18]            1&#xa;[2, 1, 2]          1&#xa;[18, 2]            1&#xa;[11, 15]           1&#xa;[15, 11]           1&#xa;[1, 9]             1&#xa;[9, 1]             1&#xa;[2, 11]            1&#xa;[1, 20]            1" ID="ID_1006930605" CREATED="1617307149315" MODIFIED="1617468144251"/>
</node>
<node TEXT="Base avec les multimodaux" FOLDED="true" ID="ID_1145660380" CREATED="1617288885092" MODIFIED="1617288895345">
<node TEXT="&apos;17&apos; in modes and (&apos;1&apos; in modes or &apos;2&apos; in modes or &apos;11&apos; in modes or &apos;12&apos; in modes)" ID="ID_1323606768" CREATED="1617659207280" MODIFIED="1617659217009"/>
<node TEXT="longueur 7092&#xa;&#xa;[1, 17, 8, 8]                 765&#xa;[8, 8, 17, 1]                 764&#xa;[1, 17, 4, 4]                 501&#xa;[4, 4, 17, 1]                 491&#xa;[4, 4, 4, 17, 1]              287&#xa;                             ...&#xa;[5, 5, 17, 1]                   1&#xa;[6, 7, 17, 2]                   1&#xa;[1, 17, 5, 5]                   1&#xa;[1, 17, 5, 4, 4, 4, 17, 1]      1&#xa;[4, 4, 17, 10, 17, 2]           1&#xa;Name: LISTE_SEQ, Length: 268, dtype: int64" ID="ID_597360672" CREATED="1617659218013" MODIFIED="1617659376374"/>
</node>
<node TEXT="base semibrute avec les multimodaux" FOLDED="true" ID="ID_80685623" CREATED="1617727019205" MODIFIED="1617727037576">
<node TEXT="" ID="ID_367924640" CREATED="1617727064166" MODIFIED="1617727064166">
<node TEXT="(&apos;1&apos; in modes or &apos;2&apos; in modes or &apos;11&apos; in modes or &apos;12&apos; in modes) and &apos;13&apos; not in modes and &apos;4&apos; not in modes and &apos;16&apos; not in modes" ID="ID_341650162" CREATED="1617727088086" MODIFIED="1617727088086"/>
</node>
<node TEXT="Les refus&#xe9;s :&#xa;     [&apos;11&apos;, &apos;4&apos;, &apos;4&apos;]      1&#xa;     [&apos;16&apos;, &apos;11&apos;]      1&#xa;     [&apos;16&apos;, &apos;1&apos;]      1" ID="ID_1524945831" CREATED="1617727037587" MODIFIED="1617727061100"/>
<node TEXT="les bons&#xa;     [&apos;2&apos;]      1759&#xa;     [&apos;11&apos;]      134&#xa;     [&apos;1&apos;]      5207&#xa;     [&apos;12&apos;]      4" ID="ID_1343695846" CREATED="1617727320428" MODIFIED="1617727326536"/>
<node TEXT="Les pas bons&#xa;     [&apos;4&apos;, &apos;4&apos;, &apos;4&apos;]      889&#xa;     [&apos;4&apos;, &apos;4&apos;, &apos;4&apos;, &apos;6&apos;]      2&#xa;     [&apos;16&apos;]      80&#xa;     [&apos;4&apos;, &apos;4&apos;]      1459&#xa;     [&apos;4&apos;, &apos;4&apos;, &apos;3&apos;]      107&#xa;     [&apos;4&apos;, &apos;4&apos;, &apos;4&apos;, &apos;3&apos;]      70&#xa;     [&apos;3&apos;, &apos;4&apos;, &apos;4&apos;, &apos;4&apos;]      64&#xa;     [&apos;8&apos;, &apos;8&apos;, &apos;5&apos;]      3&#xa;     [&apos;8&apos;, &apos;8&apos;]      1794&#xa;     [&apos;3&apos;]      139&#xa;     [&apos;3&apos;, &apos;3&apos;]      33&#xa;     [&apos;10&apos;]      114&#xa;     [&apos;4&apos;, &apos;4&apos;, &apos;4&apos;, &apos;4&apos;]      48&#xa;     [&apos;8&apos;, &apos;8&apos;, &apos;3&apos;]      49&#xa;     [&apos;4&apos;, &apos;4&apos;, &apos;7&apos;]      120&#xa;     [&apos;7&apos;, &apos;4&apos;, &apos;4&apos;]      116&#xa;     [&apos;8&apos;, &apos;8&apos;, &apos;4&apos;, &apos;4&apos;]      261&#xa;     [&apos;4&apos;, &apos;4&apos;, &apos;8&apos;, &apos;8&apos;]      245&#xa;     [&apos;3&apos;, &apos;4&apos;, &apos;4&apos;]      85&#xa;     [&apos;3&apos;, &apos;4&apos;, &apos;4&apos;, &apos;4&apos;, &apos;7&apos;]      8&#xa;     [&apos;7&apos;, &apos;4&apos;, &apos;4&apos;, &apos;4&apos;, &apos;3&apos;]      7&#xa;     [&apos;5&apos;]      240&#xa;     [&apos;4&apos;, &apos;4&apos;, &apos;6&apos;]      9&#xa;     [&apos;3&apos;, &apos;4&apos;, &apos;4&apos;, &apos;4&apos;, &apos;3&apos;]      6&#xa;     [&apos;13&apos;]      6&#xa;     [&apos;4&apos;, &apos;4&apos;, &apos;4&apos;, &apos;5&apos;]      47&#xa;     [&apos;5&apos;, &apos;4&apos;, &apos;4&apos;, &apos;4&apos;]      54&#xa;     [&apos;3&apos;, &apos;8&apos;, &apos;8&apos;]      42&#xa;     [&apos;8&apos;, &apos;8&apos;, &apos;4&apos;, &apos;4&apos;, &apos;4&apos;]      110&#xa;     [&apos;4&apos;, &apos;4&apos;, &apos;4&apos;, &apos;8&apos;, &apos;8&apos;]      101&#xa;     [&apos;7&apos;]      409&#xa;     [&apos;8&apos;, &apos;8&apos;, &apos;6&apos;]      2&#xa;     [&apos;6&apos;]      14&#xa;     [&apos;6&apos;, &apos;4&apos;, &apos;4&apos;]      6&#xa;     [&apos;4&apos;, &apos;4&apos;, &apos;4&apos;, &apos;7&apos;, &apos;7&apos;]      1&#xa;     [&apos;4&apos;, &apos;4&apos;, &apos;10&apos;]      7&#xa;     [&apos;5&apos;, &apos;3&apos;]      1&#xa;     [&apos;3&apos;, &apos;5&apos;]      1&#xa;     [&apos;8&apos;, &apos;8&apos;, &apos;4&apos;, &apos;4&apos;, &apos;3&apos;]      10&#xa;     [&apos;3&apos;, &apos;4&apos;, &apos;4&apos;, &apos;8&apos;, &apos;8&apos;]      9&#xa;     [&apos;8&apos;, &apos;8&apos;, &apos;4&apos;, &apos;4&apos;, &apos;6&apos;]      1&#xa;     [&apos;6&apos;, &apos;4&apos;, &apos;4&apos;, &apos;4&apos;, &apos;7&apos;]      1&#xa;     [&apos;4&apos;, &apos;4&apos;, &apos;5&apos;]      39&#xa;     [&apos;5&apos;, &apos;4&apos;, &apos;4&apos;, &apos;4&apos;, &apos;4&apos;]      8&#xa;     [&apos;4&apos;, &apos;4&apos;, &apos;4&apos;, &apos;4&apos;, &apos;5&apos;]      6&#xa;     [&apos;6&apos;, &apos;4&apos;, &apos;4&apos;, &apos;4&apos;]      2&#xa;     [&apos;5&apos;, &apos;4&apos;, &apos;4&apos;]      33&#xa;     [&apos;7&apos;, &apos;4&apos;, &apos;4&apos;, &apos;4&apos;]      65&#xa;     [&apos;4&apos;, &apos;4&apos;, &apos;4&apos;, &apos;7&apos;]      63&#xa;     [&apos;7&apos;, &apos;4&apos;, &apos;4&apos;, &apos;4&apos;, &apos;4&apos;]      7&#xa;     [&apos;4&apos;, &apos;4&apos;, &apos;4&apos;, &apos;4&apos;, &apos;7&apos;]      8&#xa;     [&apos;7&apos;, &apos;5&apos;]      6&#xa;     [&apos;5&apos;, &apos;7&apos;]      6&#xa;     [&apos;6&apos;, &apos;7&apos;]      1&#xa;     [&apos;6&apos;, &apos;6&apos;]      5&#xa;     [&apos;7&apos;, &apos;4&apos;, &apos;4&apos;, &apos;3&apos;]      12&#xa;     [&apos;3&apos;, &apos;4&apos;, &apos;4&apos;, &apos;7&apos;]      11&#xa;     [&apos;5&apos;, &apos;4&apos;, &apos;4&apos;, &apos;3&apos;]      2&#xa;     [&apos;7&apos;, &apos;7&apos;, &apos;4&apos;, &apos;4&apos;]      1&#xa;     [&apos;10&apos;, &apos;4&apos;, &apos;4&apos;]      7&#xa;     [&apos;7&apos;, &apos;3&apos;, &apos;3&apos;]      1&#xa;     [&apos;8&apos;, &apos;8&apos;, &apos;3&apos;, &apos;4&apos;, &apos;4&apos;]      1&#xa;     [&apos;4&apos;, &apos;4&apos;, &apos;3&apos;, &apos;8&apos;, &apos;8&apos;]      1&#xa;     [&apos;5&apos;, &apos;5&apos;]      7&#xa;     [&apos;5&apos;, &apos;5&apos;, &apos;4&apos;, &apos;4&apos;]      1&#xa;     [&apos;4&apos;, &apos;4&apos;, &apos;5&apos;, &apos;5&apos;]      1&#xa;     [&apos;10&apos;, &apos;4&apos;, &apos;4&apos;, &apos;4&apos;]      3&#xa;     [&apos;4&apos;, &apos;4&apos;, &apos;4&apos;, &apos;10&apos;]      3&#xa;     [&apos;8&apos;, &apos;8&apos;, &apos;3&apos;, &apos;3&apos;]      2&#xa;     [&apos;7&apos;, &apos;7&apos;]      4&#xa;     [&apos;3&apos;, &apos;4&apos;, &apos;4&apos;, &apos;6&apos;]      1&#xa;     [&apos;8&apos;, &apos;8&apos;, &apos;4&apos;, &apos;4&apos;, &apos;4&apos;, &apos;3&apos;]      2&#xa;     [&apos;3&apos;, &apos;4&apos;, &apos;4&apos;, &apos;4&apos;, &apos;8&apos;, &apos;8&apos;]      2&#xa;     [&apos;3&apos;, &apos;4&apos;, &apos;4&apos;, &apos;3&apos;]      6&#xa;     [&apos;5&apos;, &apos;8&apos;, &apos;8&apos;]      2&#xa;     [&apos;8&apos;, &apos;8&apos;, &apos;4&apos;, &apos;4&apos;, &apos;4&apos;, &apos;7&apos;]      1&#xa;     [&apos;7&apos;, &apos;4&apos;, &apos;4&apos;, &apos;4&apos;, &apos;8&apos;, &apos;8&apos;]      1&#xa;     [&apos;3&apos;, &apos;4&apos;, &apos;4&apos;, &apos;5&apos;]      3&#xa;     [&apos;3&apos;, &apos;4&apos;, &apos;4&apos;, &apos;4&apos;, &apos;4&apos;]      1&#xa;     [&apos;4&apos;, &apos;4&apos;, &apos;4&apos;, &apos;4&apos;, &apos;3&apos;]      1&#xa;     [&apos;7&apos;, &apos;8&apos;, &apos;8&apos;]      3&#xa;     [&apos;7&apos;, &apos;8&apos;, &apos;8&apos;, &apos;3&apos;]      1&#xa;     [&apos;3&apos;, &apos;8&apos;, &apos;8&apos;, &apos;7&apos;]      1&#xa;     [&apos;8&apos;, &apos;8&apos;, &apos;7&apos;]      3&#xa;     [&apos;5&apos;, &apos;4&apos;, &apos;4&apos;, &apos;4&apos;, &apos;3&apos;]      2&#xa;     [&apos;6&apos;, &apos;6&apos;, &apos;4&apos;, &apos;4&apos;]      1&#xa;     [&apos;3&apos;, &apos;4&apos;, &apos;4&apos;, &apos;4&apos;, &apos;5&apos;]      1&#xa;     [&apos;3&apos;, &apos;4&apos;, &apos;4&apos;, &apos;7&apos;, &apos;7&apos;]      1&#xa;     [&apos;3&apos;, &apos;3&apos;, &apos;4&apos;, &apos;4&apos;]      1&#xa;     [&apos;4&apos;, &apos;4&apos;, &apos;3&apos;, &apos;3&apos;]      1&#xa;     [&apos;10&apos;, &apos;16&apos;]      1&#xa;     [&apos;7&apos;, &apos;3&apos;]      1&#xa;     [&apos;3&apos;, &apos;3&apos;, &apos;8&apos;, &apos;8&apos;]      1&#xa;     [&apos;4&apos;, &apos;4&apos;, &apos;16&apos;]      2&#xa;     [&apos;16&apos;, &apos;4&apos;, &apos;4&apos;]      1&#xa;     [&apos;6&apos;, &apos;8&apos;, &apos;8&apos;]      1" ID="ID_377991965" CREATED="1617727133216" MODIFIED="1617727144630"/>
</node>
<node TEXT="base finale des distances" ID="ID_1917049798" CREATED="1617822980136" MODIFIED="1617822997449"/>
<node TEXT="Reprise des erreurs" ID="ID_1149111443" CREATED="1617288906727" MODIFIED="1617288917610">
<node TEXT="reprise par lab avec les trajets dont l&apos;ecart est moins que 5 km" ID="ID_490297028" CREATED="1617288917619" MODIFIED="1617828899838">
<node TEXT="l&apos;ecart accumule est de 1165.3171053653227 km&#xa;1540 lignes ont ete modifiees&#xa;0.7566994190683913 km par ligne&#xa;nombre d&apos;erreurs actuel : 4218" ID="ID_1755029314" CREATED="1617828872040" MODIFIED="1617829094742"/>
</node>
<node TEXT="reprise par HERE avec les trajets dont l&apos;ecart est moins que 5 km" ID="ID_849520792" CREATED="1617288925698" MODIFIED="1617829086578">
<node TEXT="l&apos;ecart accumule est de 1365.556134385755 km&#xa;1316 lignes ont ete modifiees&#xa;1.0376566370712423 km par ligne&#xa;nombre d&apos;erreurs actuel : 2902" ID="ID_624478031" CREATED="1617830663716" MODIFIED="1617830679523"/>
</node>
<node TEXT="erreurs tenaces (2900)" ID="ID_1675102107" CREATED="1617832906695" MODIFIED="1617845405685">
<node TEXT="424 de &quot;invalid query&quot; pour les 2 logiciels" ID="ID_1609673672" CREATED="1617832912387" MODIFIED="1617832953256">
<node TEXT="421 :&quot;inf&quot; pour les lon ou lat dans la base de donn&#xe9;es" ID="ID_650810485" CREATED="1617832990173" MODIFIED="1617833022265">
<node TEXT="probablement traduit par une jonction non renseign&#xe9;e&#xa;XJONC = nan pour toutes les latorig foireuses" ID="ID_757955397" CREATED="1617834191448" MODIFIED="1617834526134"/>
</node>
<node TEXT="3 : yorig ou ydest = 1 &lt;=&gt; latorig ou latdest = 0.000009" ID="ID_529131790" CREATED="1617833023419" MODIFIED="1617833099286">
<node TEXT="en pleine for&#xea;t amazonienne, et 2 en &#xe9;quateur&#xa;Les distances renseign&#xe9;es sont nulles" ID="ID_1740148216" CREATED="1617834963708" MODIFIED="1617835003210"/>
</node>
<node TEXT="=&gt; on supprime les lignes correspondantes dans les 2 cas" ID="ID_1359406814" CREATED="1617835032865" MODIFIED="1617835072554"/>
</node>
<node TEXT="2476 pour OD trop loin" ID="ID_1539271714" CREATED="1617832954429" MODIFIED="1617832972888">
<node TEXT="2 traj en Louisiane qui ont pas l&apos;air bizarres&#xa;7 traj avec une extr&#xe9;mit&#xe9; en 0.000000 -76.237290 (&#xe9;quateur)&#xa;Le reste avec un couple (0, 0)" ID="ID_155789332" CREATED="1617836304806" MODIFIED="1617836439322"/>
<node TEXT="=&gt; on supprime les lignes correspondantes dans tous les cas" ID="ID_106931247" CREATED="1617835032865" MODIFIED="1617836469441"/>
</node>
</node>
<node TEXT="id&#xe9;es &#xe0; retenir" ID="ID_639893774" CREATED="1617836500283" MODIFIED="1617836511735">
<node TEXT="Il se peut que yait des trajets comme celui en Louisiane qui sont bons mais pas du tout &#xe0; Mtl. J&apos;ai pas v&#xe9;rifi&#xe9; mais il y en a forc&#xe9;ment moins que 1316 (4218 - 2902)" ID="ID_334068892" CREATED="1617836511743" MODIFIED="1617836614430"/>
</node>
</node>
<node TEXT="calcul des taux d&apos;occupation" ID="ID_995266528" CREATED="1617844275801" MODIFIED="1617844293804">
<node TEXT="moyenne de tous les taux d&apos;occ des trajets pris en compte" ID="ID_460067964" CREATED="1617844293815" MODIFIED="1617844308183"/>
</node>
<node TEXT="QUESTION : Le nombre de personnes par aire de diff on prend juste les gens qui se deplacent ou tout le monde ?&#xa;&#xa;Parce que si on supprime des trajets mais pas les pers associ&#xe9;es &#xe7;a fausse le calcul&#xa;&#xa;Mais en m&#xea;me temps les personnes qui se d&#xe9;placent pas de base il faut les compter...&#xa;&#xa;Du coup j&apos;ai fait avec tout le monde" ID="ID_1130656498" CREATED="1617844919854" MODIFIED="1617845033709"/>
<node TEXT="groupement des deplacements par aire de diff et avec le facteur associe (FACLOG)" ID="ID_890469104" CREATED="1617846167074" MODIFIED="1617846233125">
<node TEXT="[&quot;ADIDU&quot;, &quot;dist_calc&quot;, &quot;nb_pers&quot;]" ID="ID_1400789696" CREATED="1617846494657" MODIFIED="1617850546784"/>
</node>
</node>
<node TEXT="Liste des attributs gard&#xe9;e :" FOLDED="true" ID="ID_756105127" CREATED="1617288968152" MODIFIED="1618412653080">
<node TEXT="[&quot;IPERE&quot;, &quot;FEUILLET&quot;, &quot;RANG&quot;, &quot;NODEPLAC&quot;, &quot;NB_JONC&quot;, &quot;DIST&quot;, &quot;SEQ_MODES&quot;, &quot;XORIG&quot;, &quot;YORIG&quot;, &quot;LATORIG&quot;, &quot;LONORIG&quot;, &quot;XDEST&quot;, &quot;YDEST&quot;, &quot;LATDEST&quot;, &quot;LONDEST&quot;, &quot;XJONC&quot;, &quot;YJONC&quot;, &quot;LATJONC&quot;, &quot;LONJONC&quot;, &quot;NB_MODES&quot;, &quot;LISTE_SEQ&quot;(, &quot;no_segment&quot;), &quot;dist_calc&quot;, &quot;code_err&quot;]" ID="ID_1371818492" CREATED="1617288990613" MODIFIED="1617740138293"/>
</node>
<node TEXT="codes d&apos;erreur" ID="ID_732111985" CREATED="1617832431141" MODIFIED="1618412653113">
<node TEXT="code erreur 0 : tout s&apos;est bien passe&#xa;code erreur 1 : &apos;routes&apos; pas dans les cles ET [&apos;code&apos;] == &apos;InvalidQuery&apos;&#xa;code erreur 2 : &apos;routes&apos; pas dans les cles&#xa;code erreur 3 : O ou D trop loin des trucs calcules" ID="ID_373699684" CREATED="1617832436640" MODIFIED="1617832482422"/>
</node>
</node>
<node TEXT="Emissions sur le territoire" POSITION="right" ID="ID_755433265" CREATED="1618412656296" MODIFIED="1618413418912">
<edge COLOR="#00007c"/>
<node TEXT="Bases initiales" ID="ID_770600055" CREATED="1618412694198" MODIFIED="1618412702656">
<node TEXT="Nombre de v&#xe9;hicules de chaque groupe par aire de diffusion" ID="ID_1309158569" CREATED="1618412702664" MODIFIED="1618412717063">
<node TEXT="ADIDU" ID="ID_499204301" CREATED="1618413990823" MODIFIED="1618413994346"/>
<node TEXT="no_corr (pas de corresp)" ID="ID_77439326" CREATED="1618413994636" MODIFIED="1618414004696"/>
<node TEXT="gr0" ID="ID_475645753" CREATED="1618414005977" MODIFIED="1618414012003"/>
<node TEXT="gr1" ID="ID_286875568" CREATED="1618414012143" MODIFIED="1618414015157"/>
<node TEXT="..." ID="ID_567149133" CREATED="1618414015461" MODIFIED="1618414016663"/>
<node TEXT="gr9" ID="ID_860270488" CREATED="1618414016807" MODIFIED="1618414020993"/>
</node>
<node TEXT="Emissions moyennes par groupe" ID="ID_663261402" CREATED="1618412717170" MODIFIED="1618412746698">
<node TEXT="numero groupe" ID="ID_796121142" CREATED="1618413722687" MODIFIED="1618413755135"/>
<node TEXT="emission a associer" ID="ID_1663730040" CREATED="1618413726589" MODIFIED="1618413750627"/>
</node>
<node TEXT="Km totaux par AD (dans le dossier OD)" ID="ID_1534148225" CREATED="1618412747024" MODIFIED="1619120543105">
<node TEXT="ADIDU" ID="ID_727933966" CREATED="1618413701646" MODIFIED="1618413705906"/>
<node TEXT="km totaux" ID="ID_475193625" CREATED="1618413706044" MODIFIED="1618413709449"/>
<node TEXT="nb personnes" ID="ID_28488559" CREATED="1618413709677" MODIFIED="1618413714065"/>
</node>
<node TEXT="Base des aires de diffusion et co sur tout le Canada" ID="ID_840768177" CREATED="1618412779724" MODIFIED="1618412877726">
<node TEXT="ADIDU" ID="ID_948627740" CREATED="1618413842706" MODIFIED="1618413846221"/>
<node TEXT="autres..." ID="ID_14067221" CREATED="1618413846487" MODIFIED="1618413852353"/>
</node>
<node TEXT="base des SM" ID="ID_997280282" CREATED="1618501797554" MODIFIED="1618501802903">
<node TEXT="Sm100" ID="ID_1811843594" CREATED="1618501802924" MODIFIED="1618501807175"/>
<node TEXT="R8Sm100 (inutile)" ID="ID_24565065" CREATED="1618501807375" MODIFIED="1618501821581"/>
<node TEXT="Descrip (nom)" ID="ID_1339688784" CREATED="1618501821703" MODIFIED="1618501831196"/>
<node TEXT="MI_Sup_km2 (superficie)" ID="ID_1080744985" CREATED="1618501831309" MODIFIED="1618501854520"/>
<node TEXT="Date_AMJ" ID="ID_1582240467" CREATED="1618501854678" MODIFIED="1618501864683"/>
<node TEXT="Pop2016" ID="ID_1280362655" CREATED="1618501865189" MODIFIED="1618501870068"/>
<node TEXT="TLog2016 (inutile)" ID="ID_1684193969" CREATED="1618501870177" MODIFIED="1618501912562"/>
<node TEXT="RhLog2016 (inutile)" ID="ID_1285846212" CREATED="1618501877251" MODIFIED="1618501918701"/>
<node TEXT="geometry" ID="ID_1040782591" CREATED="1618501890401" MODIFIED="1618501893125"/>
</node>
<node TEXT="equivalence AD SM" ID="ID_1624555220" CREATED="1620421280401" MODIFIED="1620421290082">
<node TEXT="outs/equivalence_AD_SM.pkl" ID="ID_286475663" CREATED="1620421290090" MODIFIED="1620421305656"/>
<node TEXT="ADIDU" ID="ID_1656651995" CREATED="1620421305783" MODIFIED="1620421369478"/>
<node TEXT="Sm100" ID="ID_1261166765" CREATED="1620421369761" MODIFIED="1620421399596"/>
</node>
</node>
<node TEXT="Bases en sortie" ID="ID_1338592183" CREATED="1619125926161" MODIFIED="1619125932576">
<node TEXT="Emissions finales par AD" ID="ID_850669886" CREATED="1619125932590" MODIFIED="1619125941160"/>
<node TEXT="Emissions finales par SM" ID="ID_601142062" CREATED="1619125941294" MODIFIED="1619125949498"/>
</node>
<node TEXT="attributs des bases en sortie" ID="ID_93994694" CREATED="1618412941167" MODIFIED="1618413262601" STYLE="fork">
<node TEXT="(Id d&#xe9;coupage g&#xe9;ographique)" ID="ID_1310119307" CREATED="1618412951758" MODIFIED="1618412993688"/>
<node TEXT="(Nom d&#xe9;coupage g&#xe9;ographique)" ID="ID_1250256718" CREATED="1618412994160" MODIFIED="1618413006084"/>
<node TEXT="* gCO2/km moyen" ID="ID_1576309890" CREATED="1618413006555" MODIFIED="1618500429593"/>
<node TEXT="+ km totaux" ID="ID_360060289" CREATED="1618413014485" MODIFIED="1618500433645"/>
<node TEXT="+ nb personnes/d&#xe9;coupage" ID="ID_217739300" CREATED="1618413018496" MODIFIED="1618500437960"/>
<node TEXT="+ aires" ID="ID_263639374" CREATED="1618413024085" MODIFIED="1618500441372"/>
<node TEXT="+ nb de v&#xe9;hicules/d&#xe9;coupage" ID="ID_1240110639" CREATED="1620420787880" MODIFIED="1620420799013"/>
<node TEXT="-- tCO2/d&#xe9;coupage" ID="ID_15542531" CREATED="1618413028569" MODIFIED="1618500509411"/>
<node TEXT="-- km/hab" ID="ID_1667073599" CREATED="1618413040404" MODIFIED="1618500513358"/>
<node TEXT="-- gCO2/m2" ID="ID_345340854" CREATED="1618413046892" MODIFIED="1618500517672"/>
<node TEXT="-- kgCO2/pers" ID="ID_230149981" CREATED="1618413071083" MODIFIED="1618500561700"/>
<node TEXT="-- kgCO2/veh" ID="ID_1380257870" CREATED="1620424166440" MODIFIED="1620424183006"/>
<node TEXT="-- km/veh" ID="ID_1416199533" CREATED="1620424183408" MODIFIED="1620425796915"/>
</node>
<node TEXT="Choix des attributs" ID="ID_1063727665" CREATED="1622128145286" MODIFIED="1622128151648">
<node TEXT="Nombre de v&#xe9;hicules (AD ou SAAQ ?)" ID="ID_1381443196" CREATED="1622128151671" MODIFIED="1622128175700">
<node TEXT="LE TRUC C&apos;EST QUE LES VEHICULES SONT CALCULES DE LA MEME FACON QUE LES PERSONNES -&gt; Le nombre de personnes est pas bon" ID="ID_1849492130" CREATED="1622129665600" MODIFIED="1622129708197"/>
<node TEXT="10% moins de veh si on compte avec SAAQ" ID="ID_659461112" CREATED="1622128158716" MODIFIED="1622128209518"/>
<node TEXT="de grosses diff&#xe9;rences dans les donn&#xe9;es (jusqu&apos;&#xe0; des facteurs 20, des fois m&#xea;me infinis quand pas de donn&#xe9;es)" ID="ID_717960658" CREATED="1622128209666" MODIFIED="1622129475157"/>
<node TEXT="30% sont de m&#xea;me valeur &#xe0; 20% pr&#xe8;s" ID="ID_1541043739" CREATED="1622129475920" MODIFIED="1622146403248"/>
<node TEXT="82% on jusqu&apos;au double de valeur en &#xe9;cart" ID="ID_1970871400" CREATED="1622129587634" MODIFIED="1622146428318"/>
</node>
</node>
</node>
</node>
</map>
