import { RouterModule, Routes } from '@angular/router';
import { NgModule } from '@angular/core';

import { PagesComponent } from './pages.component';
import { OverviewComponent } from './overview/overview.component';
import { UsersComponent } from './users/users.component';
import { UserComponent } from './user/user.component';
import { TrendingComponent} from './trending/trending.component';
import { RecommendedComponent } from './recommended/recommended.component';

const routes: Routes = [{
  path: '',
  component: PagesComponent,
  children: [{
    path: 'overview',
    component: OverviewComponent,
  }, {
    path: 'users',
    component: UsersComponent,
  }, {
    path: 'user',
    component: UserComponent,
  }, {
    path: 'recommended',
    component: RecommendedComponent,
  }, {
    path: 'trending',
    component: TrendingComponent,
  }, {
    path: 'content',
    loadChildren: './content/content.module#ContentModule',
  }, {
    path: '',
    redirectTo: 'overview',
    pathMatch: 'full',
  }],
}];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class PagesRoutingModule {
}
