# Index des composants — ElegantFin Cinema Edition v1.3.3

Généré par `python scripts/component-index.py`. **Ne pas éditer à la main.**

Les règles d'un même composant sont réparties en couches sur tout le fichier :
l'ordre porte la cascade, c'est voulu, il ne faut pas les regrouper. Mais avant
de modifier le style d'un composant, il faut avoir vu **toutes** ses règles —
sinon on en corrige une pendant qu'une autre, ailleurs, continue de gagner.
C'est exactement ce qui a produit la régression v1.2.88 sur le bouton skip,
dont les huit règles s'étalaient sur 3 700 lignes.

Source indexée : `ElegantFin-cinema-v1.3.3.css` — 6645 lignes.

| Composant | Règles | Zones | Lignes |
|---|---:|---:|---|
| `card` | 36 | 14 | 383–465, 703, 785, 1431–1451, 1954–1987, 2014–2018, 2293–2311, 2347, 5692, 5979–5995, 6075–6097, 6127–6134, 6208, 6523 |
| `cardScalable` | 28 | 13 | 383–394, 442–465, 731–775, 801–839, 2311, 3235, 3346, 3425, 4981, 5706–5716, 5785, 5979, 6118–6134 |
| `cardImageContainer` | 23 | 13 | 437, 753, 781–810, 839, 896–926, 5090–5094, 5175, 5698, 5777–5785, 5838, 5979–5995, 6118, 6256 |
| `material-icons` | 15 | 11 | 319–338, 1650, 1709, 1761, 3192, 3351, 3425–3431, 3537, 3794, 4284, 4318–4328 |
| `itemDetailPage` | 16 | 10 | 1494, 1580, 1659, 1880–1905, 1949, 2049, 2360–2365, 3888, 4165, 6351–6389 |
| `nameContainer` | 27 | 9 | 649, 2056–2079, 2120, 2149, 2184–2230, 2267, 2298–2302, 4657–4709, 6351–6389 |
| `backdropCard` | 12 | 9 | 883–889, 1004, 1880, 1966, 2049, 2302–2311, 2338, 2365, 2635 |
| `card-hoverable` | 23 | 8 | 465, 741, 801–889, 5094, 5716, 5866–5885, 5979, 6263 |
| `parentName` | 23 | 8 | 649, 2061–2079, 2120, 2149, 2184–2230, 4663–4709, 4782, 6351–6389 |
| `detailPageWrapperContainer` | 17 | 8 | 649, 1462–1472, 1905, 2023, 2056–2079, 2149, 2184–2230, 2298 |
| `subtitle` | 16 | 8 | 1880, 1949, 2061, 2120, 2239–2249, 2360–2365, 4717–4750, 6351–6389 |
| `cardBox` | 12 | 8 | 383–431, 457, 703, 823, 930, 5692, 5979, 6263 |
| `detailLogo` | 17 | 7 | 649, 1894–1905, 1940–1949, 2049–2079, 2149, 2184–2230, 2298 |
| `loginPage` | 15 | 7 | 3504, 4993–5008, 5047, 5075–5094, 5721, 5764, 6107–6134 |
| `skinHeader` | 11 | 7 | 4989, 5318, 5374–5382, 5408–5433, 5768, 5947, 6460 |
| `emby-button` | 10 | 7 | 575–592, 619–637, 2994–3001, 3371, 3406, 3559, 3812 |
| `js` | 7 | 7 | 286, 1566, 2120, 2693, 3325, 5894, 6144 |
| `verticalSection` | 11 | 6 | 1654, 2531–2536, 4165, 5777, 5894, 6144 |
| `paper-icon-button-light` | 9 | 6 | 537–592, 1580, 1650, 1709, 4190, 4576 |
| `nowPlayingBar` | 8 | 6 | 2879, 5227, 5731, 5825, 5928–5959, 6213 |
| `person` | 8 | 6 | 1880–1890, 2049, 2302, 2347–2356, 3632, 6346 |
| `detailImageContainer` | 20 | 5 | 1880–1890, 1954–2018, 2049, 2289–2311, 2338–2365 |
| `listItem` | 16 | 5 | 592, 2315, 3714–3740, 3771–3803, 6231–6248 |
| `osdHeader` | 15 | 5 | 1623–1641, 5313–5382, 5408–5433, 5768, 6213 |
| `actionSheetMenuItem` | 11 | 5 | 592, 3714–3725, 3771, 3849–3865, 5749 |
| `navMenuOption` | 11 | 5 | 592, 688–698, 3781–3803, 3869–3874, 6018–6029 |
| `cardImageIcon` | 8 | 5 | 375–379, 2302–2311, 2371, 3219, 5175 |
| `emby-scroller-container` | 7 | 5 | 1654–1667, 2521, 2557, 5777, 5894 |
| `portraitCard` | 5 | 5 | 1004, 1082, 1799, 2014, 2635 |
| `btnPlay` | 16 | 4 | 474–498, 537–592, 3435–3477, 3510–3537 |
| `cardOverlayContainer` | 12 | 4 | 857–889, 934–956, 1016, 6213–6231 |
| `itemName` | 11 | 4 | 649, 2120, 4663–4709, 4800–4817 |
| `backdropImage` | 10 | 4 | 2437–2464, 2491–2495, 5685, 5785–5793 |
| `emby-tab-button` | 10 | 4 | 592, 659–668, 3483, 5484–5520 |
| `upNextContainer` | 10 | 4 | 4346–4365, 4391–4417, 5721–5731, 5757 |
| `sectionTabs` | 9 | 4 | 1678, 3483, 5354–5359, 5499–5525 |
| `button-link` | 8 | 4 | 592, 619–637, 2829–2838, 2899–2909 |
| `detailRibbon` | 7 | 4 | 1519–1547, 1714, 1799–1804, 6346 |
| `listItemBodyText` | 7 | 4 | 3735–3754, 3794, 3853, 6248 |
| `visualCardBox` | 7 | 4 | 383, 762–775, 801–806, 930 |
| `detailPagePrimaryContent` | 6 | 4 | 1534–1552, 2254, 4159, 5963 |
| `skip-button` | 6 | 4 | 592, 3488, 4440–4457, 4484–4490 |
| `squareCard` | 6 | 4 | 785, 2302, 2338–2356, 5051–5055 |
| `button-submit` | 5 | 4 | 3504, 3591, 5075–5083, 6321 |
| `mainDrawer` | 5 | 4 | 2843, 5721–5731, 6005, 6044 |
| `sectionTitle` | 5 | 4 | 1654, 1688–1695, 4264, 5042 |
| `skinHeader-blurred` | 5 | 4 | 4989, 5342–5349, 5947, 6213 |
| `appfooter` | 4 | 4 | 2578, 5458, 5808, 6213 |
| `page` | 4 | 4 | 926, 2512, 2557, 5777 |
| `raised` | 4 | 4 | 592, 678, 3371, 3406 |
| `skinHeader-withBackground` | 4 | 4 | 1562, 4989, 5313, 5363 |
| `detailButton` | 13 | 3 | 537–592, 3416–3477, 3533–3537 |
| `emby-scroller` | 9 | 3 | 1659–1673, 6050–6097, 6199–6208 |
| `itemBackdrop` | 9 | 3 | 1846–1890, 2023, 2365 |
| `itemSelectionPanel` | 9 | 3 | 814–818, 3164, 3192–3235 |
| `check` | 8 | 3 | 3192, 3425, 3845–3865 |
| `pageTitle` | 8 | 3 | 1598–1641, 5374, 5433 |
| `detailSectionContent` | 6 | 3 | 3026, 3970–3980, 4061–4071 |
| `emby-checkbox` | 6 | 3 | 3169, 3206–3210, 3259–3271 |
| `headerTop` | 6 | 3 | 5324–5349, 5400–5417, 5444–5448 |
| `actionSheetContent` | 5 | 3 | 3837–3841, 5721–5731, 5757 |
| `cardText-first` | 5 | 3 | 844, 3198–3224, 5156 |
| `cardText-secondary` | 5 | 3 | 844, 3224–3228, 5872–5880 |
| `dialog` | 5 | 3 | 3076–3086, 5721–5731, 5757 |
| `guideProgramName` | 5 | 3 | 592, 4841–4852, 4895–4900 |
| `musicParentName` | 5 | 3 | 1880, 2360–2365, 4782–4791 |
| `noHomeButtonHeader` | 5 | 3 | 1580, 5374, 5484–5492 |
| `overflowBackdropCard` | 5 | 3 | 883–889, 3202, 5151–5156 |
| `album` | 4 | 3 | 2049, 2307–2311, 2347 |
| `cardPadder` | 4 | 3 | 379, 930, 3215–3219 |
| `cardText` | 4 | 3 | 844–854, 3224, 6123 |
| `countIndicator` | 4 | 3 | 722, 5819, 6270–6294 |
| `dialog-fullscreen` | 4 | 3 | 3086, 5721–5731, 5757 |
| `emby-scrollbuttons` | 4 | 3 | 1700–1705, 6144, 6498 |
| `formDialogFooter` | 4 | 3 | 3144, 3598, 6270–6294 |
| `infoWrapper` | 4 | 3 | 1993–1998, 2254, 2282 |
| `listItemImage` | 4 | 3 | 2612–2617, 3708, 6248 |
| `semiTransparent` | 4 | 3 | 1562, 4989, 5342–5363 |
| `toast` | 4 | 3 | 4338, 5721–5731, 5757 |
| `defaultCardBackground` | 3 | 3 | 3346, 5171, 5270 |
| `folder` | 3 | 3 | 1799, 3325, 3389 |
| `formDialogFooterItem` | 3 | 3 | 3144, 3384, 3510 |
| `formDialogHeader` | 3 | 3 | 3598, 6213, 6270 |
| `iconOsd` | 3 | 3 | 4967, 6213, 6270 |
| `itemsContainer` | 3 | 3 | 703, 1682, 4165 |
| `live_tv` | 3 | 3 | 1880, 2347, 3632 |
| `myPreferencesMenuPage` | 3 | 3 | 352, 3879, 4173 |
| `playerStats` | 3 | 3 | 4967, 6270, 6306 |
| `scss` | 3 | 3 | 956, 3241, 5894 |
| `sectionTitle-cards` | 3 | 3 | 1654, 4264, 4314 |
| `x` | 3 | 3 | 2120, 4765, 5894 |
| `itemExternalLinks` | 11 | 2 | 2892–2949, 3026 |
| `checkboxOutline` | 10 | 2 | 3169–3210, 3241–3271 |
| `mdl-slider` | 9 | 2 | 2689, 2744–2802 |
| `listItemIcon` | 8 | 2 | 3628–3632, 3849–3879 |
| `sectionTitleTextButton` | 8 | 2 | 4247–4284, 4318–4328 |
| `sliderContainer` | 8 | 2 | 2693, 2721–2786 |
| `cardOverlayButton-br` | 7 | 2 | 942, 971–1009 |
| `detail-clamp-text` | 7 | 2 | 2962–2988, 3014–3018 |
| `divUsers` | 7 | 2 | 5051–5055, 6107–6134 |
| `multiSelectCheckboxOutline` | 7 | 2 | 3206–3210, 3240–3259 |
| `backgroundContainer` | 6 | 2 | 2427, 2469–2487 |
| `detailPagePrimaryContainer` | 6 | 2 | 1506–1552, 2254 |
| `detailsGroupItem` | 6 | 2 | 3932, 4000–4038 |
| `headerButton` | 6 | 2 | 512–592, 5426 |
| `headerLeft` | 6 | 2 | 1604–1641, 5613 |
| `trackSelections` | 6 | 2 | 3905–3932, 4066–4071 |
| `withBackdrop` | 6 | 2 | 2427, 2469–2487 |
| `detailSection` | 5 | 2 | 3888–3897, 4051–4071 |
| `mainDrawer-scrollContainer` | 5 | 2 | 2852, 6018–6035 |
| `mediaInfoItem` | 5 | 2 | 1718–1761, 5894 |
| `overview-expand` | 5 | 2 | 2994–3018, 3970 |
| `playedIndicator` | 5 | 2 | 3308, 5979–6000 |
| `videoIndicator` | 5 | 2 | 3314–3342, 6270 |
| `withSectionTabs` | 5 | 2 | 2478–2495, 5349 |
| `emby-tab-button-active` | 4 | 2 | 3570, 5511–5525 |
| `headerUserButton` | 4 | 2 | 512–525, 4177–4190 |
| `play_arrow` | 4 | 2 | 3351–3367, 3537 |
| `playlistIndexIndicatorImage` | 4 | 2 | 3735–3740, 5264–5270 |
| `programCell` | 4 | 2 | 4832, 4891–4900 |
| `programGuideSection` | 4 | 2 | 2315–2330, 4071–4086 |
| `secondary` | 4 | 2 | 3744–3754, 3794 |
| `section0` | 4 | 2 | 896–926, 5777 |
| `visualLoginForm` | 4 | 2 | 5042–5059, 5100 |
| `alphaPickerButton` | 3 | 2 | 592, 4110–4117 |
| `cardFooter` | 3 | 2 | 3235, 5866–5885 |
| `cardOverlayButtonIcon` | 3 | 2 | 942–954, 1009 |
| `castCollapsible` | 3 | 2 | 753, 3210–3219 |
| `detailPageContent` | 3 | 2 | 3901, 4152–4159 |
| `emby-scrollbuttons-button` | 3 | 2 | 1709, 6505–6512 |
| `fullSyncIndicator` | 3 | 2 | 722, 6270–6294 |
| `guestCastContent` | 3 | 2 | 753, 3210–3219 |
| `guide-channelHeaderCell` | 3 | 2 | 592, 4866–4882 |
| `guide-date-tab-button` | 3 | 2 | 592, 3570–3578 |
| `manualLoginForm` | 3 | 2 | 5042–5059, 5100 |
| `overview` | 3 | 2 | 3014–3018, 3980 |
| `selectionCommandsPanel` | 3 | 2 | 3154–3160, 6213 |
| `backdropImageFadeIn` | 2 | 2 | 2562, 6310 |
| `blurhash-canvas` | 2 | 2 | 5838, 6256 |
| `book` | 2 | 2 | 1880, 2347 |
| `btnDeleteImage` | 2 | 2 | 3371, 3584 |
| `cardContent` | 2 | 2 | 753, 785 |
| `cardImage` | 2 | 2 | 5838, 6256 |
| `cardOverlayButton` | 2 | 2 | 956, 992 |
| `cardOverlayButton-hover` | 2 | 2 | 839, 971 |
| `chevron_right` | 2 | 2 | 4284, 4328 |
| `collapseContent` | 2 | 2 | 3149, 3596 |
| `content-primary` | 2 | 2 | 4152, 4230 |
| `detailPageSecondaryContainer` | 2 | 2 | 1529, 1556 |
| `editorsChoiceItemOverview` | 2 | 2 | 6435, 6516 |
| `endsAt` | 2 | 2 | 1739, 5894 |
| `formDialogFooter-clear` | 2 | 2 | 3144, 3598 |
| `headroom` | 2 | 2 | 5337, 5374 |
| `mediaInfoOfficialRating` | 2 | 2 | 1739, 5894 |
| `mediaSourceIndicator` | 2 | 2 | 722, 6270 |
| `navMenuOption-selected` | 2 | 2 | 3884, 6029 |
| `nowPlayingInfoContainer` | 2 | 2 | 2883, 5201 |
| `org` | 2 | 2 | 2919, 2949 |
| `paperList` | 2 | 2 | 762, 3609 |
| `playlist` | 2 | 2 | 3730, 5179 |
| `queue` | 2 | 2 | 1880, 2347 |
| `readOnlyContent` | 2 | 2 | 3640, 5542 |
| `recordingFields` | 2 | 2 | 3924, 4066 |
| `runtime` | 2 | 2 | 5112, 5141 |
| `sectionTitleContainer` | 2 | 2 | 1705, 4095 |
| `sectionTitleContainer-cards` | 2 | 2 | 4259, 4314 |
| `tagline` | 2 | 2 | 2418, 3980 |
| `upNextDialog-title` | 2 | 2 | 4370, 4404 |
| `vertical-list` | 2 | 2 | 1682, 6341 |
| `videoOsdBottom` | 2 | 2 | 2875, 5304 |
| `videoOsdBottom-maincontrols` | 2 | 2 | 2875, 5304 |
| `checkboxContainer` | 7 | 1 | 3198–3235 |
| `itemDetailsGroup` | 7 | 1 | 3984–4071 |
| `trackSelectionFieldContainer` | 6 | 1 | 3943–3966 |
| `editorsChoiceScrollButtonsContainer` | 5 | 1 | 6472–6512 |
| `innerCardFooter` | 5 | 1 | 3039–3068 |
| `itemProgressBar` | 5 | 1 | 2612–2635 |
| `backgroundProgress` | 4 | 1 | 2623–2646 |
| `chapterCardImageContainer` | 4 | 1 | 3039–3068 |
| `endTimeText` | 4 | 1 | 5112–5141 |
| `mainDetailButtons` | 4 | 1 | 3533–3547 |
| `overview-controls` | 4 | 1 | 3014–3026 |
| `playbackProgress` | 4 | 1 | 2623–2651 |
| `scrollX` | 4 | 1 | 1659–1678 |
| `startTimeText` | 4 | 1 | 5112–5135 |
| `button-flat` | 3 | 1 | 2856–2866 |
| `cardIndicators` | 3 | 1 | 3288–3298 |
| `cardOverlayFab-primary` | 3 | 1 | 934–956 |
| `com` | 3 | 1 | 2925–2943 |
| `content` | 3 | 1 | 4007–4038 |
| `discover-card` | 3 | 1 | 6523–6546 |
| `emby-select-withcolor` | 3 | 1 | 4590–4624 |
| `emby-textarea` | 3 | 1 | 4581–4606 |
| `fab` | 3 | 1 | 3393–3406 |
| `listChildrenCollapsible` | 3 | 1 | 4056–4071 |
| `mdl-slider-background-flex` | 3 | 1 | 2713–2726 |
| `mediaInfoCriticRating` | 3 | 1 | 1780–1789 |
| `nextUpSection` | 3 | 1 | 4051–4071 |
| `nowPlayingPageImageContainerNoAlbum` | 3 | 1 | 5165–5175 |
| `serverInfo` | 3 | 1 | 3613–3622 |
| `transcodingProgress` | 3 | 1 | 2623–2635 |
