import { Component, OnDestroy } from '@angular/core';
import { NbThemeService } from '@nebular/theme';

@Component({
  selector: 'ngx-trending-score',
  styleUrls: ['./trending-score.component.scss'],
  template: `
    <nb-card size="xsmall">
      <nb-card-header>
        <span>Library Trending Score</span>
        <div class="ghost-dropdown" ngbDropdown>
          <button type="button" class="btn btn-sm" ngbDropdownToggle
                  [ngClass]="{ 'btn-success': currentTheme == 'default', 'btn-primary': currentTheme != 'default'}">
            {{ type }}
          </button>
          <ul class="dropdown-menu">
            <li class="dropdown-item" *ngFor="let t of types" (click)="type = t">{{ t }}</li>
          </ul>
        </div>
      </nb-card-header>
      <nb-card-body class="p-0">
        <ngx-trending-score-chart></ngx-trending-score-chart>
      </nb-card-body>
    </nb-card>
  `,
})
export class TrendingScoreComponent implements OnDestroy {
  type: string = 'month';
  types = ['week', 'month', 'year'];
  currentTheme: string;
  themeSubscription: any;

  constructor(private themeService: NbThemeService) {
    this.themeSubscription = this.themeService.getJsTheme().subscribe(theme => {
      this.currentTheme = theme.name;
    });
  }

  ngOnDestroy() {
    this.themeSubscription.unsubscribe();
  }
}
