import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { AppRoutingModule } from './app-routing.module';
import { ChartsModule } from 'ng2-charts';
import { AppComponent } from './app.component';
import { NavbarComponent } from './components/navbar/navbar.component';
import { UserPageComponent } from './components/user-page/user-page.component';
import { SidebarComponent } from './components/sidebar/sidebar.component';
import { ChartComponent } from './components/chart/chart.component';

@NgModule({
  declarations: [
    AppComponent,
    NavbarComponent,
    UserPageComponent,
    SidebarComponent,
    ChartComponent
  ],
  imports: [
    BrowserModule,
    // Created Modules
    AppRoutingModule,
    ChartsModule,
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
