import { NgModule } from '@angular/core';
import { AngularEchartsModule } from 'ngx-echarts';
import { NgxChartsModule } from '@swimlane/ngx-charts';
import { ChartModule } from 'angular2-chartjs';

import { ThemeModule } from '../../@theme/theme.module';

import { TrendingRoutingModule, routedComponents } from './trending-routing.module';
import { TrendingEchartsLineComponent } from './trending-components/trending-echarts-line.component';
import { TrendingEchartsPieComponent } from './trending-components/trending-echarts-pie.component';
import { TrendingEchartsBarComponent } from './trending-components/trending-echarts-bar.component';
import { TrendingEchartsMultipleXaxisComponent } from './trending-components/trending-echarts-multiple-xaxis.component';
import { TrendingEchartsAreaStackComponent } from './trending-components/trending-echarts-area-stack.component';
import { TrendingEchartsBarAnimationComponent } from './trending-components/trending-echarts-bar-animation.component';
import { TrendingEchartsRadarComponent } from './trending-components/trending-echarts-radar.component';

import {ComponentsModule} from '../components/components.module';


const components = [
  TrendingEchartsLineComponent,
  TrendingEchartsPieComponent,
  TrendingEchartsBarComponent,
  TrendingEchartsMultipleXaxisComponent,
  TrendingEchartsAreaStackComponent,
  TrendingEchartsBarAnimationComponent,
  TrendingEchartsRadarComponent,
];

@NgModule({
  imports: [ComponentsModule, ThemeModule, TrendingRoutingModule, AngularEchartsModule, NgxChartsModule, ChartModule],
  declarations: [...routedComponents, ...components],
})
export class TrendingModule {}
