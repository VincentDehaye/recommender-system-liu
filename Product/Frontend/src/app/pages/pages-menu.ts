import { NbMenuItem } from '@nebular/theme';

export const MENU_ITEMS: NbMenuItem[] = [
  /*{
    title: 'Overview',
    icon: 'ion-android-search',
    link: '/pages/overview',
    home: true,
  },*/
  {
    title: 'ACCOUNT',
    group: true,
  },
  {
    title: 'Logout',
    icon: 'ion-android-person',
    link: '/pages/login',
  },
  {
    title: 'ANALYTICS',
    group: true,
  },
   {
    title: 'Overview',
    icon: 'ion-android-globe',
    link: '/pages/overview',
  },
  {
    title: 'Recommendations',
    icon: 'ion-person-stalker',
    link: '/pages/users',
  },
  {
    title: 'Trending',
    icon: 'ion-arrow-graph-up-right',
    link: '/pages/trending',
  },
  {
    title: 'Recommendations',
    icon: 'ion-heart',
    link: '/pages/recommended',
  },
  /*{
    title: 'Content',
    icon: 'ion-android-list',
    link: '/pages/content/content-table',
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
    link: '/pages/user',
  },
];
