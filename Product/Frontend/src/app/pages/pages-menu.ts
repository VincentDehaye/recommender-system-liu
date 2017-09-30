import { NbMenuItem } from '@nebular/theme';

export const MENU_ITEMS: NbMenuItem[] = [
  {
    title: 'Overview',
    icon: 'ion-android-search',
    link: '/pages/dashboard',
    home: true,
  },
  {
    title: 'How To Use',
    icon: 'ion-information-circled',
    link: '/pages/ui-features/buttons',
  },
  {
    title: 'ANALYTICS',
    group: true,
  },
  {
    title: 'Users',
    icon: 'ion-person-stalker',
    children: [
      {
        title: 'Random User',
        link: '/pages/users/single-user',
      },
      {
        title: 'All Users',
        link: '/pages/users/all-users',
      },
    ],
  },
  {
    title: 'Trending',
    icon: 'ion-arrow-graph-up-right',
    children: [
      {
        title: 'Trending Library',
        link: '/pages/trending/trending-library',
      },
      {
        title: 'Trending World',
        link: '/pages/trending/trending-world',
      },
    ],
  },
  {
    title: 'Recommendations',
    icon: 'ion-heart',
    children: [
      {
        title: 'Echarts',
        link: '/pages/charts/echarts',
      },
      {
        title: 'Charts.js',
        link: '/pages/charts/chartjs',
      },
      {
        title: 'D3',
        link: '/pages/charts/d3',
      },
    ],
  },
  {
    title: 'Content',
    icon: 'ion-android-list',
    link: '/pages/tables/smart-table',
  },
 /* {
    title: 'Editors',
    icon: 'nb-title',
    children: [
      {
        title: 'TinyMCE',
        link: '/pages/editors/tinymce',
      },
      {
        title: 'CKEditor',
        link: '/pages/editors/ckeditor',
      },
    ],
  },*/
  /*{
    title: 'UI Features',
    icon: 'nb-keypad',
    link: '/pages/ui-features',
    children: [
      {
        title: 'Buttons',
        link: '/pages/ui-features/buttons',
      },
      {
        title: 'Grid',
        link: '/pages/ui-features/grid',
      },
      {
        title: 'Icons',
        link: '/pages/ui-features/icons',
      },
      {
        title: 'Modals',
        link: '/pages/ui-features/modals',
      },
      {
        title: 'Typography',
        link: '/pages/ui-features/typography',
      },
      {
        title: 'Animated Searches',
        link: '/pages/ui-features/search-fields',
      },
      {
        title: 'Tabs',
        link: '/pages/ui-features/tabs',
      },
    ],
  },*/
  /*{
    title: 'Forms',
    icon: 'nb-compose',
    children: [
      {
        title: 'Form Inputs',
        link: '/pages/forms/inputs',
      },
      {
        title: 'Form Layouts',
        link: '/pages/forms/layouts',
      },
    ],
  },*/
  /*{
    title: 'Components',
    icon: 'nb-gear',
    children: [
      {
        title: 'Tree',
        link: '/pages/components/tree',
      }, {
        title: 'Notifications',
        link: '/pages/components/notifications',
      },
    ],
  },*/
  /*{
    title: 'Maps',
    icon: 'nb-location',
    children: [
      {
        title: 'Google Maps',
        link: '/pages/maps/gmaps',
      },
      {
        title: 'Leaflet Maps',
        link: '/pages/maps/leaflet',
      },
      {
        title: 'Bubble Maps',
        link: '/pages/maps/bubble',
      },
    ],
  },*/
  /*{
    title: 'Auth',
    icon: 'nb-locked',
    children: [
      {
        title: 'Login',
        link: '/auth/login',
      },
      {
        title: 'Register',
        link: '/auth/register',
      },
      {
        title: 'Request Password',
        link: '/auth/request-password',
      },
      {
        title: 'Reset Password',
        link: '/auth/reset-password',
      },
    ],
  },*/
  {
    title: 'SIMULATION',
    group: true,
  },
  {
    title: 'User',
    icon: 'ion-android-person',
    link: '/pages/ui-features/typography',
    home: true,
  },
];
