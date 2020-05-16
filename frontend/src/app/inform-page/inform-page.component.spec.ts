import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { InformPageComponent } from './inform-page.component';

describe('InformPageComponent', () => {
  let component: InformPageComponent;
  let fixture: ComponentFixture<InformPageComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ InformPageComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(InformPageComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
