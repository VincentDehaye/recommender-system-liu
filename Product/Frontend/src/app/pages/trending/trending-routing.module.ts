import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { TrendingComponent } from './trending.component';
import { TrendingWorldComponent } from './trending-world/trending-world.component';
import { TrendingLibraryComponent } from './trending-library/trending-library.component';

const routes: Routes = [{
  path: '',
  component: TrendingComponent,
  children: [{
    path: 'trending-library',
    component: TrendingLibraryComponent,
  }, {
    path: 'trending-world',
    component: TrendingWorldComponent,
  }],
}];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class TrendingRoutingModule { }

export const routedComponents = [
  TrendingComponent,
  TrendingLibraryComponent,
  TrendingWorldComponent,
];
