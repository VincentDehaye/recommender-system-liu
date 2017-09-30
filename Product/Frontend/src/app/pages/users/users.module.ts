import { NgModule } from '@angular/core';
import { AngularEchartsModule } from 'ngx-echarts';
import { NgxChartsModule } from '@swimlane/ngx-charts';
import { ChartModule } from 'angular2-chartjs';

import { ThemeModule } from '../../@theme/theme.module';

import { UsersRoutingModule, routedComponents } from './users-routing.module';
import { SingleUserChartjsBarComponent } from './single-user/single-user-chartjs-bar.component';
import { SingleUserChartjsLineComponent } from './single-user/single-user-chartjs-line.component';
import { SingleUserChartjsPieComponent } from './single-user/single-user-chartjs-pie.component';
import { SingleUserChartjsMultipleXaxisComponent } from './single-user/single-user-chartjs-multiple-xaxis.component';
import { SingleUserChartjsBarHorizontalComponent } from './single-user/single-user-chartjs-bar-horizontal.component';
import { SingleUserChartjsRadarComponent } from './single-user/single-user-chartjs-radar.component';
import { AllUsersD3BarComponent } from './all-users/all-users-d3-bar.component';
import { AllUsersD3LineComponent } from './all-users/all-users-d3-line.component';
import { AllUsersD3PieComponent } from './all-users/all-users-d3-pie.component';
import { AllUsersD3AreaStackComponent } from './all-users/all-users-d3-area-stack.component';
import { AllUsersD3PolarComponent } from './all-users/all-users-d3-polar.component';
import { AllUsersD3AdvancedPieComponent } from './all-users/all-users-d3-advanced-pie.component';

const components = [
  SingleUserChartjsBarComponent,
  SingleUserChartjsLineComponent,
  SingleUserChartjsPieComponent,
  SingleUserChartjsMultipleXaxisComponent,
  SingleUserChartjsBarHorizontalComponent,
  SingleUserChartjsRadarComponent,
  AllUsersD3BarComponent,
  AllUsersD3LineComponent,
  AllUsersD3PieComponent,
  AllUsersD3AreaStackComponent,
  AllUsersD3PolarComponent,
  AllUsersD3AdvancedPieComponent,
];

@NgModule({
  imports: [ThemeModule, UsersRoutingModule, AngularEchartsModule, NgxChartsModule, ChartModule],
  declarations: [...routedComponents, ...components],
})
export class UsersModule {}
