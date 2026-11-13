# Index des composants — ElegantFin Cinema Edition v1.5.9

Généré par `python scripts/component-index.py`. **Ne pas éditer à la main.**

Les règles d'un même composant sont réparties en couches sur tout le fichier :
l'ordre porte la cascade, c'est voulu, il ne faut pas les regrouper. Mais avant
de modifier le style d'un composant, il faut avoir vu **toutes** ses règles —
sinon on en corrige une pendant qu'une autre, ailleurs, continue de gagner.
C'est exactement ce qui a produit la régression v1.2.88 sur le bouton skip,
dont les huit règles s'étalaient sur 3 700 lignes.

Source indexée : `ElegantFin-cinema-v1.5.9.css` — 8063 lignes.

| Composant | Règles | Zones | Lignes |
|---|---:|---:|---|
| `card` | 38 | 16 | 457–487, 518–553, 791, 904, 1565–1585, 2194–2227, 2254–2258, 2535–2553, 2589, 6970, 7006–7016, 7156, 7256–7275, 7353–7375, 7405–7412, 7576 |
| `cardScalable` | 29 | 14 | 457, 487, 541–553, 854–894, 920–964, 2553, 3634, 3746, 3824, 6034, 6984–7016, 7086, 7256, 7396–7412 |
| `cardImageContainer` | 21 | 13 | 468, 536, 872, 900–929, 964, 1022–1046, 6190–6194, 6274, 6976, 7086, 7126, 7256–7275, 7396 |
| `material-icons` | 17 | 13 | 393–412, 1785, 1883, 1936, 3591, 3751, 3824–3830, 3945, 4107, 4661, 5190, 5224–5234, 5851 |
| `itemDetailPage` | 20 | 12 | 1628, 1709, 1794, 1821, 2050–2090, 2125–2140, 2176–2180, 2290, 2602, 4788, 5083, 7830–7868 |
| `skinHeader` | 20 | 12 | 296, 1709, 4087–4103, 4473, 4519–4546, 6042–6046, 6483, 6539–6547, 6617–6642, 7070, 7223, 7901 |
| `js` | 13 | 12 | 330, 360, 1695–1709, 1794, 2361, 2968, 3395, 3725, 5851, 6848, 7175, 7422 |
| `emby-button` | 13 | 10 | 663–680, 707–725, 3229, 3363–3370, 3771, 3805, 3967, 4679, 5368, 5421 |
| `nameContainer` | 27 | 9 | 737, 2297–2320, 2361, 2390, 2425–2472, 2509, 2540–2544, 5607–5660, 7830–7868 |
| `parentName` | 23 | 8 | 737, 2302–2320, 2361, 2390, 2425–2472, 5613–5660, 5733, 7830–7868 |
| `detailLogo` | 20 | 8 | 737, 2079–2090, 2125–2140, 2167–2180, 2290–2320, 2390, 2425–2472, 2540 |
| `detailPageWrapperContainer` | 17 | 8 | 737, 1596–1606, 2090, 2263, 2297–2320, 2390, 2425–2472, 2540 |
| `subtitle` | 17 | 8 | 2050–2060, 2176–2180, 2302, 2361, 2481–2491, 2602, 5668–5701, 7830–7868 |
| `cardBox` | 13 | 8 | 457–487, 518–542, 791, 942–946, 1051, 6970, 7256, 7641 |
| `backdropCard` | 12 | 8 | 1009–1015, 1132, 2050–2060, 2206, 2290, 2544–2553, 2580, 2891 |
| `nowPlayingBar` | 8 | 8 | 330, 3153, 6326, 7033, 7120, 7209, 7235, 7581 |
| `card-hoverable` | 22 | 7 | 553, 920–1015, 6194, 6994, 7126–7165, 7256, 7641 |
| `listItem` | 18 | 7 | 314, 680, 2557, 4581–4607, 4638–4670, 4715, 7618–7635 |
| `loginPage` | 18 | 7 | 3911, 6046–6080, 6120–6139, 6175–6194, 7023, 7066, 7385–7412 |
| `paper-icon-button-light` | 12 | 7 | 625–680, 1709, 1785, 1883, 3531–3551, 5368, 5505 |
| `navMenuOption` | 12 | 6 | 680, 776–786, 4156, 4648–4670, 4769–4774, 7298–7309 |
| `emby-tab-button` | 11 | 6 | 680, 747–756, 3886, 6693–6704, 6732–6749, 7913 |
| `verticalSection` | 11 | 6 | 1789, 2793–2798, 5083, 7079, 7175, 7422 |
| `button-link` | 10 | 6 | 680, 707–725, 3104–3113, 3173–3183, 3229, 7792 |
| `headerTop` | 9 | 6 | 2180, 4473, 4519, 6489–6514, 6609–6626, 6653–6657 |
| `person` | 8 | 6 | 2050–2075, 2290, 2544, 2589–2598, 4039, 7825 |
| `mainDrawer` | 7 | 6 | 3118, 4121, 4519, 7023–7033, 7285, 7324 |
| `scss` | 6 | 6 | 296, 819, 1077, 3640, 4162, 7175 |
| `detailImageContainer` | 20 | 5 | 2050–2075, 2194–2258, 2290, 2531–2553, 2580–2598 |
| `btnPlay` | 19 | 5 | 562–586, 625–680, 3834–3885, 3917–3945, 5368 |
| `osdHeader` | 15 | 5 | 1758–1776, 6478–6547, 6617–6642, 7070, 7581 |
| `cardOverlayContainer` | 12 | 5 | 983–1015, 1055–1077, 1150, 7581, 7618 |
| `sectionTabs` | 11 | 5 | 1852, 3886, 4546, 6519–6524, 6710–6754 |
| `cardImageIcon` | 8 | 5 | 449–453, 2544–2553, 2616, 3618, 6274 |
| `sectionTitle` | 7 | 5 | 1789, 1862–1869, 4374, 5160–5168, 6115 |
| `semiTransparent` | 7 | 5 | 1691, 4087–4103, 6042, 6507–6528, 6564 |
| `emby-scroller-container` | 6 | 5 | 1789–1794, 1832, 2781, 7079, 7175 |
| `portraitCard` | 6 | 5 | 1132, 1216, 1974–1979, 2254, 2891 |
| `appfooter` | 5 | 5 | 330, 2834, 6667, 7109, 7581 |
| `skinHeader-withBackground` | 5 | 5 | 1691, 4087, 6042, 6478, 6528 |
| `detailButton` | 15 | 4 | 625–680, 3815–3885, 3941–3945, 5368 |
| `itemName` | 11 | 4 | 737, 2361, 5613–5660, 5751–5768 |
| `backdropImage` | 10 | 4 | 2680–2708, 2735–2739, 6963, 7086–7094 |
| `upNextContainer` | 10 | 4 | 5251–5269, 5295–5321, 7023–7033, 7059 |
| `emby-scroller` | 9 | 4 | 1794, 1832–1838, 7328–7375, 7560–7576 |
| `sectionTitleTextButton` | 9 | 4 | 479, 5143–5151, 5178–5190, 5224–5234 |
| `skip-button` | 9 | 4 | 680, 3895, 5344–5378, 5405–5423 |
| `backgroundContainer` | 8 | 4 | 2144, 2672, 2713–2731, 2763 |
| `detailRibbon` | 8 | 4 | 1653–1677, 1889, 1974–1986, 7825 |
| `visualCardBox` | 7 | 4 | 457, 881–894, 920–925, 1051 |
| `actionSheetMenuItem` | 6 | 4 | 680, 4581–4592, 4638, 7051 |
| `button-submit` | 6 | 4 | 3911, 3998, 6175–6183, 7703–7718 |
| `cardText-secondary` | 6 | 4 | 314, 969, 3623–3627, 7148–7156 |
| `skinHeader-blurred` | 6 | 4 | 6042, 6507–6514, 7223, 7581–7600 |
| `squareCard` | 6 | 4 | 904, 2544, 2580–2598, 6144–6148 |
| `itemsContainer` | 4 | 4 | 791, 1821, 1856, 5083 |
| `raised` | 4 | 4 | 680, 766, 3771, 3805 |
| `tsx` | 4 | 4 | 1132, 1709, 4473, 4550 |
| `x` | 4 | 4 | 2361, 4162, 5716, 7175 |
| `itemSelectionPanel` | 9 | 3 | 933–937, 3563, 3591–3634 |
| `pageTitle` | 8 | 3 | 1733–1776, 6539, 6642 |
| `headerButton` | 7 | 3 | 600–680, 5368, 6635 |
| `homePage` | 7 | 3 | 4473, 4519–4546, 6771 |
| `playedIndicator` | 7 | 3 | 819–833, 3707, 7256–7280 |
| `detailSectionContent` | 6 | 3 | 3395, 4870–4880, 4963–4973 |
| `emby-checkbox` | 6 | 3 | 3568, 3605–3609, 3658–3670 |
| `listItemBodyText` | 6 | 3 | 4602–4621, 4661, 7635 |
| `actionSheetContent` | 5 | 3 | 4707–4711, 7023–7033, 7059 |
| `cardText-first` | 5 | 3 | 969, 3597–3623, 6255 |
| `detailPagePrimaryContent` | 5 | 3 | 1666–1682, 2496, 7239 |
| `dialog` | 5 | 3 | 3447–3457, 7023–7033, 7059 |
| `guideProgramName` | 5 | 3 | 680, 5792–5803, 5846–5851 |
| `noHomeButtonHeader` | 5 | 3 | 1709, 6539, 6693–6704 |
| `overflowBackdropCard` | 5 | 3 | 1009–1015, 3601, 6250–6255 |
| `secondary` | 5 | 3 | 314, 4611–4621, 4661 |
| `album` | 4 | 3 | 2290, 2549–2553, 2589 |
| `cardPadder` | 4 | 3 | 453, 1051, 3614–3618 |
| `cardText` | 4 | 3 | 969–979, 3623, 7401 |
| `dialog-fullscreen` | 4 | 3 | 3457, 7023–7033, 7059 |
| `emby-input` | 4 | 3 | 5519, 5548–5566, 7718 |
| `emby-scrollbuttons` | 4 | 3 | 1874–1879, 7422, 7947 |
| `folder` | 4 | 3 | 1974–1979, 3725, 3788 |
| `formDialogFooter` | 4 | 3 | 3515, 4005, 7652–7676 |
| `infoWrapper` | 4 | 3 | 2233–2238, 2496, 2524 |
| `listItemIcon` | 4 | 3 | 4035–4039, 4715, 4779 |
| `listItemImage` | 4 | 3 | 2868–2873, 4575, 7635 |
| `musicParentName` | 4 | 3 | 2050, 2602, 5733–5742 |
| `programGuideSection` | 4 | 3 | 2557–2572, 4973, 5000 |
| `toast` | 4 | 3 | 5244, 7023–7033, 7059 |
| `cardFooter` | 3 | 3 | 3634, 7126, 7165 |
| `check` | 3 | 3 | 3591, 3824, 4715 |
| `collectionItems` | 3 | 3 | 1821, 4973, 5009 |
| `defaultCardBackground` | 3 | 3 | 3746, 6270, 6369 |
| `formDialogFooterItem` | 3 | 3 | 3515, 3783, 3917 |
| `formDialogHeader` | 3 | 3 | 4005, 7581, 7652 |
| `iconOsd` | 3 | 3 | 6020, 7581, 7652 |
| `live_tv` | 3 | 3 | 2050, 2589, 4039 |
| `myPreferencesMenuPage` | 3 | 3 | 426, 4779, 5091 |
| `playerStats` | 3 | 3 | 6020, 7652, 7688 |
| `readOnlyContent` | 3 | 3 | 4047, 6133, 6787 |
| `sectionTitle-cards` | 3 | 3 | 1789, 5160, 5220 |
| `sectionTitleContainer` | 3 | 3 | 1821, 1879, 5009 |
| `itemExternalLinks` | 13 | 2 | 3166–3244, 3395 |
| `checkboxOutline` | 10 | 2 | 3568–3609, 3640–3670 |
| `itemBackdrop` | 9 | 2 | 2016–2075, 2263 |
| `mdl-slider` | 9 | 2 | 2964, 3019–3077 |
| `cardOverlayButton-br` | 8 | 2 | 1063, 1092–1143 |
| `sliderContainer` | 8 | 2 | 2968, 2996–3061 |
| `detail-clamp-text` | 7 | 2 | 3331–3357, 3383–3387 |
| `divUsers` | 7 | 2 | 6144–6148, 7385–7412 |
| `multiSelectCheckboxOutline` | 7 | 2 | 3605–3609, 3639–3658 |
| `countIndicator` | 6 | 2 | 810–840, 7652–7676 |
| `detailPagePrimaryContainer` | 6 | 2 | 1640–1682, 2496 |
| `detailsGroupItem` | 6 | 2 | 4832, 4903–4940 |
| `headerLeft` | 6 | 2 | 1739–1776, 6892 |
| `selectionCommandsPanel` | 6 | 2 | 3525–3559, 7581 |
| `trackSelections` | 6 | 2 | 4801–4832, 4968–4973 |
| `withBackdrop` | 6 | 2 | 2672, 2713–2731 |
| `detailSection` | 5 | 2 | 4788–4797, 4953–4973 |
| `fullSyncIndicator` | 5 | 2 | 810–833, 7652–7676 |
| `mainDrawer-scrollContainer` | 5 | 2 | 3126, 7298–7315 |
| `manualLoginForm` | 5 | 2 | 6115–6159, 6200 |
| `mediaInfoItem` | 5 | 2 | 1893–1936, 7175 |
| `overview-expand` | 5 | 2 | 3363–3387, 4870 |
| `scrollX` | 5 | 2 | 1794, 1832–1852 |
| `videoIndicator` | 5 | 2 | 3714–3742, 7652 |
| `visualLoginForm` | 5 | 2 | 6115–6159, 6200 |
| `withSectionTabs` | 5 | 2 | 2722–2739, 6514 |
| `alphaPickerButton` | 4 | 2 | 680, 5024–5036 |
| `backgroundProgress` | 4 | 2 | 2879–2891, 2921 |
| `emby-select` | 4 | 2 | 5519–5531, 7718 |
| `emby-tab-button-active` | 4 | 2 | 3978, 6740–6754 |
| `emby-textarea` | 4 | 2 | 5510–5519, 5548–5566 |
| `mediaSourceIndicator` | 4 | 2 | 810–833, 7652 |
| `play_arrow` | 4 | 2 | 3751–3767, 3945 |
| `playbackProgress` | 4 | 2 | 2879–2891, 2926 |
| `playlistIndexIndicatorImage` | 4 | 2 | 4602–4607, 6363–6369 |
| `programCell` | 4 | 2 | 5783, 5842–5851 |
| `cardOverlayButtonIcon` | 3 | 2 | 1063–1075, 1143 |
| `castCollapsible` | 3 | 2 | 872, 3609–3618 |
| `detailPageSecondaryContainer` | 3 | 2 | 1661–1686, 1811 |
| `emby-scrollbuttons-button` | 3 | 2 | 1883, 7954–7961 |
| `guestCastContent` | 3 | 2 | 872, 3609–3618 |
| `guide-channelHeaderCell` | 3 | 2 | 680, 5817–5833 |
| `guide-date-tab-button` | 3 | 2 | 680, 3978–3986 |
| `headerUserButton` | 3 | 2 | 600–613, 5095 |
| `noHeaderRight` | 3 | 2 | 1709, 6042–6046 |
| `overview` | 3 | 2 | 3383–3387, 4880 |
| `add` | 2 | 2 | 1794, 7175 |
| `alphaPicker-fixed-right` | 2 | 2 | 2763, 5036 |
| `backdropImageFadeIn` | 2 | 2 | 2818, 7692 |
| `book` | 2 | 2 | 2050, 2589 |
| `btnDeleteImage` | 2 | 2 | 3771, 3992 |
| `cardContent` | 2 | 2 | 872, 904 |
| `cardOverlayButton` | 2 | 2 | 1077, 1120 |
| `cardOverlayButton-hover` | 2 | 2 | 964, 1092 |
| `chevron_right` | 2 | 2 | 5190, 5234 |
| `classList` | 2 | 2 | 1794, 7175 |
| `collapseContent` | 2 | 2 | 3520, 4003 |
| `collectionItemsContainer` | 2 | 2 | 1821, 5013 |
| `content-primary` | 2 | 2 | 5077, 5126 |
| `editorsChoiceContainer` | 2 | 2 | 6848, 7872 |
| `editorsChoiceItemBanner` | 2 | 2 | 6848, 7600 |
| `editorsChoiceItemOverview` | 2 | 2 | 7872, 7965 |
| `endsAt` | 2 | 2 | 1914, 7175 |
| `f5f5f5` | 2 | 2 | 5344, 5383 |
| `fieldDescription` | 2 | 2 | 314, 7718 |
| `formDialogFooter-clear` | 2 | 2 | 3515, 4005 |
| `guide-programNameCaret` | 2 | 2 | 314, 5799 |
| `headroom` | 2 | 2 | 6502, 6539 |
| `indicator` | 2 | 2 | 840, 3702 |
| `mc-row` | 2 | 2 | 468, 7492 |
| `mediaInfoOfficialRating` | 2 | 2 | 1914, 7175 |
| `navMenuOption-selected` | 2 | 2 | 4784, 7309 |
| `nowPlayingInfoContainer` | 2 | 2 | 3157, 6300 |
| `org` | 2 | 2 | 3193, 3223 |
| `page` | 2 | 2 | 2763, 7079 |
| `paperList` | 2 | 2 | 881, 4016 |
| `playlist` | 2 | 2 | 4597, 6278 |
| `programSecondaryTitle` | 2 | 2 | 314, 5851 |
| `queue` | 2 | 2 | 2050, 2589 |
| `reactRoot` | 2 | 2 | 4473, 6898 |
| `recordingFields` | 2 | 2 | 4824, 4968 |
| `runtime` | 2 | 2 | 6212, 6240 |
| `sectionTitleContainer-cards` | 2 | 2 | 5155, 5220 |
| `sidebarHeader` | 2 | 2 | 4143, 7315 |
| `splide` | 2 | 2 | 6848, 7921 |
| `tagline` | 2 | 2 | 2663, 4880 |
| `upNextDialog-title` | 2 | 2 | 5274, 5308 |
| `vertical-list` | 2 | 2 | 1856, 7820 |
| `vertical-wrap` | 2 | 2 | 806, 1821 |
| `videoOsdBottom` | 2 | 2 | 3149, 6469 |
| `videoOsdBottom-maincontrols` | 2 | 2 | 3149, 6469 |
| `userPreferencesPage` | 12 | 1 | 7703–7799 |
| `checkboxContainer` | 7 | 1 | 3597–3634 |
| `itemDetailsGroup` | 7 | 1 | 4887–4973 |
| `itemProgressBar` | 6 | 1 | 2868–2902 |
| `streaming-lookup-container` | 6 | 1 | 3251–3296 |
| `trackSelectionFieldContainer` | 6 | 1 | 4843–4866 |
| `editorsChoiceScrollButtonsContainer` | 5 | 1 | 7921–7961 |
| `emby-select-withcolor` | 5 | 1 | 5519–5574 |
| `innerCardFooter` | 5 | 1 | 3410–3439 |
| `chapterCardImageContainer` | 4 | 1 | 3410–3439 |
| `endTimeText` | 4 | 1 | 6212–6240 |
| `mainDetailButtons` | 4 | 1 | 3941–3955 |
| `overview-controls` | 4 | 1 | 3383–3395 |
| `startTimeText` | 4 | 1 | 6212–6234 |
| `button-flat` | 3 | 1 | 3130–3140 |
| `cardIndicators` | 3 | 1 | 3687–3697 |
| `cardOverlayFab-primary` | 3 | 1 | 1055–1077 |
| `com` | 3 | 1 | 3199–3217 |
| `content` | 3 | 1 | 4909–4940 |
| `fab` | 3 | 1 | 3792–3805 |
| `listChildrenCollapsible` | 3 | 1 | 4958–4973 |
| `mdl-slider-background-flex` | 3 | 1 | 2988–3001 |
| `mediaInfoCriticRating` | 3 | 1 | 1955–1964 |
| `nextUpSection` | 3 | 1 | 4953–4973 |
| `nowPlayingPageImageContainerNoAlbum` | 3 | 1 | 6264–6274 |
| `serverInfo` | 3 | 1 | 4020–4029 |
| `transcodingProgress` | 3 | 1 | 2879–2891 |
