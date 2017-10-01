import { NgModule } from '@angular/core';
import { AngularEchartsModule } from 'ngx-echarts';
import { NgxChartsModule } from '@swimlane/ngx-charts';
import { ChartModule } from 'angular2-chartjs';

import { ThemeModule } from '../../@theme/theme.module';

import { RecommendedRoutingModule, routedComponents } from './recommended-routing.module';
import { RecommendedChartjsBarComponent } from './recommended-components/recommended-chartjs-bar.component';
import { RecommendedChartjsLineComponent } from './recommended-components/recommended-chartjs-line.component';
import { RecommendedChartjsPieComponent } from './recommended-components/recommended-chartjs-pie.component';
import { RecommendedChartjsMultipleXaxisComponent } from './recommended-components/recommended-chartjs-multiple-xaxis.component';
import { RecommendedChartjsBarHorizontalComponent } from './recommended-components/recommended-chartjs-bar-horizontal.component';
import { RecommendedChartjsRadarComponent } from './recommended-components/recommended-chartjs-radar.component';

const components = [
  RecommendedChartjsBarComponent,
  RecommendedChartjsLineComponent,
  RecommendedChartjsPieComponent,
  RecommendedChartjsMultipleXaxisComponent,
  RecommendedChartjsBarHorizontalComponent,
  RecommendedChartjsRadarComponent,
];

@NgModule({
  imports: [ThemeModule, RecommendedRoutingModule, AngularEchartsModule, NgxChartsModule, ChartModule],
  declarations: [...routedComponents, ...components],
})
export class RecommendedModule {}
