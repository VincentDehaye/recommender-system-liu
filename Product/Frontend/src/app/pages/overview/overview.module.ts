import { NgModule } from '@angular/core';
import { AngularEchartsModule } from 'ngx-echarts';

import { ThemeModule } from '../../@theme/theme.module';
import { OverviewComponent } from './overview.component';
import { StatusCardComponent } from './status-card/status-card.component';
import { ActorsComponent } from './actors/actors.component';
import { InfoComponent } from './info/info.component';
import { ContentListsComponent } from './content-lists/content-lists.component';
import { ViewsComponent } from './views/views.component';
import { ViewsChartComponent } from './views/views-chart/views-chart.component';
import { SubscribersComponent } from './subscribers/subscribers.component';
import { RecommendationsPerformanceComponent } from './recommendations-performance/recommendations-performance.component';
import { TrendingScoreComponent } from './trending-score/trending-score.component';
import { TrendingScoreChartComponent } from './trending-score/trending-score-chart.component';


@NgModule({
  imports: [
    ThemeModule,
    AngularEchartsModule,
  ],
  declarations: [
    OverviewComponent,
    StatusCardComponent,
    ActorsComponent,
    InfoComponent,
    ContentListsComponent,
    ViewsComponent,
    ViewsChartComponent,
    SubscribersComponent,
    RecommendationsPerformanceComponent,
    TrendingScoreComponent,
    TrendingScoreChartComponent,
  ],
})
export class OverviewModule { }
