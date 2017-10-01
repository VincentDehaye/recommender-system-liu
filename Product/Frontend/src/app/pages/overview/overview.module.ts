import { NgModule } from '@angular/core';
import { AngularEchartsModule } from 'ngx-echarts';

import { ThemeModule } from '../../@theme/theme.module';
import { OverviewComponent } from './overview.component';
import { StatusCardComponent } from './status-card/status-card.component';
import { ContactsComponent } from './contacts/contacts.component';
import { ActorsComponent } from './actors/actors.component';
import { TemperatureComponent } from './temperature/temperature.component';
import { TemperatureDraggerComponent } from './temperature/temperature-dragger/temperature-dragger.component';
import { TeamComponent } from './team/team.component';
import { KittenComponent } from './kitten/kitten.component';
import { InfoComponent } from './info/info.component';
import { SecurityCamerasComponent } from './security-cameras/security-cameras.component';
import { ContentListsComponent } from './content-lists/content-lists.component';
import { ElectricityComponent } from './electricity/electricity.component';
import { ElectricityChartComponent } from './electricity/electricity-chart/electricity-chart.component';
import { ViewsComponent } from './views/views.component';
import { ViewsChartComponent } from './views/views-chart/views-chart.component';
import { WeatherComponent } from './weather/weather.component';
import { SubscribersComponent } from './subscribers/subscribers.component';
import { SolarComponent } from './solar/solar.component';
import { RecommendationsPerformanceComponent } from './recommendations-performance/recommendations-performance.component';
import { TrafficComponent } from './traffic/traffic.component';
import { TrendingScoreComponent } from './trending-score/trending-score.component';
import { TrafficChartComponent } from './traffic/traffic-chart.component';
import { TrendingScoreChartComponent } from './trending-score/trending-score-chart.component';


@NgModule({
  imports: [
    ThemeModule,
    AngularEchartsModule,
  ],
  declarations: [
    OverviewComponent,
    StatusCardComponent,
    TemperatureDraggerComponent,
    ContactsComponent,
    ActorsComponent,
    TemperatureComponent,
    TeamComponent,
    KittenComponent,
    InfoComponent,
    SecurityCamerasComponent,
    ContentListsComponent,
    ElectricityComponent,
    ElectricityChartComponent,
    ViewsComponent,
    ViewsChartComponent,
    WeatherComponent,
    SubscribersComponent,
    SolarComponent,
    RecommendationsPerformanceComponent,
    TrendingScoreComponent,
    TrendingScoreChartComponent,
    TrafficComponent,
    TrafficChartComponent,
  ],
})
export class OverviewModule { }
