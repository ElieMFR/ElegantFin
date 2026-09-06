# Index des composants — ElegantFin Cinema Edition v1.2.99

Généré par `python scripts/component-index.py`. **Ne pas éditer à la main.**

Les règles d'un même composant sont réparties en couches sur tout le fichier :
l'ordre porte la cascade, c'est voulu, il ne faut pas les regrouper. Mais avant
de modifier le style d'un composant, il faut avoir vu **toutes** ses règles —
sinon on en corrige une pendant qu'une autre, ailleurs, continue de gagner.
C'est exactement ce qui a produit la régression v1.2.88 sur le bouton skip,
dont les huit règles s'étalaient sur 3 700 lignes.

Source indexée : `ElegantFin-cinema-v1.2.99.css` — 6346 lignes.

| Composant | Règles | Zones | Lignes |
|---|---:|---:|---|
| `card` | 32 | 14 | 383–394, 426–438, 620, 702, 1348–1368, 1871–1904, 1931–1935, 2210–2241, 5536, 5823–5839, 5919–5941, 5971, 6043, 6316 |
| `cardScalable` | 25 | 13 | 383–394, 431–438, 648–692, 718–756, 2228, 3125, 3236, 3315, 4825, 5550–5560, 5629, 5823, 5962–5971 |
| `cardImageContainer` | 23 | 13 | 426, 670, 698–727, 756, 813–843, 4934–4938, 5019, 5542, 5621–5629, 5682, 5823–5839, 5962, 6091 |
| `material-icons` | 15 | 11 | 319–338, 1567, 1626, 1678, 3088, 3241, 3315–3321, 3427, 3684, 4134, 4168–4178 |
| `itemDetailPage` | 16 | 10 | 1411, 1497, 1576, 1797–1822, 1866, 1966, 2256–2261, 3778, 4055, 6144–6182 |
| `nameContainer` | 27 | 9 | 575, 1973–1996, 2037, 2066, 2101–2147, 2184, 2215–2219, 4501–4553, 6144–6182 |
| `card-hoverable` | 23 | 8 | 438, 658, 718–806, 4938, 5560, 5710–5729, 5823, 6098 |
| `parentName` | 23 | 8 | 575, 1978–1996, 2037, 2066, 2101–2147, 4507–4553, 4626, 6144–6182 |
| `detailPageWrapperContainer` | 17 | 8 | 575, 1379–1389, 1822, 1940, 1973–1996, 2066, 2101–2147, 2215 |
| `subtitle` | 16 | 8 | 1797, 1866, 1978, 2037, 2156–2166, 2256–2261, 4561–4594, 6144–6182 |
| `cardBox` | 11 | 8 | 383–394, 420–438, 620, 740, 847, 5536, 5823, 6098 |
| `detailLogo` | 17 | 7 | 575, 1811–1822, 1857–1866, 1966–1996, 2066, 2101–2147, 2215 |
| `loginPage` | 14 | 7 | 3394, 4837–4852, 4891, 4919–4938, 5565, 5608, 5951–5971 |
| `backdropCard` | 12 | 7 | 800–806, 921, 1797, 1883, 1966, 2219–2261, 2531 |
| `skinHeader` | 11 | 7 | 4833, 5162, 5218–5226, 5252–5277, 5612, 5791, 6253 |
| `emby-button` | 9 | 7 | 512–529, 556, 2890–2897, 3261, 3296, 3449, 3702 |
| `js` | 7 | 7 | 286, 1483, 2037, 2589, 3215, 5738, 5979 |
| `verticalSection` | 11 | 6 | 1571, 2427–2432, 4055, 5621, 5738, 5979 |
| `nowPlayingBar` | 8 | 6 | 2775, 5071, 5575, 5669, 5772–5803, 6048 |
| `listItem` | 16 | 5 | 529, 2232, 3604–3630, 3661–3693, 6066–6083 |
| `osdHeader` | 15 | 5 | 1540–1558, 5157–5226, 5252–5277, 5612, 6048 |
| `actionSheetMenuItem` | 11 | 5 | 529, 3604–3615, 3661, 3739–3755, 5593 |
| `navMenuOption` | 11 | 5 | 529, 605–615, 3671–3693, 3759–3764, 5862–5873 |
| `cardImageIcon` | 8 | 5 | 375–379, 2219–2228, 2267, 3115, 5019 |
| `person` | 8 | 5 | 1797–1807, 1966, 2219–2252, 3522, 6139 |
| `emby-scroller-container` | 7 | 5 | 1571–1584, 2417, 2453, 5621, 5738 |
| `paper-icon-button-light` | 7 | 5 | 488–529, 1497, 1567, 1626, 4420 |
| `portraitCard` | 5 | 5 | 921, 999, 1716, 1931, 2531 |
| `detailImageContainer` | 19 | 4 | 1797–1807, 1871–1935, 1966, 2206–2261 |
| `btnPlay` | 14 | 4 | 449, 488–529, 3325–3367, 3400–3427 |
| `cardOverlayContainer` | 12 | 4 | 774–806, 851–883, 933, 6048–6066 |
| `itemName` | 11 | 4 | 575, 2037, 4507–4553, 4644–4661 |
| `backdropImage` | 10 | 4 | 2333–2360, 2387–2391, 5529, 5629–5637 |
| `upNextContainer` | 10 | 4 | 4196–4215, 4241–4267, 5565–5575, 5601 |
| `emby-tab-button` | 9 | 4 | 529, 585, 3373, 5328–5364 |
| `sectionTabs` | 9 | 4 | 1595, 3373, 5198–5203, 5343–5369 |
| `button-link` | 7 | 4 | 529, 556, 2725–2734, 2795–2805 |
| `detailRibbon` | 7 | 4 | 1436–1464, 1631, 1716–1721, 6139 |
| `listItemBodyText` | 7 | 4 | 3625–3644, 3684, 3743, 6083 |
| `visualCardBox` | 7 | 4 | 383, 679–692, 718–723, 847 |
| `detailPagePrimaryContent` | 6 | 4 | 1451–1469, 2171, 4049, 5807 |
| `skip-button` | 6 | 4 | 529, 3378, 4290–4307, 4334–4340 |
| `button-submit` | 5 | 4 | 3394, 3481, 4919–4927, 6114 |
| `mainDrawer` | 5 | 4 | 2739, 5565–5575, 5849, 5888 |
| `sectionTitle` | 5 | 4 | 1571, 1605–1612, 4114, 4886 |
| `skinHeader-blurred` | 5 | 4 | 4833, 5186–5193, 5791, 6048 |
| `appfooter` | 4 | 4 | 2474, 5302, 5652, 6048 |
| `page` | 4 | 4 | 843, 2408, 2453, 5621 |
| `raised` | 4 | 4 | 529, 595, 3261, 3296 |
| `skinHeader-withBackground` | 4 | 4 | 1479, 4833, 5157, 5207 |
| `detailButton` | 12 | 3 | 488–529, 3306–3367, 3423–3427 |
| `emby-scroller` | 9 | 3 | 1576–1590, 5894–5941, 6034–6043 |
| `itemBackdrop` | 9 | 3 | 1763–1807, 1940, 2261 |
| `check` | 8 | 3 | 3088, 3315, 3735–3755 |
| `itemSelectionPanel` | 8 | 3 | 731–735, 3060, 3088–3125 |
| `pageTitle` | 8 | 3 | 1515–1558, 5218, 5277 |
| `detailSectionContent` | 6 | 3 | 2922, 3860–3870, 3951–3961 |
| `emby-checkbox` | 6 | 3 | 3065, 3102–3106, 3149–3161 |
| `headerTop` | 6 | 3 | 5168–5193, 5244–5261, 5288–5292 |
| `squareCard` | 6 | 3 | 702, 2219–2252, 4895–4899 |
| `actionSheetContent` | 5 | 3 | 3727–3731, 5565–5575, 5601 |
| `cardText-first` | 5 | 3 | 761, 3094–3120, 5000 |
| `dialog` | 5 | 3 | 2972–2982, 5565–5575, 5601 |
| `guideProgramName` | 5 | 3 | 529, 4685–4696, 4739–4744 |
| `musicParentName` | 5 | 3 | 1797, 2256–2261, 4626–4635 |
| `noHomeButtonHeader` | 5 | 3 | 1497, 5218, 5328–5336 |
| `overflowBackdropCard` | 5 | 3 | 800–806, 3098, 4995–5000 |
| `cardPadder` | 4 | 3 | 379, 847, 3111–3115 |
| `cardText` | 4 | 3 | 761–771, 3120, 5967 |
| `cardText-secondary` | 4 | 3 | 761, 3120, 5716–5724 |
| `dialog-fullscreen` | 4 | 3 | 2982, 5565–5575, 5601 |
| `emby-scrollbuttons` | 4 | 3 | 1617–1622, 5979, 6291 |
| `infoWrapper` | 4 | 3 | 1910–1915, 2171, 2199 |
| `listItemImage` | 4 | 3 | 2508–2513, 3598, 6083 |
| `semiTransparent` | 4 | 3 | 1479, 4833, 5186–5207 |
| `toast` | 4 | 3 | 4188, 5565–5575, 5601 |
| `defaultCardBackground` | 3 | 3 | 3236, 5015, 5114 |
| `folder` | 3 | 3 | 1716, 3215, 3279 |
| `formDialogFooterItem` | 3 | 3 | 3040, 3274, 3400 |
| `itemsContainer` | 3 | 3 | 620, 1599, 4055 |
| `live_tv` | 3 | 3 | 1797, 2241, 3522 |
| `myPreferencesMenuPage` | 3 | 3 | 352, 3769, 4063 |
| `scss` | 3 | 3 | 874, 3131, 5738 |
| `sectionTitle-cards` | 3 | 3 | 1571, 4114, 4164 |
| `x` | 3 | 3 | 2037, 4609, 5738 |
| `itemExternalLinks` | 11 | 2 | 2788–2845, 2922 |
| `mdl-slider` | 9 | 2 | 2585, 2640–2698 |
| `listItemIcon` | 8 | 2 | 3518–3522, 3739–3769 |
| `sectionTitleTextButton` | 8 | 2 | 4097–4134, 4168–4178 |
| `sliderContainer` | 8 | 2 | 2589, 2617–2682 |
| `detail-clamp-text` | 7 | 2 | 2858–2884, 2910–2914 |
| `backgroundContainer` | 6 | 2 | 2323, 2365–2383 |
| `detailPagePrimaryContainer` | 6 | 2 | 1423–1469, 2171 |
| `detailsGroupItem` | 6 | 2 | 3822, 3890–3928 |
| `divUsers` | 6 | 2 | 4895–4899, 5951–5971 |
| `headerLeft` | 6 | 2 | 1521–1558, 5457 |
| `trackSelections` | 6 | 2 | 3795–3822, 3956–3961 |
| `withBackdrop` | 6 | 2 | 2323, 2365–2383 |
| `detailSection` | 5 | 2 | 3778–3787, 3941–3961 |
| `headerButton` | 5 | 2 | 474–529, 5270 |
| `mainDrawer-scrollContainer` | 5 | 2 | 2748, 5862–5879 |
| `mediaInfoItem` | 5 | 2 | 1635–1678, 5738 |
| `overview-expand` | 5 | 2 | 2890–2914, 3860 |
| `playedIndicator` | 5 | 2 | 3198, 5823–5844 |
| `videoIndicator` | 5 | 2 | 3204–3232, 6105 |
| `withSectionTabs` | 5 | 2 | 2374–2391, 5193 |
| `album` | 4 | 2 | 1966, 2224–2241 |
| `cardOverlayButtonIcon` | 4 | 2 | 859–874, 926 |
| `emby-tab-button-active` | 4 | 2 | 3460, 5355–5369 |
| `play_arrow` | 4 | 2 | 3241–3257, 3427 |
| `playlistIndexIndicatorImage` | 4 | 2 | 3625–3630, 5108–5114 |
| `programCell` | 4 | 2 | 4676, 4735–4744 |
| `secondary` | 4 | 2 | 3634–3644, 3684 |
| `section0` | 4 | 2 | 813–843, 5621 |
| `visualLoginForm` | 4 | 2 | 4886–4903, 4944 |
| `alphaPickerButton` | 3 | 2 | 529, 4000–4007 |
| `cardFooter` | 3 | 2 | 3125, 5710–5729 |
| `castCollapsible` | 3 | 2 | 670, 3106–3115 |
| `detailPageContent` | 3 | 2 | 3791, 4042–4049 |
| `emby-scrollbuttons-button` | 3 | 2 | 1626, 6298–6305 |
| `guestCastContent` | 3 | 2 | 670, 3106–3115 |
| `guide-channelHeaderCell` | 3 | 2 | 529, 4710–4726 |
| `guide-date-tab-button` | 3 | 2 | 529, 3460–3468 |
| `manualLoginForm` | 3 | 2 | 4886–4903, 4944 |
| `overview` | 3 | 2 | 2910–2914, 3870 |
| `programGuideSection` | 3 | 2 | 2232, 3961–3976 |
| `selectionCommandsPanel` | 3 | 2 | 3050–3056, 6048 |
| `blurhash-canvas` | 2 | 2 | 5682, 6091 |
| `book` | 2 | 2 | 1797, 2241 |
| `btnDeleteImage` | 2 | 2 | 3261, 3474 |
| `cardContent` | 2 | 2 | 670, 702 |
| `cardImage` | 2 | 2 | 5682, 6091 |
| `cardOverlayButton-hover` | 2 | 2 | 756, 888 |
| `chevron_right` | 2 | 2 | 4134, 4178 |
| `collapseContent` | 2 | 2 | 3045, 3486 |
| `content-primary` | 2 | 2 | 4042, 4080 |
| `countIndicator` | 2 | 2 | 639, 5663 |
| `detailPageSecondaryContainer` | 2 | 2 | 1446, 1473 |
| `editorsChoiceItemOverview` | 2 | 2 | 6228, 6309 |
| `endsAt` | 2 | 2 | 1656, 5738 |
| `formDialogFooter` | 2 | 2 | 3040, 3488 |
| `formDialogFooter-clear` | 2 | 2 | 3040, 3488 |
| `formDialogHeader` | 2 | 2 | 3488, 6048 |
| `headerUserButton` | 2 | 2 | 474, 4067 |
| `headroom` | 2 | 2 | 5181, 5218 |
| `iconOsd` | 2 | 2 | 4811, 6048 |
| `mediaInfoOfficialRating` | 2 | 2 | 1656, 5738 |
| `mediaSourceIndicator` | 2 | 2 | 639, 6105 |
| `navMenuOption-selected` | 2 | 2 | 3774, 5873 |
| `nowPlayingInfoContainer` | 2 | 2 | 2779, 5045 |
| `org` | 2 | 2 | 2815, 2845 |
| `paperList` | 2 | 2 | 679, 3499 |
| `playlist` | 2 | 2 | 3620, 5023 |
| `queue` | 2 | 2 | 1797, 2241 |
| `readOnlyContent` | 2 | 2 | 3530, 5386 |
| `recordingFields` | 2 | 2 | 3814, 3956 |
| `runtime` | 2 | 2 | 4956, 4985 |
| `sectionTitleContainer` | 2 | 2 | 1622, 3985 |
| `sectionTitleContainer-cards` | 2 | 2 | 4109, 4164 |
| `tagline` | 2 | 2 | 2314, 3870 |
| `upNextDialog-title` | 2 | 2 | 4220, 4254 |
| `vertical-list` | 2 | 2 | 1599, 6134 |
| `videoOsdBottom` | 2 | 2 | 2771, 5148 |
| `videoOsdBottom-maincontrols` | 2 | 2 | 2771, 5148 |
| `checkboxOutline` | 10 | 1 | 3065–3161 |
| `cardOverlayButton-br` | 8 | 1 | 859–926 |
| `itemDetailsGroup` | 7 | 1 | 3874–3961 |
| `multiSelectCheckboxOutline` | 7 | 1 | 3102–3149 |
| `checkboxContainer` | 6 | 1 | 3094–3125 |
| `trackSelectionFieldContainer` | 6 | 1 | 3833–3856 |
| `editorsChoiceScrollButtonsContainer` | 5 | 1 | 6265–6305 |
| `innerCardFooter` | 5 | 1 | 2935–2964 |
| `itemProgressBar` | 5 | 1 | 2508–2531 |
| `backgroundProgress` | 4 | 1 | 2519–2542 |
| `chapterCardImageContainer` | 4 | 1 | 2935–2964 |
| `endTimeText` | 4 | 1 | 4956–4985 |
| `mainDetailButtons` | 4 | 1 | 3423–3437 |
| `overview-controls` | 4 | 1 | 2910–2922 |
| `playbackProgress` | 4 | 1 | 2519–2547 |
| `scrollX` | 4 | 1 | 1576–1595 |
| `startTimeText` | 4 | 1 | 4956–4979 |
| `button-flat` | 3 | 1 | 2752–2762 |
| `cardIndicators` | 3 | 1 | 3178–3188 |
| `cardOverlayFab-primary` | 3 | 1 | 851–883 |
| `com` | 3 | 1 | 2821–2839 |
| `content` | 3 | 1 | 3897–3928 |
| `discover-card` | 3 | 1 | 6316–6339 |
| `emby-select-withcolor` | 3 | 1 | 4434–4468 |
| `emby-textarea` | 3 | 1 | 4425–4450 |
| `fab` | 3 | 1 | 3283–3296 |
| `listChildrenCollapsible` | 3 | 1 | 3946–3961 |
| `mdl-slider-background-flex` | 3 | 1 | 2609–2622 |
| `mediaInfoCriticRating` | 3 | 1 | 1697–1706 |
| `nextUpSection` | 3 | 1 | 3941–3961 |
| `nowPlayingPageImageContainerNoAlbum` | 3 | 1 | 5009–5019 |
| `serverInfo` | 3 | 1 | 3503–3512 |
| `transcodingProgress` | 3 | 1 | 2519–2531 |
