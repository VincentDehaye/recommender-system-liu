import { Component } from '@angular/core';

@Component({
  selector: 'ngx-footer',
  styleUrls: ['./footer.component.scss'],
  template: `
    <span class="created-by">
      Created by <b><a target="_blank">Coogl3</a></b>
    </span>
    <div class="socials">
      <a href="https://gitlab.ida.liu.se/PUM-Company3/Software" target="_blank" class="ion ion-social-github"></a>
    </div>
  `,
})
export class FooterComponent {
}
