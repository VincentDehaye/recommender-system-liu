import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';


// Component imports
// TODO:Page notFoundComponent
import { UserPageComponent } from './components/user-page/user-page.component';

const appRoutes: Routes = [
  {path: '', component: UserPageComponent},
  {path: 'user-page', component: UserPageComponent},
];

@NgModule({
  imports: [
    RouterModule.forRoot(
      appRoutes
    )
  ],
  exports: [
    RouterModule
  ]
})
export class AppRoutingModule { }
