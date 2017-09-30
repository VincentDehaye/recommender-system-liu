import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { UsersComponent } from './users.component';
import { AllUsersComponent } from './all-users/all-users.component';
import { SingleUserComponent } from './single-user/single-user.component';

const routes: Routes = [{
  path: '',
  component: UsersComponent,
  children: [{
    path: 'single-user',
    component: SingleUserComponent,
  }, {
    path: 'all-users',
    component: AllUsersComponent,
  }],
}];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class UsersRoutingModule { }

export const routedComponents = [
  UsersComponent,
  SingleUserComponent,
  AllUsersComponent,
];
