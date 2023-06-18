#![cfg_attr(
    all(not(debug_assertions), target_os = "windows"),
    windows_subsystem = "windows"
)]

use tauri::{
    api::dialog::ask, http::ResponseBuilder, CustomMenuItem, Event, GlobalShortcutManager, Manager,
    RunEvent, SystemTray, SystemTrayEvent, SystemTrayMenu, WindowBuilder, WindowUrl,
  };

fn main() {
    let tray_menu = SystemTrayMenu::new()
        .add_item(CustomMenuItem::new("focus", "Get back on track"))
        .add_item(CustomMenuItem::new("quit", "Quit"));

    #[allow(unused_mut)]
    let mut app = tauri::Builder::default()
        .system_tray(SystemTray::new().with_menu(tray_menu))
        .on_system_tray_event(|_app, event| match event {
            SystemTrayEvent::MenuItemClick { id, .. } => {
                match id.as_str() {
                    "focus" => {
                        let window = _app.get_window("main").unwrap();
                        window.show().unwrap();
                        window.set_focus().unwrap();
                    }
                    "quit" => {
                        std::process::exit(0);
                    }
                    _ => {}
                }
            }
            _ => {}
        })
        .build(tauri::generate_context!())
        .expect("error while running tauri application");

    #[cfg(target_os = "macos")]
    app.set_activation_policy(tauri::ActivationPolicy::Regular);

    app.run(move |_app_handle, _event| {
        #[cfg(all(desktop, not(test)))]
        if let RunEvent::ExitRequested { api, .. } = &_event {
            // Keep the event loop running even if all windows are closed
            // This allow us to catch system tray events when there is no window
            api.prevent_exit();
        }
    })
}
