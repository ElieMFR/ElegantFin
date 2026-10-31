# Index des composants — ElegantFin Cinema Edition v1.5.4

Généré par `python scripts/component-index.py`. **Ne pas éditer à la main.**

Les règles d'un même composant sont réparties en couches sur tout le fichier :
l'ordre porte la cascade, c'est voulu, il ne faut pas les regrouper. Mais avant
de modifier le style d'un composant, il faut avoir vu **toutes** ses règles —
sinon on en corrige une pendant qu'une autre, ailleurs, continue de gagner.
C'est exactement ce qui a produit la régression v1.2.88 sur le bouton skip,
dont les huit règles s'étalaient sur 3 700 lignes.

Source indexée : `ElegantFin-cinema-v1.5.4.css` — 8106 lignes.

| Composant | Règles | Zones | Lignes |
|---|---:|---:|---|
| `card` | 38 | 16 | 457–468, 499–545, 783, 900, 1560–1580, 2194–2227, 2254–2258, 2535–2553, 2589, 6948, 6984–6994, 7230–7249, 7327–7349, 7379–7386, 7550, 7984 |
| `cardScalable` | 31 | 13 | 457–468, 522–545, 846–890, 916–960, 2553, 3635, 3746, 3825, 6013, 6962–6994, 7065, 7230, 7370–7386 |
| `material-icons` | 17 | 13 | 393–412, 1785, 1883, 1936, 3592, 3751, 3825–3831, 3938, 4101, 4656, 5192, 5226–5236, 5830 |
| `cardImageContainer` | 21 | 12 | 517, 868, 896–925, 960, 1017–1041, 6168–6172, 6252, 6954, 7057–7065, 7105, 7230–7249, 7370 |
| `itemDetailPage` | 20 | 12 | 1623, 1709, 1794, 1821, 2050–2090, 2125–2140, 2176–2180, 2290, 2602, 4779, 5085, 7804–7842 |
| `skinHeader` | 20 | 12 | 296, 1709, 4081–4097, 4468, 4514–4541, 6021–6025, 6461, 6517–6525, 6595–6620, 7048, 7197, 7913 |
| `js` | 13 | 12 | 330, 360, 1695–1709, 1794, 2361, 2967, 3396, 3725, 5830, 6826, 7149, 7396 |
| `nameContainer` | 27 | 9 | 729, 2297–2320, 2361, 2390, 2425–2472, 2509, 2540–2544, 5586–5639, 7804–7842 |
| `cardBox` | 13 | 9 | 457–468, 499–511, 537, 783, 938–942, 1046, 6948, 7230, 7615 |
| `emby-button` | 12 | 9 | 655–672, 699–717, 3229, 3364–3371, 3771, 3806, 3960, 4674, 5408 |
| `card-hoverable` | 23 | 8 | 545, 856, 916–1010, 6172, 6972, 7105–7140, 7230, 7615 |
| `parentName` | 23 | 8 | 729, 2302–2320, 2361, 2390, 2425–2472, 5592–5639, 5712, 7804–7842 |
| `detailLogo` | 20 | 8 | 729, 2079–2090, 2125–2140, 2167–2180, 2290–2320, 2390, 2425–2472, 2540 |
| `listItem` | 19 | 8 | 314, 672, 2557, 4576–4602, 4633–4665, 4710, 4754, 7592–7609 |
| `detailPageWrapperContainer` | 17 | 8 | 729, 1591–1601, 2090, 2263, 2297–2320, 2390, 2425–2472, 2540 |
| `subtitle` | 17 | 8 | 2050–2060, 2176–2180, 2302, 2361, 2481–2491, 2602, 5647–5680, 7804–7842 |
| `backdropCard` | 12 | 8 | 1004–1010, 1127, 2050–2060, 2206, 2290, 2544–2553, 2580, 2890 |
| `nowPlayingBar` | 8 | 8 | 330, 3153, 6304, 7011, 7099, 7183, 7209, 7555 |
| `loginPage` | 18 | 7 | 3904, 6025–6059, 6099–6117, 6153–6172, 7001, 7044, 7359–7386 |
| `navMenuOption` | 12 | 6 | 672, 768–778, 4151, 4643–4665, 4760–4765, 7272–7283 |
| `emby-tab-button` | 11 | 6 | 672, 739–748, 3883, 6671–6682, 6710–6727, 7925 |
| `paper-icon-button-light` | 11 | 6 | 617–672, 1709, 1785, 1883, 3532–3552, 5492 |
| `verticalSection` | 11 | 6 | 1789, 2792–2797, 5085, 7057, 7149, 7396 |
| `button-link` | 10 | 6 | 672, 699–717, 3103–3112, 3173–3183, 3229, 7766 |
| `headerTop` | 9 | 6 | 2180, 4468, 4514, 6467–6492, 6587–6604, 6631–6635 |
| `person` | 8 | 6 | 2050–2075, 2290, 2544, 2589–2598, 4033, 7799 |
| `mainDrawer` | 7 | 6 | 3117, 4115, 4514, 7001–7011, 7259, 7298 |
| `scss` | 6 | 6 | 296, 811, 1072, 3641, 4157, 7149 |
| `detailImageContainer` | 20 | 5 | 2050–2075, 2194–2258, 2290, 2531–2553, 2580–2598 |
| `osdHeader` | 15 | 5 | 1758–1776, 6456–6525, 6595–6620, 7048, 7555 |
| `cardOverlayContainer` | 12 | 5 | 978–1010, 1050–1072, 1145, 7555, 7592 |
| `sectionTabs` | 11 | 5 | 1852, 3883, 4541, 6497–6502, 6688–6732 |
| `actionSheetMenuItem` | 10 | 5 | 672, 4576–4587, 4633, 4710–4754, 7029 |
| `cardImageIcon` | 8 | 5 | 449–453, 2544–2553, 2616, 3619, 6252 |
| `sectionTitle` | 7 | 5 | 1789, 1862–1869, 4369, 5162–5170, 6094 |
| `semiTransparent` | 7 | 5 | 1691, 4081–4097, 6021, 6485–6506, 6542 |
| `emby-scroller-container` | 6 | 5 | 1789–1794, 1832, 2782, 7057, 7149 |
| `portraitCard` | 6 | 5 | 1127, 1211, 1974–1979, 2254, 2890 |
| `appfooter` | 5 | 5 | 330, 2833, 6645, 7088, 7555 |
| `skinHeader-withBackground` | 5 | 5 | 1691, 4081, 6021, 6456, 6506 |
| `btnPlay` | 16 | 4 | 554–578, 617–672, 3835–3877, 3910–3938 |
| `itemName` | 11 | 4 | 729, 2361, 5592–5639, 5730–5747 |
| `backdropImage` | 10 | 4 | 2681–2709, 2736–2740, 6941, 7065–7073 |
| `upNextContainer` | 10 | 4 | 5254–5273, 5299–5325, 7001–7011, 7037 |
| `emby-scroller` | 9 | 4 | 1794, 1832–1838, 7302–7349, 7534–7550 |
| `backgroundContainer` | 8 | 4 | 2144, 2672, 2714–2732, 2764 |
| `detailRibbon` | 8 | 4 | 1648–1676, 1889, 1974–1986, 7799 |
| `listItemBodyText` | 7 | 4 | 4597–4616, 4656, 4731, 7609 |
| `skip-button` | 7 | 4 | 672, 3888, 5348–5365, 5392–5410 |
| `visualCardBox` | 7 | 4 | 457, 877–890, 916–921, 1046 |
| `button-submit` | 6 | 4 | 3904, 3992, 6153–6161, 7677–7692 |
| `cardText-secondary` | 6 | 4 | 314, 965, 3624–3628, 7127–7135 |
| `detailPagePrimaryContent` | 6 | 4 | 1663–1681, 2496, 5079, 7213 |
| `skinHeader-blurred` | 6 | 4 | 6021, 6485–6492, 7197, 7555–7574 |
| `squareCard` | 6 | 4 | 900, 2544, 2580–2598, 6122–6126 |
| `itemsContainer` | 4 | 4 | 783, 1821, 1856, 5085 |
| `raised` | 4 | 4 | 672, 758, 3771, 3806 |
| `tsx` | 4 | 4 | 1127, 1709, 4468, 4545 |
| `x` | 4 | 4 | 2361, 4157, 5695, 7149 |
| `detailButton` | 13 | 3 | 617–672, 3816–3877, 3934–3938 |
| `itemSelectionPanel` | 9 | 3 | 929–933, 3564, 3592–3635 |
| `pageTitle` | 8 | 3 | 1733–1776, 6517, 6620 |
| `sectionTitleTextButton` | 8 | 3 | 5145–5153, 5180–5192, 5226–5236 |
| `homePage` | 7 | 3 | 4468, 4514–4541, 6749 |
| `playedIndicator` | 7 | 3 | 811–825, 3708, 7230–7254 |
| `check` | 6 | 3 | 3592, 3825, 4710–4754 |
| `detailSectionContent` | 6 | 3 | 3396, 4865–4875, 4958–4968 |
| `emby-checkbox` | 6 | 3 | 3569, 3606–3610, 3659–3671 |
| `actionSheetContent` | 5 | 3 | 4702–4706, 7001–7011, 7037 |
| `cardText-first` | 5 | 3 | 965, 3598–3624, 6233 |
| `dialog` | 5 | 3 | 3448–3458, 7001–7011, 7037 |
| `guideProgramName` | 5 | 3 | 672, 5771–5782, 5825–5830 |
| `noHomeButtonHeader` | 5 | 3 | 1709, 6517, 6671–6682 |
| `overflowBackdropCard` | 5 | 3 | 1004–1010, 3602, 6228–6233 |
| `secondary` | 5 | 3 | 314, 4606–4616, 4656 |
| `album` | 4 | 3 | 2290, 2549–2553, 2589 |
| `cardPadder` | 4 | 3 | 453, 1046, 3615–3619 |
| `cardText` | 4 | 3 | 965–975, 3624, 7375 |
| `detailPageContent` | 4 | 3 | 1811, 4792, 5072–5079 |
| `dialog-fullscreen` | 4 | 3 | 3458, 7001–7011, 7037 |
| `emby-scrollbuttons` | 4 | 3 | 1874–1879, 7396, 7959 |
| `folder` | 4 | 3 | 1974–1979, 3725, 3789 |
| `formDialogFooter` | 4 | 3 | 3516, 3999, 7626–7650 |
| `infoWrapper` | 4 | 3 | 2233–2238, 2496, 2524 |
| `listItemImage` | 4 | 3 | 2867–2872, 4570, 7609 |
| `musicParentName` | 4 | 3 | 2050, 2602, 5712–5721 |
| `programGuideSection` | 4 | 3 | 2557–2572, 4968, 4995 |
| `toast` | 4 | 3 | 5246, 7001–7011, 7037 |
| `cardFooter` | 3 | 3 | 3635, 7105, 7140 |
| `collectionItems` | 3 | 3 | 1821, 4968, 5004 |
| `defaultCardBackground` | 3 | 3 | 3746, 6248, 6347 |
| `detailPageSecondaryContainer` | 3 | 3 | 1658, 1685, 1811 |
| `emby-input` | 3 | 3 | 5506, 5535, 7692 |
| `formDialogFooterItem` | 3 | 3 | 3516, 3784, 3910 |
| `formDialogHeader` | 3 | 3 | 3999, 7555, 7626 |
| `iconOsd` | 3 | 3 | 5999, 7555, 7626 |
| `live_tv` | 3 | 3 | 2050, 2589, 4033 |
| `myPreferencesMenuPage` | 3 | 3 | 426, 4770, 5093 |
| `playerStats` | 3 | 3 | 5999, 7626, 7662 |
| `readOnlyContent` | 3 | 3 | 4041, 6111, 6765 |
| `sectionTitle-cards` | 3 | 3 | 1789, 5162, 5222 |
| `sectionTitleContainer` | 3 | 3 | 1821, 1879, 5004 |
| `itemExternalLinks` | 13 | 2 | 3166–3244, 3396 |
| `checkboxOutline` | 10 | 2 | 3569–3610, 3641–3671 |
| `itemBackdrop` | 9 | 2 | 2016–2075, 2263 |
| `mdl-slider` | 9 | 2 | 2963, 3018–3076 |
| `cardOverlayButton-br` | 8 | 2 | 1058, 1087–1138 |
| `listItemIcon` | 8 | 2 | 4029–4033, 4710–4770 |
| `sliderContainer` | 8 | 2 | 2967, 2995–3060 |
| `detail-clamp-text` | 7 | 2 | 3332–3358, 3384–3388 |
| `divUsers` | 7 | 2 | 6122–6126, 7359–7386 |
| `multiSelectCheckboxOutline` | 7 | 2 | 3606–3610, 3640–3659 |
| `countIndicator` | 6 | 2 | 802–832, 7626–7650 |
| `detailPagePrimaryContainer` | 6 | 2 | 1635–1681, 2496 |
| `detailsGroupItem` | 6 | 2 | 4827, 4898–4935 |
| `headerButton` | 6 | 2 | 592–672, 6613 |
| `headerLeft` | 6 | 2 | 1739–1776, 6870 |
| `selectionCommandsPanel` | 6 | 2 | 3526–3560, 7555 |
| `trackSelections` | 6 | 2 | 4796–4827, 4963–4968 |
| `withBackdrop` | 6 | 2 | 2672, 2714–2732 |
| `detailSection` | 5 | 2 | 4779–4788, 4948–4968 |
| `fullSyncIndicator` | 5 | 2 | 802–825, 7626–7650 |
| `mainDrawer-scrollContainer` | 5 | 2 | 3126, 7272–7289 |
| `manualLoginForm` | 5 | 2 | 6094–6137, 6178 |
| `mediaInfoItem` | 5 | 2 | 1893–1936, 7149 |
| `overview-expand` | 5 | 2 | 3364–3388, 4865 |
| `scrollX` | 5 | 2 | 1794, 1832–1852 |
| `videoIndicator` | 5 | 2 | 3714–3742, 7626 |
| `visualLoginForm` | 5 | 2 | 6094–6137, 6178 |
| `withSectionTabs` | 5 | 2 | 2723–2740, 6492 |
| `alphaPickerButton` | 4 | 2 | 672, 5019–5031 |
| `backgroundProgress` | 4 | 2 | 2878–2890, 2920 |
| `emby-select` | 4 | 2 | 5506–5518, 7692 |
| `emby-tab-button-active` | 4 | 2 | 3971, 6718–6732 |
| `mediaSourceIndicator` | 4 | 2 | 802–825, 7626 |
| `play_arrow` | 4 | 2 | 3751–3767, 3938 |
| `playbackProgress` | 4 | 2 | 2878–2890, 2925 |
| `playlistIndexIndicatorImage` | 4 | 2 | 4597–4602, 6341–6347 |
| `programCell` | 4 | 2 | 5762, 5821–5830 |
| `cardOverlayButtonIcon` | 3 | 2 | 1058–1070, 1138 |
| `castCollapsible` | 3 | 2 | 868, 3610–3619 |
| `emby-scrollbuttons-button` | 3 | 2 | 1883, 7966–7973 |
| `emby-textarea` | 3 | 2 | 5497–5506, 5535 |
| `guestCastContent` | 3 | 2 | 868, 3610–3619 |
| `guide-channelHeaderCell` | 3 | 2 | 672, 5796–5812 |
| `guide-date-tab-button` | 3 | 2 | 672, 3971–3979 |
| `headerUserButton` | 3 | 2 | 592–605, 5097 |
| `noHeaderRight` | 3 | 2 | 1709, 6021–6025 |
| `overview` | 3 | 2 | 3384–3388, 4875 |
| `section0` | 3 | 2 | 1017–1041, 7057 |
| `add` | 2 | 2 | 1794, 7149 |
| `alphaPicker-fixed-right` | 2 | 2 | 2764, 5031 |
| `backdropImageFadeIn` | 2 | 2 | 2817, 7666 |
| `book` | 2 | 2 | 2050, 2589 |
| `btnDeleteImage` | 2 | 2 | 3771, 3985 |
| `cardContent` | 2 | 2 | 868, 900 |
| `cardOverlayButton` | 2 | 2 | 1072, 1115 |
| `cardOverlayButton-hover` | 2 | 2 | 960, 1087 |
| `chevron_right` | 2 | 2 | 5192, 5236 |
| `classList` | 2 | 2 | 1794, 7149 |
| `collapseContent` | 2 | 2 | 3521, 3997 |
| `collectionItemsContainer` | 2 | 2 | 1821, 5008 |
| `content-primary` | 2 | 2 | 5072, 5128 |
| `editorsChoiceContainer` | 2 | 2 | 6826, 7888 |
| `editorsChoiceItemBanner` | 2 | 2 | 6826, 7574 |
| `editorsChoiceItemOverview` | 2 | 2 | 7888, 7977 |
| `endsAt` | 2 | 2 | 1914, 7149 |
| `fieldDescription` | 2 | 2 | 314, 7692 |
| `formDialogFooter-clear` | 2 | 2 | 3516, 3999 |
| `guide-programNameCaret` | 2 | 2 | 314, 5778 |
| `headroom` | 2 | 2 | 6480, 6517 |
| `indicator` | 2 | 2 | 832, 3703 |
| `mediaInfoOfficialRating` | 2 | 2 | 1914, 7149 |
| `navMenuOption-selected` | 2 | 2 | 4775, 7283 |
| `nowPlayingInfoContainer` | 2 | 2 | 3157, 6278 |
| `org` | 2 | 2 | 3193, 3223 |
| `page` | 2 | 2 | 2764, 7057 |
| `paperList` | 2 | 2 | 877, 4010 |
| `playlist` | 2 | 2 | 4592, 6256 |
| `programSecondaryTitle` | 2 | 2 | 314, 5830 |
| `queue` | 2 | 2 | 2050, 2589 |
| `reactRoot` | 2 | 2 | 4468, 6876 |
| `recordingFields` | 2 | 2 | 4819, 4963 |
| `runtime` | 2 | 2 | 6190, 6218 |
| `sectionTitleContainer-cards` | 2 | 2 | 5157, 5222 |
| `sidebarHeader` | 2 | 2 | 4138, 7289 |
| `splide` | 2 | 2 | 6826, 7933 |
| `tagline` | 2 | 2 | 2663, 4875 |
| `upNextDialog-title` | 2 | 2 | 5278, 5312 |
| `vertical-list` | 2 | 2 | 1856, 7794 |
| `vertical-wrap` | 2 | 2 | 798, 1821 |
| `videoOsdBottom` | 2 | 2 | 3149, 6447 |
| `videoOsdBottom-maincontrols` | 2 | 2 | 3149, 6447 |
| `userPreferencesPage` | 12 | 1 | 7677–7773 |
| `checkboxContainer` | 7 | 1 | 3598–3635 |
| `itemDetailsGroup` | 7 | 1 | 4882–4968 |
| `itemProgressBar` | 6 | 1 | 2867–2901 |
| `streaming-lookup-container` | 6 | 1 | 3251–3296 |
| `trackSelectionFieldContainer` | 6 | 1 | 4838–4861 |
| `editorsChoiceScrollButtonsContainer` | 5 | 1 | 7933–7973 |
| `innerCardFooter` | 5 | 1 | 3411–3440 |
| `chapterCardImageContainer` | 4 | 1 | 3411–3440 |
| `emby-select-withcolor` | 4 | 1 | 5506–5553 |
| `endTimeText` | 4 | 1 | 6190–6218 |
| `mainDetailButtons` | 4 | 1 | 3934–3948 |
| `overview-controls` | 4 | 1 | 3384–3396 |
| `startTimeText` | 4 | 1 | 6190–6212 |
| `button-flat` | 3 | 1 | 3130–3140 |
| `cardIndicators` | 3 | 1 | 3688–3698 |
| `cardOverlayFab-primary` | 3 | 1 | 1050–1072 |
| `com` | 3 | 1 | 3199–3217 |
| `content` | 3 | 1 | 4904–4935 |
| `discover-card` | 3 | 1 | 7984–8007 |
| `fab` | 3 | 1 | 3793–3806 |
| `listChildrenCollapsible` | 3 | 1 | 4953–4968 |
| `mdl-slider-background-flex` | 3 | 1 | 2987–3000 |
| `mediaInfoCriticRating` | 3 | 1 | 1955–1964 |
| `nextUpSection` | 3 | 1 | 4948–4968 |
| `nowPlayingPageImageContainerNoAlbum` | 3 | 1 | 6242–6252 |
| `serverInfo` | 3 | 1 | 4014–4023 |
| `transcodingProgress` | 3 | 1 | 2878–2890 |
