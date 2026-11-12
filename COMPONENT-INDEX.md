# Index des composants — ElegantFin Cinema Edition v1.5.7

Généré par `python scripts/component-index.py`. **Ne pas éditer à la main.**

Les règles d'un même composant sont réparties en couches sur tout le fichier :
l'ordre porte la cascade, c'est voulu, il ne faut pas les regrouper. Mais avant
de modifier le style d'un composant, il faut avoir vu **toutes** ses règles —
sinon on en corrige une pendant qu'une autre, ailleurs, continue de gagner.
C'est exactement ce qui a produit la régression v1.2.88 sur le bouton skip,
dont les huit règles s'étalaient sur 3 700 lignes.

Source indexée : `ElegantFin-cinema-v1.5.7.css` — 8049 lignes.

| Composant | Règles | Zones | Lignes |
|---|---:|---:|---|
| `card` | 38 | 16 | 457–487, 518–553, 791, 904, 1565–1585, 2199–2232, 2259–2263, 2540–2558, 2594, 6956, 6992–7002, 7142, 7242–7261, 7339–7361, 7391–7398, 7562 |
| `cardScalable` | 29 | 14 | 457, 487, 541–553, 854–894, 920–964, 2558, 3640, 3751, 3829, 6020, 6970–7002, 7072, 7242, 7382–7398 |
| `cardImageContainer` | 21 | 13 | 468, 536, 872, 900–929, 964, 1022–1046, 6176–6180, 6260, 6962, 7072, 7112, 7242–7261, 7382 |
| `material-icons` | 17 | 13 | 393–412, 1790, 1888, 1941, 3597, 3756, 3829–3835, 3941, 4103, 4657, 5193, 5227–5237, 5837 |
| `itemDetailPage` | 20 | 12 | 1628, 1714, 1799, 1826, 2055–2095, 2130–2145, 2181–2185, 2295, 2607, 4780, 5086, 7816–7854 |
| `skinHeader` | 20 | 12 | 296, 1714, 4083–4099, 4469, 4515–4542, 6028–6032, 6469, 6525–6533, 6603–6628, 7056, 7209, 7887 |
| `js` | 13 | 12 | 330, 360, 1700–1714, 1799, 2366, 2973, 3401, 3730, 5837, 6834, 7161, 7408 |
| `nameContainer` | 27 | 9 | 737, 2302–2325, 2366, 2395, 2430–2477, 2514, 2545–2549, 5593–5646, 7816–7854 |
| `emby-button` | 12 | 9 | 663–680, 707–725, 3234, 3369–3376, 3776, 3810, 3963, 4675, 5415 |
| `parentName` | 23 | 8 | 737, 2307–2325, 2366, 2395, 2430–2477, 5599–5646, 5719, 7816–7854 |
| `detailLogo` | 20 | 8 | 737, 2084–2095, 2130–2145, 2172–2185, 2295–2325, 2395, 2430–2477, 2545 |
| `listItem` | 19 | 8 | 314, 680, 2562, 4577–4603, 4634–4666, 4711, 4755, 7604–7621 |
| `detailPageWrapperContainer` | 17 | 8 | 737, 1596–1606, 2095, 2268, 2302–2325, 2395, 2430–2477, 2545 |
| `subtitle` | 17 | 8 | 2055–2065, 2181–2185, 2307, 2366, 2486–2496, 2607, 5654–5687, 7816–7854 |
| `cardBox` | 13 | 8 | 457–487, 518–542, 791, 942–946, 1051, 6956, 7242, 7627 |
| `backdropCard` | 12 | 8 | 1009–1015, 1132, 2055–2065, 2211, 2295, 2549–2558, 2585, 2896 |
| `nowPlayingBar` | 8 | 8 | 330, 3158, 6312, 7019, 7106, 7195, 7221, 7567 |
| `card-hoverable` | 22 | 7 | 553, 920–1015, 6180, 6980, 7112–7151, 7242, 7627 |
| `loginPage` | 18 | 7 | 3907, 6032–6066, 6106–6125, 6161–6180, 7009, 7052, 7371–7398 |
| `navMenuOption` | 12 | 6 | 680, 776–786, 4152, 4644–4666, 4761–4766, 7284–7295 |
| `emby-tab-button` | 11 | 6 | 680, 747–756, 3882, 6679–6690, 6718–6735, 7899 |
| `paper-icon-button-light` | 11 | 6 | 625–680, 1714, 1790, 1888, 3537–3557, 5499 |
| `verticalSection` | 11 | 6 | 1794, 2798–2803, 5086, 7065, 7161, 7408 |
| `button-link` | 10 | 6 | 680, 707–725, 3109–3118, 3178–3188, 3234, 7778 |
| `headerTop` | 9 | 6 | 2185, 4469, 4515, 6475–6500, 6595–6612, 6639–6643 |
| `person` | 8 | 6 | 2055–2080, 2295, 2549, 2594–2603, 4035, 7811 |
| `mainDrawer` | 7 | 6 | 3123, 4117, 4515, 7009–7019, 7271, 7310 |
| `scss` | 6 | 6 | 296, 819, 1077, 3646, 4158, 7161 |
| `detailImageContainer` | 20 | 5 | 2055–2080, 2199–2263, 2295, 2536–2558, 2585–2603 |
| `osdHeader` | 15 | 5 | 1763–1781, 6464–6533, 6603–6628, 7056, 7567 |
| `cardOverlayContainer` | 12 | 5 | 983–1015, 1055–1077, 1150, 7567, 7604 |
| `sectionTabs` | 11 | 5 | 1857, 3882, 4542, 6505–6510, 6696–6740 |
| `actionSheetMenuItem` | 10 | 5 | 680, 4577–4588, 4634, 4711–4755, 7037 |
| `cardImageIcon` | 8 | 5 | 449–453, 2549–2558, 2621, 3624, 6260 |
| `sectionTitle` | 7 | 5 | 1794, 1867–1874, 4370, 5163–5171, 6101 |
| `semiTransparent` | 7 | 5 | 1696, 4083–4099, 6028, 6493–6514, 6550 |
| `emby-scroller-container` | 6 | 5 | 1794–1799, 1837, 2786, 7065, 7161 |
| `portraitCard` | 6 | 5 | 1132, 1216, 1979–1984, 2259, 2896 |
| `appfooter` | 5 | 5 | 330, 2839, 6653, 7095, 7567 |
| `skinHeader-withBackground` | 5 | 5 | 1696, 4083, 6028, 6464, 6514 |
| `btnPlay` | 16 | 4 | 562–586, 625–680, 3839–3881, 3913–3941 |
| `itemName` | 11 | 4 | 737, 2366, 5599–5646, 5737–5754 |
| `backdropImage` | 10 | 4 | 2685–2713, 2740–2744, 6949, 7072–7080 |
| `upNextContainer` | 10 | 4 | 5254–5272, 5298–5324, 7009–7019, 7045 |
| `emby-scroller` | 9 | 4 | 1799, 1837–1843, 7314–7361, 7546–7562 |
| `sectionTitleTextButton` | 9 | 4 | 479, 5146–5154, 5181–5193, 5227–5237 |
| `backgroundContainer` | 8 | 4 | 2149, 2677, 2718–2736, 2768 |
| `detailRibbon` | 8 | 4 | 1653–1681, 1894, 1979–1991, 7811 |
| `skip-button` | 8 | 4 | 680, 3891, 5347–5372, 5399–5417 |
| `listItemBodyText` | 7 | 4 | 4598–4617, 4657, 4732, 7621 |
| `visualCardBox` | 7 | 4 | 457, 881–894, 920–925, 1051 |
| `button-submit` | 6 | 4 | 3907, 3994, 6161–6169, 7689–7704 |
| `cardText-secondary` | 6 | 4 | 314, 969, 3629–3633, 7134–7142 |
| `detailPagePrimaryContent` | 6 | 4 | 1668–1686, 2501, 5080, 7225 |
| `skinHeader-blurred` | 6 | 4 | 6028, 6493–6500, 7209, 7567–7586 |
| `squareCard` | 6 | 4 | 904, 2549, 2585–2603, 6130–6134 |
| `itemsContainer` | 4 | 4 | 791, 1826, 1861, 5086 |
| `raised` | 4 | 4 | 680, 766, 3776, 3810 |
| `tsx` | 4 | 4 | 1132, 1714, 4469, 4546 |
| `x` | 4 | 4 | 2366, 4158, 5702, 7161 |
| `detailButton` | 13 | 3 | 625–680, 3820–3881, 3937–3941 |
| `itemSelectionPanel` | 9 | 3 | 933–937, 3569, 3597–3640 |
| `pageTitle` | 8 | 3 | 1738–1781, 6525, 6628 |
| `homePage` | 7 | 3 | 4469, 4515–4542, 6757 |
| `playedIndicator` | 7 | 3 | 819–833, 3713, 7242–7266 |
| `check` | 6 | 3 | 3597, 3829, 4711–4755 |
| `detailSectionContent` | 6 | 3 | 3401, 4866–4876, 4959–4969 |
| `emby-checkbox` | 6 | 3 | 3574, 3611–3615, 3664–3676 |
| `actionSheetContent` | 5 | 3 | 4703–4707, 7009–7019, 7045 |
| `cardText-first` | 5 | 3 | 969, 3603–3629, 6241 |
| `dialog` | 5 | 3 | 3453–3463, 7009–7019, 7045 |
| `guideProgramName` | 5 | 3 | 680, 5778–5789, 5832–5837 |
| `noHomeButtonHeader` | 5 | 3 | 1714, 6525, 6679–6690 |
| `overflowBackdropCard` | 5 | 3 | 1009–1015, 3607, 6236–6241 |
| `secondary` | 5 | 3 | 314, 4607–4617, 4657 |
| `album` | 4 | 3 | 2295, 2554–2558, 2594 |
| `cardPadder` | 4 | 3 | 453, 1051, 3620–3624 |
| `cardText` | 4 | 3 | 969–979, 3629, 7387 |
| `detailPageContent` | 4 | 3 | 1816, 4793, 5073–5080 |
| `dialog-fullscreen` | 4 | 3 | 3463, 7009–7019, 7045 |
| `emby-scrollbuttons` | 4 | 3 | 1879–1884, 7408, 7933 |
| `folder` | 4 | 3 | 1979–1984, 3730, 3793 |
| `formDialogFooter` | 4 | 3 | 3521, 4001, 7638–7662 |
| `infoWrapper` | 4 | 3 | 2238–2243, 2501, 2529 |
| `listItemImage` | 4 | 3 | 2873–2878, 4571, 7621 |
| `musicParentName` | 4 | 3 | 2055, 2607, 5719–5728 |
| `programGuideSection` | 4 | 3 | 2562–2577, 4969, 4996 |
| `toast` | 4 | 3 | 5247, 7009–7019, 7045 |
| `cardFooter` | 3 | 3 | 3640, 7112, 7151 |
| `collectionItems` | 3 | 3 | 1826, 4969, 5005 |
| `defaultCardBackground` | 3 | 3 | 3751, 6256, 6355 |
| `detailPageSecondaryContainer` | 3 | 3 | 1663, 1690, 1816 |
| `emby-input` | 3 | 3 | 5513, 5542, 7704 |
| `formDialogFooterItem` | 3 | 3 | 3521, 3788, 3913 |
| `formDialogHeader` | 3 | 3 | 4001, 7567, 7638 |
| `iconOsd` | 3 | 3 | 6006, 7567, 7638 |
| `live_tv` | 3 | 3 | 2055, 2594, 4035 |
| `myPreferencesMenuPage` | 3 | 3 | 426, 4771, 5094 |
| `playerStats` | 3 | 3 | 6006, 7638, 7674 |
| `readOnlyContent` | 3 | 3 | 4043, 6119, 6773 |
| `sectionTitle-cards` | 3 | 3 | 1794, 5163, 5223 |
| `sectionTitleContainer` | 3 | 3 | 1826, 1884, 5005 |
| `itemExternalLinks` | 13 | 2 | 3171–3249, 3401 |
| `checkboxOutline` | 10 | 2 | 3574–3615, 3646–3676 |
| `itemBackdrop` | 9 | 2 | 2021–2080, 2268 |
| `mdl-slider` | 9 | 2 | 2969, 3024–3082 |
| `cardOverlayButton-br` | 8 | 2 | 1063, 1092–1143 |
| `listItemIcon` | 8 | 2 | 4031–4035, 4711–4771 |
| `sliderContainer` | 8 | 2 | 2973, 3001–3066 |
| `detail-clamp-text` | 7 | 2 | 3337–3363, 3389–3393 |
| `divUsers` | 7 | 2 | 6130–6134, 7371–7398 |
| `multiSelectCheckboxOutline` | 7 | 2 | 3611–3615, 3645–3664 |
| `countIndicator` | 6 | 2 | 810–840, 7638–7662 |
| `detailPagePrimaryContainer` | 6 | 2 | 1640–1686, 2501 |
| `detailsGroupItem` | 6 | 2 | 4828, 4899–4936 |
| `headerButton` | 6 | 2 | 600–680, 6621 |
| `headerLeft` | 6 | 2 | 1744–1781, 6878 |
| `selectionCommandsPanel` | 6 | 2 | 3531–3565, 7567 |
| `trackSelections` | 6 | 2 | 4797–4828, 4964–4969 |
| `withBackdrop` | 6 | 2 | 2677, 2718–2736 |
| `detailSection` | 5 | 2 | 4780–4789, 4949–4969 |
| `fullSyncIndicator` | 5 | 2 | 810–833, 7638–7662 |
| `mainDrawer-scrollContainer` | 5 | 2 | 3131, 7284–7301 |
| `manualLoginForm` | 5 | 2 | 6101–6145, 6186 |
| `mediaInfoItem` | 5 | 2 | 1898–1941, 7161 |
| `overview-expand` | 5 | 2 | 3369–3393, 4866 |
| `scrollX` | 5 | 2 | 1799, 1837–1857 |
| `videoIndicator` | 5 | 2 | 3719–3747, 7638 |
| `visualLoginForm` | 5 | 2 | 6101–6145, 6186 |
| `withSectionTabs` | 5 | 2 | 2727–2744, 6500 |
| `alphaPickerButton` | 4 | 2 | 680, 5020–5032 |
| `backgroundProgress` | 4 | 2 | 2884–2896, 2926 |
| `emby-select` | 4 | 2 | 5513–5525, 7704 |
| `emby-tab-button-active` | 4 | 2 | 3974, 6726–6740 |
| `mediaSourceIndicator` | 4 | 2 | 810–833, 7638 |
| `play_arrow` | 4 | 2 | 3756–3772, 3941 |
| `playbackProgress` | 4 | 2 | 2884–2896, 2931 |
| `playlistIndexIndicatorImage` | 4 | 2 | 4598–4603, 6349–6355 |
| `programCell` | 4 | 2 | 5769, 5828–5837 |
| `cardOverlayButtonIcon` | 3 | 2 | 1063–1075, 1143 |
| `castCollapsible` | 3 | 2 | 872, 3615–3624 |
| `emby-scrollbuttons-button` | 3 | 2 | 1888, 7940–7947 |
| `emby-textarea` | 3 | 2 | 5504–5513, 5542 |
| `guestCastContent` | 3 | 2 | 872, 3615–3624 |
| `guide-channelHeaderCell` | 3 | 2 | 680, 5803–5819 |
| `guide-date-tab-button` | 3 | 2 | 680, 3974–3982 |
| `headerUserButton` | 3 | 2 | 600–613, 5098 |
| `noHeaderRight` | 3 | 2 | 1714, 6028–6032 |
| `overview` | 3 | 2 | 3389–3393, 4876 |
| `add` | 2 | 2 | 1799, 7161 |
| `alphaPicker-fixed-right` | 2 | 2 | 2768, 5032 |
| `backdropImageFadeIn` | 2 | 2 | 2823, 7678 |
| `book` | 2 | 2 | 2055, 2594 |
| `btnDeleteImage` | 2 | 2 | 3776, 3988 |
| `cardContent` | 2 | 2 | 872, 904 |
| `cardOverlayButton` | 2 | 2 | 1077, 1120 |
| `cardOverlayButton-hover` | 2 | 2 | 964, 1092 |
| `chevron_right` | 2 | 2 | 5193, 5237 |
| `classList` | 2 | 2 | 1799, 7161 |
| `collapseContent` | 2 | 2 | 3526, 3999 |
| `collectionItemsContainer` | 2 | 2 | 1826, 5009 |
| `content-primary` | 2 | 2 | 5073, 5129 |
| `editorsChoiceContainer` | 2 | 2 | 6834, 7858 |
| `editorsChoiceItemBanner` | 2 | 2 | 6834, 7586 |
| `editorsChoiceItemOverview` | 2 | 2 | 7858, 7951 |
| `endsAt` | 2 | 2 | 1919, 7161 |
| `f5f5f5` | 2 | 2 | 5347, 5377 |
| `fieldDescription` | 2 | 2 | 314, 7704 |
| `formDialogFooter-clear` | 2 | 2 | 3521, 4001 |
| `guide-programNameCaret` | 2 | 2 | 314, 5785 |
| `headroom` | 2 | 2 | 6488, 6525 |
| `indicator` | 2 | 2 | 840, 3708 |
| `mc-row` | 2 | 2 | 468, 7478 |
| `mediaInfoOfficialRating` | 2 | 2 | 1919, 7161 |
| `navMenuOption-selected` | 2 | 2 | 4776, 7295 |
| `nowPlayingInfoContainer` | 2 | 2 | 3162, 6286 |
| `org` | 2 | 2 | 3198, 3228 |
| `page` | 2 | 2 | 2768, 7065 |
| `paperList` | 2 | 2 | 881, 4012 |
| `playlist` | 2 | 2 | 4593, 6264 |
| `programSecondaryTitle` | 2 | 2 | 314, 5837 |
| `queue` | 2 | 2 | 2055, 2594 |
| `reactRoot` | 2 | 2 | 4469, 6884 |
| `recordingFields` | 2 | 2 | 4820, 4964 |
| `runtime` | 2 | 2 | 6198, 6226 |
| `sectionTitleContainer-cards` | 2 | 2 | 5158, 5223 |
| `sidebarHeader` | 2 | 2 | 4139, 7301 |
| `splide` | 2 | 2 | 6834, 7907 |
| `tagline` | 2 | 2 | 2668, 4876 |
| `upNextDialog-title` | 2 | 2 | 5277, 5311 |
| `vertical-list` | 2 | 2 | 1861, 7806 |
| `vertical-wrap` | 2 | 2 | 806, 1826 |
| `videoOsdBottom` | 2 | 2 | 3154, 6455 |
| `videoOsdBottom-maincontrols` | 2 | 2 | 3154, 6455 |
| `userPreferencesPage` | 12 | 1 | 7689–7785 |
| `checkboxContainer` | 7 | 1 | 3603–3640 |
| `itemDetailsGroup` | 7 | 1 | 4883–4969 |
| `itemProgressBar` | 6 | 1 | 2873–2907 |
| `streaming-lookup-container` | 6 | 1 | 3256–3301 |
| `trackSelectionFieldContainer` | 6 | 1 | 4839–4862 |
| `editorsChoiceScrollButtonsContainer` | 5 | 1 | 7907–7947 |
| `innerCardFooter` | 5 | 1 | 3416–3445 |
| `chapterCardImageContainer` | 4 | 1 | 3416–3445 |
| `emby-select-withcolor` | 4 | 1 | 5513–5560 |
| `endTimeText` | 4 | 1 | 6198–6226 |
| `mainDetailButtons` | 4 | 1 | 3937–3951 |
| `overview-controls` | 4 | 1 | 3389–3401 |
| `startTimeText` | 4 | 1 | 6198–6220 |
| `button-flat` | 3 | 1 | 3135–3145 |
| `cardIndicators` | 3 | 1 | 3693–3703 |
| `cardOverlayFab-primary` | 3 | 1 | 1055–1077 |
| `com` | 3 | 1 | 3204–3222 |
| `content` | 3 | 1 | 4905–4936 |
| `fab` | 3 | 1 | 3797–3810 |
| `listChildrenCollapsible` | 3 | 1 | 4954–4969 |
| `mdl-slider-background-flex` | 3 | 1 | 2993–3006 |
| `mediaInfoCriticRating` | 3 | 1 | 1960–1969 |
| `nextUpSection` | 3 | 1 | 4949–4969 |
| `nowPlayingPageImageContainerNoAlbum` | 3 | 1 | 6250–6260 |
| `serverInfo` | 3 | 1 | 4016–4025 |
| `transcodingProgress` | 3 | 1 | 2884–2896 |
