import { NgModule } from '@angular/core';
import { AngularEchartsModule } from 'ngx-echarts';
import { NgxChartsModule } from '@swimlane/ngx-charts';
import { ChartModule } from 'angular2-chartjs';
import { OverviewChartjsPieComponent } from './overview-components/rec-chartjs-pie.component';

import { ModalsComponent } from '../components/modals/modals.component'
import { ModalComponent } from '../components/modals/modal/modal.component'


import { ThemeModule } from '../../@theme/theme.module';
import { OverviewComponent } from './overview.component';
import { OverviewRoutingModule, routedComponents } from './overview-routing.module';


const components = [
    OverviewChartjsPieComponent,
    ModalsComponent,
    ModalComponent,
];
@NgModule({
  imports: [ThemeModule, AngularEchartsModule, NgxChartsModule, ChartModule, OverviewRoutingModule,
  ],
  declarations: [OverviewComponent , ...routedComponents, ...components],
  entryComponents: [
    ModalComponent,
  ],
})
export class OverviewModule {}
