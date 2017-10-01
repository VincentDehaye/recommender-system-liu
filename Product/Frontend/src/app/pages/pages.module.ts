import { NgModule } from '@angular/core';

import { PagesComponent } from './pages.component';
import { OverviewModule } from './overview/overview.module';
import { UsersModule } from './users/users.module';
import { UserModule } from './user/user.module';
import { TrendingModule } from './trending/trending.module';
import { RecommendedModule } from './recommended/recommended.module';
import { PagesRoutingModule } from './pages-routing.module';
import { ThemeModule } from '../@theme/theme.module';

const PAGES_COMPONENTS = [
  PagesComponent,
];

@NgModule({
  imports: [
    PagesRoutingModule,
    ThemeModule,
    OverviewModule,
    UsersModule,
    TrendingModule,
    RecommendedModule,
    UserModule,
  ],
  declarations: [
    ...PAGES_COMPONENTS,
  ],
})
export class PagesModule {
}
