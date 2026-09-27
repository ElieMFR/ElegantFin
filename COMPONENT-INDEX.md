# Index des composants — ElegantFin Cinema Edition v1.3.10

Généré par `python scripts/component-index.py`. **Ne pas éditer à la main.**

Les règles d'un même composant sont réparties en couches sur tout le fichier :
l'ordre porte la cascade, c'est voulu, il ne faut pas les regrouper. Mais avant
de modifier le style d'un composant, il faut avoir vu **toutes** ses règles —
sinon on en corrige une pendant qu'une autre, ailleurs, continue de gagner.
C'est exactement ce qui a produit la régression v1.2.88 sur le bouton skip,
dont les huit règles s'étalaient sur 3 700 lignes.

Source indexée : `ElegantFin-cinema-v1.3.10.css` — 7308 lignes.

| Composant | Règles | Zones | Lignes |
|---|---:|---:|---|
| `card` | 36 | 14 | 420–502, 740, 843, 1489–1509, 2031–2064, 2091–2095, 2371–2389, 2425, 6287, 6545–6561, 6639–6661, 6691–6698, 6781, 7186 |
| `cardScalable` | 28 | 13 | 420–431, 479–502, 789–833, 859–897, 2389, 3364, 3475, 3554, 5496, 6301–6311, 6380, 6545, 6682–6698 |
| `material-icons` | 17 | 13 | 356–375, 1708, 1786, 1838, 3321, 3480, 3554–3560, 3666, 3824, 4214, 4698, 4732–4742, 5314 |
| `cardImageContainer` | 22 | 12 | 474, 811, 839–868, 897, 954–984, 5605–5609, 5689, 6293, 6372–6380, 6420, 6545–6561, 6682 |
| `itemDetailPage` | 18 | 11 | 1552, 1638, 1717, 1957–1982, 2026, 2127, 2438–2443, 3809–3820, 4308, 4595, 7014–7052 |
| `skinHeader` | 16 | 10 | 284, 4039, 4072–4099, 5504, 5898, 5954–5962, 5988–6013, 6363, 6512, 7123 |
| `nameContainer` | 27 | 9 | 686, 2134–2157, 2198, 2227, 2262–2308, 2345, 2376–2380, 5071–5123, 7014–7052 |
| `backdropCard` | 12 | 9 | 941–947, 1062, 1957, 2043, 2127, 2380–2389, 2416, 2443, 2723 |
| `js` | 9 | 9 | 323, 1624, 1717, 2198, 2800, 3454, 5314, 6464, 6708 |
| `card-hoverable` | 23 | 8 | 502, 799, 859–947, 5609, 6311, 6420–6455, 6545, 6827 |
| `parentName` | 23 | 8 | 686, 2139–2157, 2198, 2227, 2262–2308, 5077–5123, 5196, 7014–7052 |
| `detailPageWrapperContainer` | 17 | 8 | 686, 1520–1530, 1982, 2100, 2134–2157, 2227, 2262–2308, 2376 |
| `subtitle` | 16 | 8 | 1957, 2026, 2139, 2198, 2317–2327, 2438–2443, 5131–5164, 7014–7052 |
| `cardBox` | 12 | 8 | 420–468, 494, 740, 881, 988, 6287, 6545, 6827 |
| `emby-button` | 11 | 8 | 612–629, 656–674, 3062, 3123–3130, 3500, 3535, 3688, 4232 |
| `detailLogo` | 17 | 7 | 686, 1971–1982, 2017–2026, 2127–2157, 2227, 2262–2308, 2376 |
| `loginPage` | 15 | 7 | 3633, 5508–5523, 5562, 5590–5609, 6316, 6359, 6671–6698 |
| `nowPlayingBar` | 7 | 7 | 2986, 5741, 6326, 6414, 6498, 6524, 6786 |
| `listItem` | 17 | 6 | 302, 629, 2393, 4134–4160, 4191–4223, 6804–6821 |
| `navMenuOption` | 12 | 6 | 629, 725–735, 3874, 4201–4223, 4289–4294, 6584–6595 |
| `verticalSection` | 11 | 6 | 1712, 2624–2629, 4595, 6372, 6464, 6708 |
| `button-link` | 10 | 6 | 629, 656–674, 2936–2945, 3006–3016, 3062, 6977 |
| `person` | 8 | 6 | 1957–1967, 2127, 2380, 2425–2434, 3761, 7009 |
| `mainDrawer` | 7 | 6 | 2950, 3838, 4072, 6316–6326, 6571, 6610 |
| `detailImageContainer` | 20 | 5 | 1957–1967, 2031–2095, 2127, 2367–2389, 2416–2443 |
| `osdHeader` | 15 | 5 | 1681–1699, 5893–5962, 5988–6013, 6363, 6786 |
| `actionSheetMenuItem` | 11 | 5 | 629, 4134–4145, 4191, 4269–4285, 6344 |
| `sectionTabs` | 10 | 5 | 1755, 3612, 4099, 5934–5939, 6079–6105 |
| `cardImageIcon` | 8 | 5 | 412–416, 2380–2389, 2449, 3348, 5689 |
| `headerTop` | 8 | 5 | 4039, 4072, 5904–5929, 5980–5997, 6024–6028 |
| `paper-icon-button-light` | 8 | 5 | 574–629, 1638, 1708, 1786, 4990 |
| `sectionTitle` | 7 | 5 | 1712, 1765–1772, 3940, 4668–4676, 5557 |
| `emby-scroller-container` | 6 | 5 | 1712–1717, 1744, 2614, 6372, 6464 |
| `portraitCard` | 5 | 5 | 1062, 1140, 1876, 2091, 2723 |
| `scss` | 5 | 5 | 284, 768, 1014, 3370, 6464 |
| `skinHeader-withBackground` | 5 | 5 | 1620, 3809, 5504, 5893, 5943 |
| `btnPlay` | 16 | 4 | 511–535, 574–629, 3564–3606, 3639–3666 |
| `cardOverlayContainer` | 12 | 4 | 915–947, 992–1014, 1074, 6786–6804 |
| `itemName` | 11 | 4 | 686, 2198, 5077–5123, 5214–5231 |
| `backdropImage` | 10 | 4 | 2514–2541, 2568–2572, 6280, 6380–6388 |
| `emby-tab-button` | 10 | 4 | 629, 696–705, 3612, 6064–6100 |
| `upNextContainer` | 10 | 4 | 4760–4779, 4805–4831, 6316–6326, 6352 |
| `emby-scroller` | 9 | 4 | 1717, 1744–1750, 6614–6661, 6772–6781 |
| `detailRibbon` | 7 | 4 | 1577–1605, 1791, 1876–1881, 7009 |
| `listItemBodyText` | 7 | 4 | 4155–4174, 4214, 4273, 6821 |
| `visualCardBox` | 7 | 4 | 420, 820–833, 859–864, 988 |
| `button-submit` | 6 | 4 | 3633, 3720, 5590–5598, 6889–6903 |
| `cardText-secondary` | 6 | 4 | 302, 902, 3353–3357, 6442–6450 |
| `detailPagePrimaryContent` | 6 | 4 | 1592–1610, 2332, 4589, 6528 |
| `skip-button` | 6 | 4 | 629, 3617, 4854–4871, 4898–4904 |
| `squareCard` | 6 | 4 | 843, 2380, 2416–2434, 5566–5570 |
| `skinHeader-blurred` | 5 | 4 | 5504, 5922–5929, 6512, 6786 |
| `appfooter` | 4 | 4 | 2666, 6038, 6403, 6786 |
| `raised` | 4 | 4 | 629, 715, 3500, 3535 |
| `detailButton` | 13 | 3 | 574–629, 3545–3606, 3662–3666 |
| `itemBackdrop` | 9 | 3 | 1923–1967, 2100, 2443 |
| `itemSelectionPanel` | 9 | 3 | 872–876, 3293, 3321–3364 |
| `check` | 8 | 3 | 3321, 3554, 4265–4285 |
| `pageTitle` | 8 | 3 | 1656–1699, 5954, 6013 |
| `sectionTitleTextButton` | 8 | 3 | 4651–4659, 4686–4698, 4732–4742 |
| `backgroundContainer` | 7 | 3 | 2505, 2546–2564, 2596 |
| `homePage` | 7 | 3 | 4039, 4072–4099, 6122 |
| `playedIndicator` | 7 | 3 | 768–782, 3437, 6545–6566 |
| `detailSectionContent` | 6 | 3 | 3155, 4390–4400, 4480–4490 |
| `emby-checkbox` | 6 | 3 | 3298, 3335–3339, 3388–3400 |
| `actionSheetContent` | 5 | 3 | 4257–4261, 6316–6326, 6352 |
| `cardText-first` | 5 | 3 | 902, 3327–3353, 5670 |
| `dialog` | 5 | 3 | 3205–3215, 6316–6326, 6352 |
| `guideProgramName` | 5 | 3 | 629, 5255–5266, 5309–5314 |
| `musicParentName` | 5 | 3 | 1957, 2438–2443, 5196–5205 |
| `noHomeButtonHeader` | 5 | 3 | 1638, 5954, 6064–6072 |
| `overflowBackdropCard` | 5 | 3 | 941–947, 3331, 5665–5670 |
| `secondary` | 5 | 3 | 302, 4164–4174, 4214 |
| `album` | 4 | 3 | 2127, 2385–2389, 2425 |
| `cardPadder` | 4 | 3 | 416, 988, 3344–3348 |
| `cardText` | 4 | 3 | 902–912, 3353, 6687 |
| `detailPageContent` | 4 | 3 | 1734, 4321, 4582–4589 |
| `dialog-fullscreen` | 4 | 3 | 3215, 6316–6326, 6352 |
| `emby-scrollbuttons` | 4 | 3 | 1777–1782, 6708, 7161 |
| `formDialogFooter` | 4 | 3 | 3273, 3727, 6838–6862 |
| `infoWrapper` | 4 | 3 | 2070–2075, 2332, 2360 |
| `listItemImage` | 4 | 3 | 2700–2705, 4128, 6821 |
| `semiTransparent` | 4 | 3 | 1620, 5504, 5922–5943 |
| `toast` | 4 | 3 | 4752, 6316–6326, 6352 |
| `cardFooter` | 3 | 3 | 3364, 6420, 6455 |
| `defaultCardBackground` | 3 | 3 | 3475, 5685, 5784 |
| `detailPageSecondaryContainer` | 3 | 3 | 1587, 1614, 1734 |
| `folder` | 3 | 3 | 1876, 3454, 3518 |
| `formDialogFooterItem` | 3 | 3 | 3273, 3513, 3639 |
| `formDialogHeader` | 3 | 3 | 3727, 6786, 6838 |
| `iconOsd` | 3 | 3 | 5482, 6786, 6838 |
| `itemsContainer` | 3 | 3 | 740, 1759, 4595 |
| `live_tv` | 3 | 3 | 1957, 2425, 3761 |
| `myPreferencesMenuPage` | 3 | 3 | 389, 4299, 4603 |
| `page` | 3 | 3 | 984, 2596, 6372 |
| `playerStats` | 3 | 3 | 5482, 6838, 6874 |
| `sectionTitle-cards` | 3 | 3 | 1712, 4668, 4728 |
| `x` | 3 | 3 | 2198, 5179, 6464 |
| `itemExternalLinks` | 13 | 2 | 2999–3077, 3155 |
| `checkboxOutline` | 10 | 2 | 3298–3339, 3370–3400 |
| `mdl-slider` | 9 | 2 | 2796, 2851–2909 |
| `listItemIcon` | 8 | 2 | 3757–3761, 4269–4299 |
| `sliderContainer` | 8 | 2 | 2800, 2828–2893 |
| `cardOverlayButton-br` | 7 | 2 | 1000, 1029–1067 |
| `detail-clamp-text` | 7 | 2 | 3091–3117, 3143–3147 |
| `divUsers` | 7 | 2 | 5566–5570, 6671–6698 |
| `multiSelectCheckboxOutline` | 7 | 2 | 3335–3339, 3369–3388 |
| `detailPagePrimaryContainer` | 6 | 2 | 1564–1610, 2332 |
| `detailsGroupItem` | 6 | 2 | 4352, 4420–4457 |
| `headerButton` | 6 | 2 | 549–629, 6006 |
| `headerLeft` | 6 | 2 | 1662–1699, 6209 |
| `trackSelections` | 6 | 2 | 4325–4352, 4485–4490 |
| `withBackdrop` | 6 | 2 | 2505, 2546–2564 |
| `countIndicator` | 5 | 2 | 759–782, 6838–6862 |
| `detailSection` | 5 | 2 | 4308–4317, 4470–4490 |
| `fullSyncIndicator` | 5 | 2 | 759–782, 6838–6862 |
| `mainDrawer-scrollContainer` | 5 | 2 | 2959, 6584–6601 |
| `mediaInfoItem` | 5 | 2 | 1795–1838, 6464 |
| `overview-expand` | 5 | 2 | 3123–3147, 4390 |
| `videoIndicator` | 5 | 2 | 3443–3471, 6838 |
| `withSectionTabs` | 5 | 2 | 2555–2572, 5929 |
| `alphaPickerButton` | 4 | 2 | 629, 4529–4541 |
| `backgroundProgress` | 4 | 2 | 2711–2723, 2753 |
| `emby-tab-button-active` | 4 | 2 | 3699, 6091–6105 |
| `mediaSourceIndicator` | 4 | 2 | 759–782, 6838 |
| `play_arrow` | 4 | 2 | 3480–3496, 3666 |
| `playbackProgress` | 4 | 2 | 2711–2723, 2758 |
| `playlistIndexIndicatorImage` | 4 | 2 | 4155–4160, 5778–5784 |
| `programCell` | 4 | 2 | 5246, 5305–5314 |
| `programGuideSection` | 4 | 2 | 2393–2408, 4490–4505 |
| `scrollX` | 4 | 2 | 1717, 1744–1755 |
| `section0` | 4 | 2 | 954–984, 6372 |
| `visualLoginForm` | 4 | 2 | 5557–5574, 5615 |
| `cardOverlayButtonIcon` | 3 | 2 | 1000–1012, 1067 |
| `castCollapsible` | 3 | 2 | 811, 3339–3348 |
| `emby-input` | 3 | 2 | 5004–5020, 6903 |
| `emby-scrollbuttons-button` | 3 | 2 | 1786, 7168–7175 |
| `guestCastContent` | 3 | 2 | 811, 3339–3348 |
| `guide-channelHeaderCell` | 3 | 2 | 629, 5280–5296 |
| `guide-date-tab-button` | 3 | 2 | 629, 3699–3707 |
| `headerUserButton` | 3 | 2 | 549–562, 4607 |
| `manualLoginForm` | 3 | 2 | 5557–5574, 5615 |
| `overview` | 3 | 2 | 3143–3147, 4400 |
| `selectionCommandsPanel` | 3 | 2 | 3283–3289, 6786 |
| `add` | 2 | 2 | 1717, 6464 |
| `alphaPicker-fixed-right` | 2 | 2 | 2596, 4541 |
| `backdropImageFadeIn` | 2 | 2 | 2650, 6878 |
| `book` | 2 | 2 | 1957, 2425 |
| `btnDeleteImage` | 2 | 2 | 3500, 3713 |
| `cardContent` | 2 | 2 | 811, 843 |
| `cardOverlayButton` | 2 | 2 | 1014, 1050 |
| `cardOverlayButton-hover` | 2 | 2 | 897, 1029 |
| `chevron_right` | 2 | 2 | 4698, 4742 |
| `classList` | 2 | 2 | 1717, 6464 |
| `collapseContent` | 2 | 2 | 3278, 3725 |
| `content-primary` | 2 | 2 | 4582, 4634 |
| `editorsChoiceItemOverview` | 2 | 2 | 7098, 7179 |
| `emby-select` | 2 | 2 | 5004, 6903 |
| `endsAt` | 2 | 2 | 1816, 6464 |
| `fieldDescription` | 2 | 2 | 302, 6903 |
| `formDialogFooter-clear` | 2 | 2 | 3273, 3727 |
| `guide-programNameCaret` | 2 | 2 | 302, 5262 |
| `headroom` | 2 | 2 | 5917, 5954 |
| `mediaInfoOfficialRating` | 2 | 2 | 1816, 6464 |
| `navMenuOption-selected` | 2 | 2 | 4304, 6595 |
| `nowPlayingInfoContainer` | 2 | 2 | 2990, 5715 |
| `org` | 2 | 2 | 3026, 3056 |
| `paperList` | 2 | 2 | 820, 3738 |
| `playlist` | 2 | 2 | 4150, 5693 |
| `programSecondaryTitle` | 2 | 2 | 302, 5314 |
| `queue` | 2 | 2 | 1957, 2425 |
| `readOnlyContent` | 2 | 2 | 3769, 6138 |
| `recordingFields` | 2 | 2 | 4344, 4485 |
| `runtime` | 2 | 2 | 5627, 5655 |
| `sectionTitleContainer` | 2 | 2 | 1782, 4514 |
| `sectionTitleContainer-cards` | 2 | 2 | 4663, 4728 |
| `sidebarHeader` | 2 | 2 | 3861, 6601 |
| `tagline` | 2 | 2 | 2496, 4400 |
| `tsx` | 2 | 2 | 4039, 4103 |
| `upNextDialog-title` | 2 | 2 | 4784, 4818 |
| `vertical-list` | 2 | 2 | 1759, 7004 |
| `videoOsdBottom` | 2 | 2 | 2982, 5884 |
| `videoOsdBottom-maincontrols` | 2 | 2 | 2982, 5884 |
| `userPreferencesPage` | 12 | 1 | 6889–6984 |
| `checkboxContainer` | 7 | 1 | 3327–3364 |
| `itemDetailsGroup` | 7 | 1 | 4404–4490 |
| `itemProgressBar` | 6 | 1 | 2700–2734 |
| `trackSelectionFieldContainer` | 6 | 1 | 4363–4386 |
| `editorsChoiceScrollButtonsContainer` | 5 | 1 | 7135–7175 |
| `innerCardFooter` | 5 | 1 | 3168–3197 |
| `chapterCardImageContainer` | 4 | 1 | 3168–3197 |
| `endTimeText` | 4 | 1 | 5627–5655 |
| `mainDetailButtons` | 4 | 1 | 3662–3676 |
| `overview-controls` | 4 | 1 | 3143–3155 |
| `startTimeText` | 4 | 1 | 5627–5649 |
| `button-flat` | 3 | 1 | 2963–2973 |
| `cardIndicators` | 3 | 1 | 3417–3427 |
| `cardOverlayFab-primary` | 3 | 1 | 992–1014 |
| `com` | 3 | 1 | 3032–3050 |
| `content` | 3 | 1 | 4426–4457 |
| `discover-card` | 3 | 1 | 7186–7209 |
| `emby-select-withcolor` | 3 | 1 | 5004–5038 |
| `emby-textarea` | 3 | 1 | 4995–5020 |
| `fab` | 3 | 1 | 3522–3535 |
| `listChildrenCollapsible` | 3 | 1 | 4475–4490 |
| `mdl-slider-background-flex` | 3 | 1 | 2820–2833 |
| `mediaInfoCriticRating` | 3 | 1 | 1857–1866 |
| `nextUpSection` | 3 | 1 | 4470–4490 |
| `nowPlayingPageImageContainerNoAlbum` | 3 | 1 | 5679–5689 |
| `serverInfo` | 3 | 1 | 3742–3751 |
| `transcodingProgress` | 3 | 1 | 2711–2723 |
