# Index des composants — ElegantFin Cinema Edition v1.2.98

Généré par `python scripts/component-index.py`. **Ne pas éditer à la main.**

Les règles d'un même composant sont réparties en couches sur tout le fichier :
l'ordre porte la cascade, c'est voulu, il ne faut pas les regrouper. Mais avant
de modifier le style d'un composant, il faut avoir vu **toutes** ses règles —
sinon on en corrige une pendant qu'une autre, ailleurs, continue de gagner.
C'est exactement ce qui a produit la régression v1.2.88 sur le bouton skip,
dont les huit règles s'étalaient sur 3 700 lignes.

Source indexée : `ElegantFin-cinema-v1.2.98.css` — 6303 lignes.

| Composant | Règles | Zones | Lignes |
|---|---:|---:|---|
| `card` | 32 | 14 | 383–394, 426–438, 616, 698, 1332–1352, 1841–1874, 1901–1905, 2180–2211, 5493, 5780–5796, 5876–5898, 5928, 6000, 6273 |
| `cardScalable` | 25 | 13 | 383–394, 431–438, 644–688, 714–752, 2198, 3095, 3197, 3276, 4782, 5507–5517, 5586, 5780, 5919–5928 |
| `cardImageContainer` | 23 | 13 | 426, 666, 694–723, 752, 809–839, 4891–4895, 4976, 5499, 5578–5586, 5639, 5780–5796, 5919, 6048 |
| `material-icons` | 15 | 11 | 319–338, 1537, 1596, 1648, 3058, 3202, 3276–3282, 3388, 3641, 4091, 4125–4135 |
| `itemDetailPage` | 16 | 10 | 1395, 1467, 1546, 1767–1792, 1836, 1936, 2226–2231, 3735, 4012, 6101–6139 |
| `nameContainer` | 27 | 9 | 575, 1943–1966, 2007, 2036, 2071–2117, 2154, 2185–2189, 4458–4510, 6101–6139 |
| `card-hoverable` | 23 | 8 | 438, 654, 714–802, 4895, 5517, 5667–5686, 5780, 6055 |
| `parentName` | 23 | 8 | 575, 1948–1966, 2007, 2036, 2071–2117, 4464–4510, 4583, 6101–6139 |
| `detailPageWrapperContainer` | 17 | 8 | 575, 1363–1373, 1792, 1910, 1943–1966, 2036, 2071–2117, 2185 |
| `subtitle` | 16 | 8 | 1767, 1836, 1948, 2007, 2126–2136, 2226–2231, 4518–4551, 6101–6139 |
| `cardBox` | 11 | 8 | 383–394, 420–438, 616, 736, 843, 5493, 5780, 6055 |
| `detailLogo` | 17 | 7 | 575, 1781–1792, 1827–1836, 1936–1966, 2036, 2071–2117, 2185 |
| `loginPage` | 14 | 7 | 3355, 4794–4809, 4848, 4876–4895, 5522, 5565, 5908–5928 |
| `backdropCard` | 12 | 7 | 796–802, 905, 1767, 1853, 1936, 2189–2231, 2501 |
| `skinHeader` | 11 | 7 | 4790, 5119, 5175–5183, 5209–5234, 5569, 5748, 6210 |
| `emby-button` | 9 | 7 | 512–529, 556, 2860–2867, 3222, 3257, 3410, 3659 |
| `verticalSection` | 11 | 6 | 1541, 2397–2402, 4012, 5578, 5695, 5936 |
| `nowPlayingBar` | 8 | 6 | 2745, 5028, 5532, 5626, 5729–5760, 6005 |
| `js` | 6 | 6 | 286, 1467, 2007, 2559, 5695, 5936 |
| `listItem` | 16 | 5 | 529, 2202, 3559–3585, 3616–3650, 6023–6040 |
| `osdHeader` | 15 | 5 | 1518–1528, 5114–5183, 5209–5234, 5569, 6005 |
| `actionSheetMenuItem` | 11 | 5 | 529, 3559–3570, 3616, 3696–3712, 5550 |
| `navMenuOption` | 11 | 5 | 529, 605–611, 3622–3650, 3716–3721, 5819–5830 |
| `cardImageIcon` | 8 | 5 | 375–379, 2189–2198, 2237, 3085, 4976 |
| `person` | 8 | 5 | 1767–1777, 1936, 2189–2222, 3477, 6096 |
| `emby-scroller-container` | 7 | 5 | 1541–1554, 2387, 2423, 5578, 5695 |
| `paper-icon-button-light` | 7 | 5 | 488–529, 1467, 1537, 1596, 4377 |
| `portraitCard` | 5 | 5 | 905, 983, 1686, 1901, 2501 |
| `detailImageContainer` | 19 | 4 | 1767–1777, 1841–1905, 1936, 2176–2231 |
| `btnPlay` | 14 | 4 | 449, 488–529, 3286–3328, 3361–3388 |
| `cardOverlayContainer` | 12 | 4 | 770–802, 847–867, 917, 6005–6023 |
| `itemName` | 11 | 4 | 575, 2007, 4464–4510, 4601–4618 |
| `backdropImage` | 10 | 4 | 2303–2330, 2357–2361, 5486, 5586–5594 |
| `upNextContainer` | 10 | 4 | 4153–4172, 4198–4224, 5522–5532, 5558 |
| `emby-tab-button` | 9 | 4 | 529, 585, 3334, 5285–5321 |
| `sectionTabs` | 9 | 4 | 1565, 3334, 5155–5160, 5300–5326 |
| `button-link` | 7 | 4 | 529, 556, 2695–2704, 2765–2775 |
| `detailRibbon` | 7 | 4 | 1420–1448, 1601, 1686–1691, 6096 |
| `listItemBodyText` | 7 | 4 | 3580–3599, 3641, 3700, 6040 |
| `visualCardBox` | 7 | 4 | 383, 675–688, 714–719, 843 |
| `detailPagePrimaryContent` | 6 | 4 | 1435–1453, 2141, 4006, 5764 |
| `skip-button` | 6 | 4 | 529, 3339, 4247–4264, 4291–4297 |
| `button-submit` | 5 | 4 | 3355, 3442, 4876–4884, 6071 |
| `mainDrawer` | 5 | 4 | 2709, 5522–5532, 5806, 5845 |
| `sectionTitle` | 5 | 4 | 1541, 1575–1582, 4071, 4843 |
| `skinHeader-blurred` | 5 | 4 | 4790, 5143–5150, 5748, 6005 |
| `appfooter` | 4 | 4 | 2444, 5259, 5609, 6005 |
| `page` | 4 | 4 | 839, 2378, 2423, 5578 |
| `raised` | 4 | 4 | 529, 595, 3222, 3257 |
| `skinHeader-withBackground` | 4 | 4 | 1463, 4790, 5114, 5164 |
| `detailButton` | 12 | 3 | 488–529, 3267–3328, 3384–3388 |
| `emby-scroller` | 9 | 3 | 1546–1560, 5851–5898, 5991–6000 |
| `itemBackdrop` | 9 | 3 | 1733–1777, 1910, 2231 |
| `check` | 8 | 3 | 3058, 3276, 3692–3712 |
| `itemSelectionPanel` | 8 | 3 | 727–731, 3030, 3058–3095 |
| `pageTitle` | 8 | 3 | 1492–1528, 5175, 5234 |
| `detailSectionContent` | 6 | 3 | 2892, 3817–3827, 3908–3918 |
| `emby-checkbox` | 6 | 3 | 3035, 3072–3076, 3118–3130 |
| `headerTop` | 6 | 3 | 5125–5150, 5201–5218, 5245–5249 |
| `squareCard` | 6 | 3 | 698, 2189–2222, 4852–4856 |
| `actionSheetContent` | 5 | 3 | 3684–3688, 5522–5532, 5558 |
| `cardText-first` | 5 | 3 | 757, 3064–3090, 4957 |
| `dialog` | 5 | 3 | 2942–2952, 5522–5532, 5558 |
| `guideProgramName` | 5 | 3 | 529, 4642–4653, 4696–4701 |
| `musicParentName` | 5 | 3 | 1767, 2226–2231, 4583–4592 |
| `noHomeButtonHeader` | 5 | 3 | 1467, 5175, 5285–5293 |
| `overflowBackdropCard` | 5 | 3 | 796–802, 3068, 4952–4957 |
| `cardPadder` | 4 | 3 | 379, 843, 3081–3085 |
| `cardText` | 4 | 3 | 757–767, 3090, 5924 |
| `cardText-secondary` | 4 | 3 | 757, 3090, 5673–5681 |
| `dialog-fullscreen` | 4 | 3 | 2952, 5522–5532, 5558 |
| `emby-scrollbuttons` | 4 | 3 | 1587–1592, 5936, 6248 |
| `infoWrapper` | 4 | 3 | 1880–1885, 2141, 2169 |
| `listItemImage` | 4 | 3 | 2478–2483, 3553, 6040 |
| `semiTransparent` | 4 | 3 | 1463, 4790, 5143–5164 |
| `toast` | 4 | 3 | 4145, 5522–5532, 5558 |
| `defaultCardBackground` | 3 | 3 | 3197, 4972, 5071 |
| `folder` | 3 | 3 | 1686, 3184, 3240 |
| `formDialogFooterItem` | 3 | 3 | 3010, 3235, 3361 |
| `itemsContainer` | 3 | 3 | 616, 1569, 4012 |
| `live_tv` | 3 | 3 | 1767, 2211, 3477 |
| `myPreferencesMenuPage` | 3 | 3 | 352, 3726, 4020 |
| `sectionTitle-cards` | 3 | 3 | 1541, 4071, 4121 |
| `x` | 3 | 3 | 2007, 4566, 5695 |
| `itemExternalLinks` | 11 | 2 | 2758–2815, 2892 |
| `mdl-slider` | 9 | 2 | 2555, 2610–2668 |
| `listItemIcon` | 8 | 2 | 3473–3477, 3696–3726 |
| `sectionTitleTextButton` | 8 | 2 | 4054–4091, 4125–4135 |
| `sliderContainer` | 8 | 2 | 2559, 2587–2652 |
| `detail-clamp-text` | 7 | 2 | 2828–2854, 2880–2884 |
| `backgroundContainer` | 6 | 2 | 2293, 2335–2353 |
| `detailPagePrimaryContainer` | 6 | 2 | 1407–1453, 2141 |
| `detailsGroupItem` | 6 | 2 | 3779, 3847–3885 |
| `divUsers` | 6 | 2 | 4852–4856, 5908–5928 |
| `headerLeft` | 6 | 2 | 1498–1528, 5414 |
| `trackSelections` | 6 | 2 | 3752–3779, 3913–3918 |
| `withBackdrop` | 6 | 2 | 2293, 2335–2353 |
| `detailSection` | 5 | 2 | 3735–3744, 3898–3918 |
| `headerButton` | 5 | 2 | 474–529, 5227 |
| `mainDrawer-scrollContainer` | 5 | 2 | 2718, 5819–5836 |
| `mediaInfoItem` | 5 | 2 | 1605–1648, 5695 |
| `overview-expand` | 5 | 2 | 2860–2884, 3817 |
| `playedIndicator` | 5 | 2 | 3167, 5780–5801 |
| `videoIndicator` | 5 | 2 | 3173–3193, 6062 |
| `withSectionTabs` | 5 | 2 | 2344–2361, 5150 |
| `album` | 4 | 2 | 1936, 2194–2211 |
| `emby-tab-button-active` | 4 | 2 | 3421, 5312–5326 |
| `play_arrow` | 4 | 2 | 3202–3218, 3388 |
| `playlistIndexIndicatorImage` | 4 | 2 | 3580–3585, 5065–5071 |
| `programCell` | 4 | 2 | 4633, 4692–4701 |
| `secondary` | 4 | 2 | 3589–3599, 3641 |
| `section0` | 4 | 2 | 809–839, 5578 |
| `visualLoginForm` | 4 | 2 | 4843–4860, 4901 |
| `alphaPickerButton` | 3 | 2 | 529, 3957–3964 |
| `cardFooter` | 3 | 2 | 3095, 5667–5686 |
| `castCollapsible` | 3 | 2 | 666, 3076–3085 |
| `detailPageContent` | 3 | 2 | 3748, 3999–4006 |
| `emby-scrollbuttons-button` | 3 | 2 | 1596, 6255–6262 |
| `guestCastContent` | 3 | 2 | 666, 3076–3085 |
| `guide-channelHeaderCell` | 3 | 2 | 529, 4667–4683 |
| `guide-date-tab-button` | 3 | 2 | 529, 3421–3429 |
| `manualLoginForm` | 3 | 2 | 4843–4860, 4901 |
| `overview` | 3 | 2 | 2880–2884, 3827 |
| `programGuideSection` | 3 | 2 | 2202, 3918–3933 |
| `selectionCommandsPanel` | 3 | 2 | 3020–3026, 6005 |
| `blurhash-canvas` | 2 | 2 | 5639, 6048 |
| `book` | 2 | 2 | 1767, 2211 |
| `btnDeleteImage` | 2 | 2 | 3222, 3435 |
| `cardContent` | 2 | 2 | 666, 698 |
| `cardImage` | 2 | 2 | 5639, 6048 |
| `cardOverlayButton-hover` | 2 | 2 | 752, 872 |
| `cardOverlayButtonIcon` | 2 | 2 | 855, 910 |
| `chevron_right` | 2 | 2 | 4091, 4135 |
| `collapseContent` | 2 | 2 | 3015, 3447 |
| `content-primary` | 2 | 2 | 3999, 4037 |
| `countIndicator` | 2 | 2 | 635, 5620 |
| `detailPageSecondaryContainer` | 2 | 2 | 1430, 1457 |
| `editorsChoiceItemOverview` | 2 | 2 | 6185, 6266 |
| `endsAt` | 2 | 2 | 1626, 5695 |
| `formDialogFooter` | 2 | 2 | 3010, 3447 |
| `formDialogFooter-clear` | 2 | 2 | 3010, 3447 |
| `formDialogHeader` | 2 | 2 | 3447, 6005 |
| `headerUserButton` | 2 | 2 | 474, 4024 |
| `headroom` | 2 | 2 | 5138, 5175 |
| `iconOsd` | 2 | 2 | 4768, 6005 |
| `mediaSourceIndicator` | 2 | 2 | 635, 6062 |
| `navMenuOption-selected` | 2 | 2 | 3731, 5830 |
| `nowPlayingInfoContainer` | 2 | 2 | 2749, 5002 |
| `org` | 2 | 2 | 2785, 2815 |
| `paperList` | 2 | 2 | 675, 3454 |
| `playlist` | 2 | 2 | 3575, 4980 |
| `queue` | 2 | 2 | 1767, 2211 |
| `readOnlyContent` | 2 | 2 | 3485, 5343 |
| `recordingFields` | 2 | 2 | 3771, 3913 |
| `runtime` | 2 | 2 | 4913, 4942 |
| `sectionTitleContainer` | 2 | 2 | 1592, 3942 |
| `sectionTitleContainer-cards` | 2 | 2 | 4066, 4121 |
| `tagline` | 2 | 2 | 2284, 3827 |
| `upNextDialog-title` | 2 | 2 | 4177, 4211 |
| `vertical-list` | 2 | 2 | 1569, 6091 |
| `videoOsdBottom` | 2 | 2 | 2741, 5105 |
| `videoOsdBottom-maincontrols` | 2 | 2 | 2741, 5105 |
| `checkboxOutline` | 10 | 1 | 3035–3130 |
| `cardOverlayButton-br` | 7 | 1 | 855–910 |
| `itemDetailsGroup` | 7 | 1 | 3831–3918 |
| `checkboxContainer` | 6 | 1 | 3064–3095 |
| `multiSelectCheckboxOutline` | 6 | 1 | 3072–3118 |
| `trackSelectionFieldContainer` | 6 | 1 | 3790–3813 |
| `editorsChoiceScrollButtonsContainer` | 5 | 1 | 6222–6262 |
| `innerCardFooter` | 5 | 1 | 2905–2934 |
| `itemProgressBar` | 5 | 1 | 2478–2501 |
| `backgroundProgress` | 4 | 1 | 2489–2512 |
| `chapterCardImageContainer` | 4 | 1 | 2905–2934 |
| `endTimeText` | 4 | 1 | 4913–4942 |
| `mainDetailButtons` | 4 | 1 | 3384–3398 |
| `overview-controls` | 4 | 1 | 2880–2892 |
| `playbackProgress` | 4 | 1 | 2489–2517 |
| `scrollX` | 4 | 1 | 1546–1565 |
| `startTimeText` | 4 | 1 | 4913–4936 |
| `button-flat` | 3 | 1 | 2722–2732 |
| `cardIndicators` | 3 | 1 | 3147–3157 |
| `cardOverlayFab-primary` | 3 | 1 | 847–867 |
| `com` | 3 | 1 | 2791–2809 |
| `content` | 3 | 1 | 3854–3885 |
| `discover-card` | 3 | 1 | 6273–6296 |
| `emby-select-withcolor` | 3 | 1 | 4391–4425 |
| `emby-textarea` | 3 | 1 | 4382–4407 |
| `fab` | 3 | 1 | 3244–3257 |
| `listChildrenCollapsible` | 3 | 1 | 3903–3918 |
| `mdl-slider-background-flex` | 3 | 1 | 2579–2592 |
| `mediaInfoCriticRating` | 3 | 1 | 1667–1676 |
| `nextUpSection` | 3 | 1 | 3898–3918 |
| `nowPlayingPageImageContainerNoAlbum` | 3 | 1 | 4966–4976 |
| `serverInfo` | 3 | 1 | 3458–3467 |
| `transcodingProgress` | 3 | 1 | 2489–2501 |
