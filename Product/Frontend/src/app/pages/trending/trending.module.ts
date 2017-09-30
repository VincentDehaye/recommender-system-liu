import { NgModule } from '@angular/core';
import { AngularEchartsModule } from 'ngx-echarts';
import { NgxChartsModule } from '@swimlane/ngx-charts';
import { ChartModule } from 'angular2-chartjs';

import { ThemeModule } from '../../@theme/theme.module';

import { TrendingRoutingModule, routedComponents } from './trending-routing.module';
import { TrendingWorldD3BarComponent } from './trending-world/trending-world-d3-bar.component';
import { TrendingWorldD3LineComponent } from './trending-world/trending-world-d3-line.component';
import { TrendingWorldD3PieComponent } from './trending-world/trending-world-d3-pie.component';
import { TrendingWorldD3AreaStackComponent } from './trending-world/trending-world-d3-area-stack.component';
import { TrendingWorldD3PolarComponent } from './trending-world/trending-world-d3-polar.component';
import { TrendingWorldD3AdvancedPieComponent } from './trending-world/trending-world-d3-advanced-pie.component';
import { TrendingLibraryEchartsLineComponent } from './trending-library/trending-library-echarts-line.component';
import { TrendingLibraryEchartsPieComponent } from './trending-library/trending-library-echarts-pie.component';
import { TrendingLibraryEchartsBarComponent } from './trending-library/trending-library-echarts-bar.component';
import { TrendingLibraryEchartsMultipleXaxisComponent } from './trending-library/trending-library-echarts-multiple-xaxis.component';
import { TrendingLibraryEchartsAreaStackComponent } from './trending-library/trending-library-echarts-area-stack.component';
import { TrendingLibraryEchartsBarAnimationComponent } from './trending-library/trending-library-echarts-bar-animation.component';
import { TrendingLibraryEchartsRadarComponent } from './trending-library/trending-library-echarts-radar.component';

const components = [
  TrendingWorldD3BarComponent,
  TrendingWorldD3LineComponent,
  TrendingWorldD3PieComponent,
  TrendingWorldD3AreaStackComponent,
  TrendingWorldD3PolarComponent,
  TrendingWorldD3AdvancedPieComponent,
  TrendingLibraryEchartsLineComponent,
  TrendingLibraryEchartsPieComponent,
  TrendingLibraryEchartsBarComponent,
  TrendingLibraryEchartsMultipleXaxisComponent,
  TrendingLibraryEchartsAreaStackComponent,
  TrendingLibraryEchartsBarAnimationComponent,
  TrendingLibraryEchartsRadarComponent,
];

@NgModule({
  imports: [ThemeModule, TrendingRoutingModule, AngularEchartsModule, NgxChartsModule, ChartModule],
  declarations: [...routedComponents, ...components],
})
export class TrendingModule {}
